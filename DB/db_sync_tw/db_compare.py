from DataBaseUtils import *
import pandas as pd

shopee_db = {"host": "10.12.77.188",
             "user": "test",
             "password": "123456",
             "port": 3306,
             "db": "shopee_location_db"}

# shopee_db = {"host": "master.shopee_location.mysql.cloud.test.shopee.io",
#              "user": "coreserver",
#              "password": "i1wQJWs2Lqv08V91cW_k",
#              "port": 6606,
#              "db": "shopee_location_db"}

csv_path = "tw_l3.csv"


def transfer_tuple_to_df(back_data):
    name = []
    parentid = []
    div_id = []
    level = []
    for i in back_data:
        name.append(i[0])
        parentid.append(i[1])
        div_id.append(i[2])
        level.append(i[3])

    dic_data = {"name": name, "parentid": parentid, "div_id": div_id, "level": level}

    df = pd.DataFrame(dic_data)

    return df


def get_df_from_shopee_location_db(region):
    db_handle = DataBaseHandle(shopee_db["host"], shopee_db["user"],
                               shopee_db["password"], shopee_db["port"],
                               shopee_db["db"])
    sql_str = "SELECT division_name, parent_id, division_id, division_level FROM location_division_tab WHERE region=\""\
              + region + "\"  AND division_status=1 ORDER BY division_name"
    db_data = db_handle.query_all_from_db(sql_str)
    db_handle.close_db()

    df = transfer_tuple_to_df(db_data)

    return df


def obtain_level_data_with_parant(df, level):
    df_level = df[df["level"] == level]
    new_index = [i for i in range(df_level.shape[0])]
    df_level.index = pd.Series(new_index)

    parentname=[]
    for i in range(df_level.shape[0]):
        df1 = df[df["div_id"] == df_level.iloc[i]['parentid']]
        if len(df1.index) == 0:
            parentname.append("000")
        else:
            parentname.append(df1["name"].iloc[0])

    dicc = {"parentname": parentname}
    df2 = pd.DataFrame(dicc)

    df = pd.concat([df_level, df2], axis=1)

    return df


def obtain_level_data_with_father_grand_father(df, level):
    df_level = df[df["level"] == level]
    new_index = [i for i in range(df_level.shape[0])]
    df_level.index = pd.Series(new_index)

    father_name = []
    grand_name = []
    for i in range(df_level.shape[0]):
        df1 = df[df["div_id"] == df_level.iloc[i]['parentid']]
        if len(df1.index) == 0:
            father_name.append("000")
            grand_name.append("000")
        else:
            father_name.append(df1["name"].iloc[0])
            df2 = df[df["div_id"] == df1["parentid"].iloc[0]]
            if len(df2.index) == 0:
                grand_name.append("000")
            else:
                grand_name.append(df2["name"].iloc[0])

    dicc = {"father_name": father_name, "grand_name": grand_name}
    df2 = pd.DataFrame(dicc)

    df = pd.concat([df_level, df2], axis=1)

    return df


def get_combined_data(df, cow1, cow2, cow3):
    df["combined_name"] = df.apply(lambda x: x[cow1] + x[cow2] + x[cow3], axis=1)
    df_cluster = df[["combined_name", cow1, cow2, cow3]]

    return df_cluster


def transfer_family_dic_from_db(df_db):
    name_db = df_db['combined_name'].tolist()
    # parent_db = df_db['parentname'].tolist()
    div_db = df_db["name"].tolist()

    dic_db = {}
    for i in range(len(name_db)):
        key = name_db[i].strip()  # ignore space
        div_name = div_db[i].strip()
        if key not in dic_db:
            dic_db[key] = [div_name]
        else:
            dic_db[key].append(div_name)
        if len(dic_db[key]) > 1:
            print(dic_db[key], "duplicate name-" + div_name + "----------------")

    return dic_db


def compare_level_data_from_2_tab(df_db, df_csv):
    dic_db = transfer_family_dic_from_db(df_db)

    error_name = []
    success_name = []
    for i in range(df_csv.shape[0]):
        div_name_csv = df_csv["Level 3"][i].strip()  # ignore space
        name_csv = df_csv["combined_name"][i].strip()  # ignore space
        father_csv = df_csv["Level 2"][i].strip()  # ignore space
        grand_csv = df_csv["Level 1"][i].strip()  # ignore space
        if name_csv not in dic_db:
            error_name.append(div_name_csv)
            print(div_name_csv + " with parentname :" + father_csv + "," + grand_csv + " not in db, Failed!!!")
        else:
            success_name.append(div_name_csv)

    return error_name, success_name


if __name__ == '__main__':
    print("---start---")
    df1 = get_df_from_shopee_location_db("TW")
    df2 = obtain_level_data_with_father_grand_father(df1, 3)
    df_db_cluster = get_combined_data(df2, "name", "father_name", "grand_name")

    print(df_db_cluster.head(10))

    df4 = pd.read_csv('tw_l3.csv')
    df_csv_cluster = get_combined_data(df4, "Level 3", "Level 2", "Level 1")
    print(df_csv_cluster.head(10))

    err, success = compare_level_data_from_2_tab(df_db_cluster, df_csv_cluster)

    if len(err) > 0:
        print("there are {} district don't match ".format(len(err)))
        print(success)
    else:
        print("It is ok for QA")


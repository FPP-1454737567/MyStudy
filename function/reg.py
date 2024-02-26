class Result:
    def __init__(self):
        self.datas = {}

    def set_data(self, item, datas = []):
        self.datas[item] = datas

    def print_data(self):
        print('datas:', self.datas)


if __name__ == '__main__':
    RES = Result()
    A = ["AA", "BB"]
    RES.set_data('name', A)
    RES.print_data()
    A.clear
    print("A被清除后的值：", A)
    RES.print_data()



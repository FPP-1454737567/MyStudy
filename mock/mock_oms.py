import os

from flask import abort, jsonify, Flask, request, Response

app = Flask(__name__)
# 增加配置，支持中文显示
app.config['JSON_AS_ASCII'] = False

tasks = {
  "header": {
    "seq_id": "8734897192",
    "retcode": 0,
    "rettype": "xxx",
    "message": ""
  },
  "order_info": {
    "order_id": 943561,
    "split_up": 0,
    "order_status": 1001,
    "order_action": {
      "can_split": 1,
      "can_unsplit": 0
    },
    "forders": [
      {
        "forder_id": "943561",
        "ofg_id": "943561001",
        "status": 5,
        "parcel_no": 1,
        "third_party_tn": "298396687",
        "consignment_no": "458399689",
        "total_price": 200400000,
        "shipping_fee": 400000,
        "shipping_fee_discount": 0,
        "items": [
          {
            "item_id": 1700214,
            "model_id": 0,
            "order_item_id": 1700214,
            "virtual_item_id": 12332,
            "virtual_model_id": 12,
            "group_id": 0,
            "item_price": 200000000,
            "quantity": 1,
            "mp_item_id": 111700214,
            "mp_model_id": 0
          }
        ],
        "latest_route_info":"XXXXXX",
        "tracking_info": [
          {
            "flag": 2,
            "description": "[Thái Bình Huyện Kiến]Reconciled (GHTK:298396687)",
            "ctime": 1541140151,
            "id": 312312,
            "logid": 212121,
            "driver_name": "aaabbb",
            "driver_phone": "123456",
            "license_plate_number": "123456",
            "receiver_name": "bo.deng",
            "epod": "XXXXXX",
            "extra_data": "{\"pin_code\":\"12345\"}",
            "pin_code": "12345",
            "tracking_code":"XXX"
          }
        ],
        "allocating_status": 1,
        "channel_id": 50012,
        "masking_channel_id": 50012,
        "carrier_name": "Giao Hàng Tiết Kiệm",
        "masking_carrier_name": "Giao Hàng Tiết Kiệm",
        "is_arrived_tws": True,
        "logistics_flag": 8,
        "shipping_method": 10086,
        "forder_status": 3001,
        "pickup_time": 1540196141,
        "actual_pickup_time": 1540196141,
        "auto_cancel_layer2": 1540196141,
        "preferred_delivery_timeslot": 1540196141,
        "asf_chargeable_weight": 123,
        "asf_distance":123,
        "fulfillment_type":3,
        "whs_id": "IDG",
        "slug_id": "abcdge",
        "plp_number": "abcdge"
      }
    ]
  }
}

@app.route('/mock_oms', methods=['GET','POST'])
def get_task():
    return jsonify(tasks)


if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 6868,debug = True)

# url:127.0.0.1:6868/mock_test
# url：10.12.184.230/mock_oms


from . import device_uploadinfo
import json
from flask import request, jsonify


# device_uploadinfo/deviceAlarmDistrictInfo
# 获取所有正在报警的行政区（POST）
@device_uploadinfo.route('/deviceAlarmDistrictInfo', methods=['POST'])
def getDeviceAlarmDistrictInfo():
    res = {
        "code": "200",
        "message": "请求成功!",
        "status": True,
        "data": {
            "code": 0,
            "msg": "success",
            "result": {
                "alarmDistrict": ["500151"]
            },
            "errorCode": "ERROR_CODE_SUCCESS"
        }
    }
    return json.dumps(res, ensure_ascii=False, indent=4)


# device_uploadinfo/deviceAlarmHouseInfoUrl
@device_uploadinfo.route('/deviceAlarmHouseInfoUrl', methods=['POST'])
def getDeviceAlarmHouseInfoUrl():
    data = json.loads(request.data.decode('utf-8'))['districtCode']
    if (data == "500151"):
        res = {
            "code": "200",
            "message": "请求成功!",
            "status": True,
            "data": {
                "code": 0,
                "msg": "success",
                "result": {
                    "deviceAlarmHouseInfoArrayList": [{
                        "wfbh": "500151005001026",
                        "type": "1"
                    }, {
                        "wfbh": "500151015001007",
                        "type": "2"
                    }, {
                        "wfbh": "500151015001025",
                        "type": "3"
                    }]
                },
                "errorCode": "ERROR_CODE_SUCCESS"
            }
        }
        return json.dumps(res, ensure_ascii=False, indent=4)
    else:
        res = {
            "code": "200",
            "message": "请求成功!",
            "status": True,
            "data": {
                "code": 0,
                "msg": "success",
                "result": {
                    "deviceAlarmHouseInfoArrayList": []
                },
                "errorCode": "ERROR_CODE_SUCCESS"
            }
        }
        return json.dumps(res, ensure_ascii=False, indent=4)


# device_uploadinfo/deviceAlarmDeviceInfo
@device_uploadinfo.route('/deviceAlarmDeviceInfo', methods=['POST'])
def getDeviceAlarmDeviceInfo():
    data = json.loads(request.data.decode('utf-8'))['houseCode']
    print("houseCode==>", json.loads(request.data.decode('utf-8'))['houseCode'])
    # data_json = json.loads(data)
    res = {
        "code": "200",
        "message": "请求成功!",
        "status": True,
        "data": {
            "code": 0,
            "msg": "success",
            "result": {
                "deviceAlarmDeviceInfoArrayList": [
                    {
                        "id": 2,
                        "wfbh": data,
                        "cgqbh": "test2",
                        "type": "receive",
                        "alarmInfo": "倾斜传感器大于设定阈值",
                        "alarmDate": "2021-05-11 10:44:52"
                    },
                    {
                        "id": 1,
                        "wfbh": data,
                        "cgqbh": "test1",
                        "type": "receive",
                        "alarmInfo": "倾斜传感器大于设定阈值",
                        "alarmDate": "2021-05-11 10:43:17"
                    }
                ]
            },
            "errorCode": "ERROR_CODE_SUCCESS"
        }
    }
    return json.dumps(res, ensure_ascii=False, indent=4)


@device_uploadinfo.route('/getDangerBuildingByDangerBuildingNum', methods=['GET'])
def getHouseDz():
    data = request.args.get('dangerBuildingNum')
    print("dangerBuildingNum==>", data)
    # data_json = json.loads(data)
    res = {
        "code": "200",
        "message": "请求成功!",
        "status": True,
        "data": {
            "code": "200",
            "msg": "success",
            "wfbh": data,
            "xxdz": "铜梁测试地址",
            "errorCode": "ERROR_CODE_SUCCESS"
        }
    }
    return json.dumps(res, ensure_ascii=False, indent=4)

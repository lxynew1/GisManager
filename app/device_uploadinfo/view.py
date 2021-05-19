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
                        "id": 2,
                        "wfbh": data,
                        "cgqbh": "test2",
                        "type": "receive",
                        "alarmInfo": "倾斜传感器大于设定阈值",
                        "alarmDate": "2021-05-11 10:44:52"
                    },
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


@device_uploadinfo.route('/deviceUploadInfo', methods=['POST'])
def getDeviceUploadInfo():
    # data = json.loads(request.data.decode('utf-8'))['deviceCode']
    # data_json = json.loads(data)
    res = {
        "code": "200",
        "data": {
            "code": 0,
            "msg": "success",
            "result": {
                "deviceUploadInfoList": [
                    {
                        "createDate": "2020-01-01 09:00",
                        "deviceName": "设备1",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "13",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 12:00",
                        "deviceName": "设备1",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "7",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 14:00",
                        "deviceName": "设备1",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "12",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 15:00",
                        "deviceName": "设备1",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "8",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 19:00",
                        "deviceName": "设备1",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "1",
                        "x": 0,
                        "y": 0
                    },
                    {
                        "createDate": "2020-01-01 20:00",
                        "deviceName": "设备1",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "8",
                        "x": 0,
                        "y": 0
                    },
                    {
                        "createDate": "2020-01-01 09:00",
                        "deviceName": "设备7",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "3",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 12:00",
                        "deviceName": "设备7",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "1",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 14:00",
                        "deviceName": "设备7",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "10",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 15:00",
                        "deviceName": "设备7",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "9",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 19:00",
                        "deviceName": "设备7",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "3",
                        "x": 0,
                        "y": 0
                    },
                    {
                        "createDate": "2020-01-01 20:00",
                        "deviceName": "设备7",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "6",
                        "x": 0,
                        "y": 0
                    },
                    {
                        "createDate": "2020-01-01 09:00",
                        "deviceName": "设备2",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "9",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 12:00",
                        "deviceName": "设备2",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "5",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 14:00",
                        "deviceName": "设备2",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "24",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 15:00",
                        "deviceName": "设备2",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "6",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 19:00",
                        "deviceName": "设备2",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "3",
                        "x": 0,
                        "y": 0
                    },
                    {
                        "createDate": "2020-01-01 20:00",
                        "deviceName": "设备2",
                        "id": 0,
                        "intValue": 0,
                        "type": "crevice",
                        "value": "7",
                        "x": 0,
                        "y": 0
                    }
                    , {
                        "createDate": "2020-01-01 09:00",
                        "deviceName": "设备5",
                        "id": 0,
                        "intValue": 0,
                        "type": "receive",
                        "value": "13",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 12:00",
                        "deviceName": "设备5",
                        "id": 0,
                        "intValue": 0,
                        "type": "receive",
                        "value": "7",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 14:00",
                        "deviceName": "设备5",
                        "id": 0,
                        "intValue": 0,
                        "type": "receive",
                        "value": "12",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 15:00",
                        "deviceName": "设备5",
                        "id": 0,
                        "intValue": 0,
                        "type": "receive",
                        "value": "8",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 19:00",
                        "deviceName": "设备5",
                        "id": 0,
                        "intValue": 0,
                        "type": "receive",
                        "value": "1",
                        "x": 0,
                        "y": 0
                    },
                    {
                        "createDate": "2020-01-01 20:00",
                        "deviceName": "设备5",
                        "id": 0,
                        "intValue": 0,
                        "type": "receive",
                        "value": "8",
                        "x": 0,
                        "y": 0
                    },
                    {
                        "createDate": "2020-01-01 09:00",
                        "deviceName": "设备6",
                        "id": 0,
                        "intValue": 0,
                        "type": "receive",
                        "value": "9",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 12:00",
                        "deviceName": "设备6",
                        "id": 0,
                        "intValue": 0,
                        "type": "receive",
                        "value": "5",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 14:00",
                        "deviceName": "设备6",
                        "id": 0,
                        "intValue": 0,
                        "type": "receive",
                        "value": "24",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 15:00",
                        "deviceName": "设备6",
                        "id": 0,
                        "intValue": 0,
                        "type": "receive",
                        "value": "6",
                        "x": 0,
                        "y": 0
                    }, {
                        "createDate": "2020-01-01 19:00",
                        "deviceName": "设备6",
                        "id": 0,
                        "intValue": 0,
                        "type": "receive",
                        "value": "3",
                        "x": 0,
                        "y": 0
                    },
                    {
                        "createDate": "2020-01-01 20:00",
                        "deviceName": "设备6",
                        "id": 0,
                        "intValue": 0,
                        "type": "receive",
                        "value": "7",
                        "x": 0,
                        "y": 0
                    },
                    {
                        "createDate": "2020-01-01 9:00",
                        "deviceName": "设备3",
                        "id": 0,
                        "intValue": 0,
                        "type": "slant",
                        "value": "7",
                        "x": 7,
                        "y": -2
                    }, {
                        "createDate": "2020-01-01 12:00",
                        "deviceName": "设备3",
                        "id": 0,
                        "intValue": 0,
                        "type": "slant",
                        "value": "7",
                        "x": 8,
                        "y": -15
                    }, {
                        "createDate": "2020-01-01 13:00",
                        "deviceName": "设备3",
                        "id": 0,
                        "intValue": 0,
                        "type": "slant",
                        "value": "7",
                        "x": 4,
                        "y": -4
                    }, {
                        "createDate": "2020-01-01 15:00",
                        "deviceName": "设备3",
                        "id": 0,
                        "intValue": 0,
                        "type": "slant",
                        "value": "7",
                        "x": 5,
                        "y": -10
                    }, {
                        "createDate": "2020-01-01 18:00",
                        "deviceName": "设备3",
                        "id": 0,
                        "intValue": 0,
                        "type": "slant",
                        "value": "7",
                        "x": 7,
                        "y": -9
                    }, {
                        "createDate": "2020-01-01 20:00",
                        "deviceName": "设备3",
                        "id": 0,
                        "intValue": 0,
                        "type": "slant",
                        "value": "0",
                        "x": 1,
                        "y": -2
                    },
                    {
                        "createDate": "2020-01-01 9:00",
                        "deviceName": "zbm-cqtest-20210428-01-lf-01-01",
                        "id": 0,
                        "intValue": 0,
                        "type": "slant",
                        "value": "7",
                        "x": 7,
                        "y": -2
                    }, {
                        "createDate": "2020-01-01 12:00",
                        "deviceName": "zbm-cqtest-20210428-01-lf-01-01",
                        "id": 0,
                        "intValue": 0,
                        "type": "slant",
                        "value": "7",
                        "x": 8,
                        "y": -15
                    }, {
                        "createDate": "2020-01-01 13:00",
                        "deviceName": "zbm-cqtest-20210428-01-lf-01-01",
                        "id": 0,
                        "intValue": 0,
                        "type": "slant",
                        "value": "7",
                        "x": 4,
                        "y": -4
                    }, {
                        "createDate": "2020-01-01 15:00",
                        "deviceName": "zbm-cqtest-20210428-01-lf-01-01",
                        "id": 0,
                        "intValue": 0,
                        "type": "slant",
                        "value": "7",
                        "x": 5,
                        "y": -10
                    }, {
                        "createDate": "2020-01-01 18:00",
                        "deviceName": "zbm-cqtest-20210428-01-lf-01-01",
                        "id": 0,
                        "intValue": 0,
                        "type": "slant",
                        "value": "7",
                        "x": 7,
                        "y": -9
                    }, {
                        "createDate": "2020-01-01 20:00",
                        "deviceName": "zbm-cqtest-20210428-01-lf-01-01",
                        "id": 0,
                        "intValue": 0,
                        "type": "slant",
                        "value": "0",
                        "x": 1,
                        "y": -2
                    }
                ]
            },
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
            "xxdz": "测试地址",
            "errorCode": "ERROR_CODE_SUCCESS",

        }
    }
    return json.dumps(res, ensure_ascii=False, indent=4)

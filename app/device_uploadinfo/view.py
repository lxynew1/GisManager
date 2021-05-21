# coding:utf-8
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
                "alarmDistrict": ["500112"]
            },
            "errorCode": "ERROR_CODE_SUCCESS"
        }
    }
    return json.dumps(res, ensure_ascii=False, indent=4)


# device_uploadinfo/deviceAlarmHouseInfoUrl
@device_uploadinfo.route('/deviceAlarmHouseInfoUrl', methods=['POST'])
def getDeviceAlarmHouseInfoUrl():
    data = json.loads(request.data.decode('utf-8'))['districtCode']
    if (data == "500112"):
        res = {
            "code": "200",
            "message": "请求成功!",
            "status": True,
            "data": {
                "code": 0,
                "msg": "success",
                "result": {
                    "deviceAlarmHouseInfoArrayList": [{
                        "wfbh": "500112016005001",
                        "type": "1"
                    }, {
                        "wfbh": "500112142001036",
                        "type": "1"
                    }, {
                        "wfbh": "500112018001031",
                        "type": "1"
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
    # // slant: "倾斜传感器" 设备4,
    # // crevice: "裂缝传感器" 设备1,
    # // strain: "应变传感器" 设备2,
    # // sink: "沉降传感器" 设备3,
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
                        "id": 1,
                        "wfbh": data,
                        "cgqbh": "设备1",
                        "type": "3",
                        "alarmInfo": "裂缝传感器大于设定阈值",
                        "alarmDate": "2021-05-11 10:44:52"
                    },
                    {
                        "id": 2,
                        "wfbh": data,
                        "cgqbh": "设备2",
                        "type": "2",
                        "alarmInfo": "应变传感器大于设定阈值",
                        "alarmDate": "2021-05-11 10:44:52"
                    },
                    {
                        "id": 3,
                        "wfbh": data,
                        "cgqbh": "设备3",
                        "type": "1",
                        "alarmInfo": "沉降传感器大于设定阈值",
                        "alarmDate": "2021-05-11 10:44:52"
                    },
                    {
                        "id": 4,
                        "wfbh": data,
                        "cgqbh": "设备4",
                        "type": "1",
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
    data = json.loads(request.data.decode('utf-8'))['deviceCode']
    type = ''
    # // slant: "倾斜传感器" 设备4,
    # // crevice: "裂缝传感器" 设备1,
    # // strain: "应变传感器" 设备2,
    # // sink: "沉降传感器" 设备3,
    if data == '设备1':
        type = 'crevice'
    elif data == '设备2':
        type = 'strain'
    elif data == '设备3':
        type = 'sink'
    elif data == '设备4':
        type = 'slant'
    msgs = [
        {
            "createDate": "2020-01-01 09:00",
            "deviceName": data,
            "id": 0,
            "intValue": 0,
            "type": type,
            "value": "13",
            "x": 10,
            "y": -8
        }, {
            "createDate": "2020-01-01 12:00",
            "deviceName": data,
            "id": 0,
            "intValue": 0,
            "type": type,
            "value": "7",
            "x": 6,
            "y": -2
        }, {
            "createDate": "2020-01-01 14:00",
            "deviceName": data,
            "id": 0,
            "intValue": 0,
            "type": type,
            "value": "12",
            "x": 9,
            "y": -5
        }, {
            "createDate": "2020-01-01 15:00",
            "deviceName": data,
            "id": 0,
            "intValue": 0,
            "type": type,
            "value": "8",
            "x": 9,
            "y": -6
        }, {
            "createDate": "2020-01-01 20:00",
            "deviceName": data,
            "id": 0,
            "intValue": 0,
            "type": type,
            "value": "5",
            "x": 5,
            "y": -7
        }, ]

    # data_json = json.loads(data)
    res = {
        "code": "200",
        "data": {
            "code": 0,
            "msg": "success",
            "result": {
                "deviceUploadInfoList": msgs
            },
        }
    }
    return json.dumps(res, ensure_ascii=False, indent=4)


@device_uploadinfo.route('/getDangerBuildingByDangerBuildingNum', methods=['GET'])
def getHouseDz():
    data = request.args.get('dangerBuildingNum')
    xxdz = ''
    print("dangerBuildingNum==>", data)
    if data == '500112018001031':
        xxdz = "渝北区王家社区老街31幢天子路65号"
    elif data == '500112142001036':
        xxdz = "渝北区石船镇渝长社区中街32附1号"
    elif data == '500112016005001':
        xxdz = "渝北区两路街道双凤路一巷1栋7号"
    # data_json = json.loads(data)
    res = {
        "code": "200",
        "message": "请求成功!",
        "status": True,
        "data": {
            "code": "200",
            "msg": "success",
            "wfbh": data,
            "xxdz": xxdz,
            "dangerBuildingGradeName": "C级",
            "fwjgName": "其他",
            "fwxzName": "社会私房",
            "sjytName": "住宅",
            "errorCode": "ERROR_CODE_SUCCESS",
        }
    }
    return json.dumps(res, ensure_ascii=False, indent=4)

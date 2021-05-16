import urllib.request, urllib.parse, urllib.error
import http.client
import json
import datetime


def getToken(username, password, serviceAddress, servicePort):
    # Token URL is typically http://server[:port]/arcgis/admin/generateToken
    tokenURL = "/arcgis/admin/generateToken"

    # URL-encode the token parameters:-
    params = urllib.parse.urlencode(
        {'username': username, 'password': password, 'client': 'requestip', 'f': 'json'})

    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    # Connect to URL and post parameters

    httpConn = http.client.HTTPConnection(serviceAddress, servicePort)
    httpConn.request("POST", tokenURL, params, headers)
    # Read response
    response = httpConn.getresponse()
    if (response.status != 200):
        httpConn.close()
        print(
            "Error while fetch tokens from admin URL. Please check the URL and try again.")
        return
    else:
        data = response.read()
        httpConn.close()

        # Extract the token from it
        token = json.loads(data)
        return token


def serviceEdit(serviceName="tjrc/RCRouteV3.MapServer", serviceState="edit", username="siteadmin", password="siteadmin",
                serviceAddress="10.73.9.20", servicePort="6080"):
    token = getToken(username, password, serviceAddress, servicePort)['token']
    print("token:", token)
    URL = "/arcgis/admin/services/" + serviceName + "/" + serviceState

    # URL-encode the token parameters:-
    params = urllib.parse.urlencode(
        {"Token": token, 'f': 'json', "service": '''{
 "serviceName": "RCRouteV3",
 "type": "MapServer",
 "description": "",
 "capabilities": "Map,Query,Data",
 "provider": "ArcObjects",
 "interceptor": "",
 "clusterName": "default",
 "minInstancesPerNode": 1,
 "maxInstancesPerNode": 2,
 "instancesPerContainer": 1,
 "maxWaitTime": 10,
 "maxStartupTime": 300,
 "maxIdleTime": 1,
 "maxUsageTime": 10,
 "loadBalancing": "ROUND_ROBIN",
 "isolationLevel": "HIGH",
 "configuredState": "STARTED",
 "recycleInterval": 1,
 "recycleStartTime": "00:00",
 "keepAliveInterval": 60,
 "private": false,
 "isDefault": false,
 "maxUploadFileSize": 0,
 "allowedUploadFileTypes": "",
 "properties": {
  "maxImageHeight": "4096",
  "virtualCacheDir": "/rest/directories/arcgiscache",
  "maxSampleSize": "100000",
  "exportTilesAllowed": "false",
  "textAntialiasingMode": "Force",
  "maxImageWidth": "4096",
  "enableDynamicLayers": "false",
  "dynamicDataWorkspaces": "[]",
  "supportedImageReturnTypes": "URL",
  "disableIdentifyRelates": "false",
  "isCached": "false",
  "maxScale": "4513.9887049999998",
  "maxBufferCount": "100",
  "schemaLockingEnabled": "true",
  "maxRecordCount": "1000",
  "filePath": "D:/arcgisserver/directories/arcgissystem/arcgisinput/tjrc/RCRouteV3.MapServer/extracted/v101/RCRoute.msd",
  "cacheOnDemand": "false",
  "useLocalCacheDir": "true",
  "outputDir": "D:/arcgisserver/directories/arcgisoutput",
  "virtualOutputDir": "/rest/directories/arcgisoutput",
  "minScale": "18055.954822",
  "maxDomainCodeCount": "25000",
  "maxExportTilesCount": "100000",
  "tilingScheme": "3",
  "ignoreCache": "false",
  "antialiasingMode": "None",
  "clientCachingAllowed": "true",
  "cacheDir": "D:/arcgisserver/directories/arcgiscache"
 },
 "extensions": [
  {
   "typeName": "NAServer",
   "capabilities": "null",
   "enabled": "true",
   "maxUploadFileSize": 0,
   "allowedUploadFileTypes": "",
   "properties": {
    "oDCostMatrix_MaxDestinationsToFind": "",
    "serviceArea_MaxBreakValue_TimeUnits": "esriTimeUnitsMinutes",
    "vRP_MaxFeaturesInPolygonBarriers": "",
    "vRP_MaxRoutes": "",
    "serviceArea_MaxBarriers": "",
    "route_MaxFeaturesInLineBarriers": "",
    "vRP_ForceHierarchyBeyondDistanceUnits": "esriMeters",
    "route_ForceHierarchyBeyondDistanceUnits": "esriMeters",
    "locationAllocation_MaxDemandPoints": "",
    "closestFacility_MaxFeaturesInPolygonBarriers": "",
    "closestFacility_MaxFacilities": "",
    "oDCostMatrix_MaxDestinations": "",
    "serviceArea_MaxBreakValue_Length": "",
    "serviceArea_ForceHierarchyBeyondTimeUnits": "esriTimeUnitsMinutes",
    "serviceArea_ForceHierarchyBeyondDistanceUnits": "esriMeters",
    "vRP_MaxFeaturesInLineBarriers": "",
    "closestFacility_ForceHierarchyBeyondDistanceUnits": "esriMeters",
    "route_AllowTimeWindows": "true",
    "serviceArea_MaxFacilities": "",
    "locationAllocation_MaxFeaturesInPolygonBarriers": "",
    "oDCostMatrix_MaxFeaturesInLineBarriers": "",
    "route_MaxFeaturesInPolygonBarriers": "",
    "locationAllocation_ForceHierarchyBeyondDistance": "",
    "saveLayerOnServerWhenError": "false",
    "route_ForceHierarchyBeyondDistance": "",
    "locationAllocation_ForceHierarchyBeyondDistanceUnits": "esriMeters",
    "serviceArea_ForceHierarchyBeyondTime": "",
    "route_MaxStops": "",
    "serviceArea_MaxFeaturesInLineBarriers": "",
    "closestFacility_MaxIncidents": "",
    "oDCostMatrix_ForceHierarchyBeyondDistanceUnits": "esriMeters",
    "allowSaveLayerOnServer": "true",
    "route_MaxBarriers": "",
    "vRP_MaxBarriers": "",
    "oDCostMatrix_ForceHierarchyBeyondDistance": "",
    "serviceArea_MaxBreakValue_LengthUnits": "esriMeters",
    "serviceArea_ForceHierarchyBeyondDistance": "",
    "saveLayerOnServerWhenDebugging": "false",
    "closestFacility_MaxFeaturesInLineBarriers": "",
    "oDCostMatrix_MaxFeaturesInPolygonBarriers": "",
    "oDCostMatrix_MaxBarriers": "",
    "closestFacility_MaxFacilitiesToFind": "",
    "closestFacility_MaxBarriers": "",
    "serviceArea_MaxBreakValue_Other": "",
    "defaultOutputGeometryPrecisionUnits": "esriMeters",
    "vRP_ForceHierarchyBeyondDistance": "",
    "oDCostMatrix_MaxOrigins": "",
    "locationAllocation_MaxBarriers": "",
    "locationAllocation_MaxFeaturesInLineBarriers": "",
    "closestFacility_ForceHierarchyBeyondDistance": "",
    "nALayerDir": "D:/arcgisserver/directories/arcgisoutput",
    "vRP_MaxOrders": "",
    "serviceArea_ForceHierarchyBeyondOther": "",
    "defaultOutputGeometryPrecision": "",
    "serviceArea_MaxFeaturesInPolygonBarriers": "",
    "serviceArea_MaxBreakValue_Time": "",
    "locationAllocation_MaxFacilities": ""
   }
  },
  {
   "typeName": "MobileServer",
   "capabilities": "",
   "enabled": "false",
   "maxUploadFileSize": 0,
   "allowedUploadFileTypes": "",
   "properties": {}
  },
  {
   "typeName": "KmlServer",
   "capabilities": "SingleImage,SeparateImages,Vectors",
   "enabled": "true",
   "maxUploadFileSize": 0,
   "allowedUploadFileTypes": "",
   "properties": {
    "minRefreshPeriod": "30",
    "compatibilityMode": "GoogleEarth",
    "imageSize": "1024",
    "dpi": "96",
    "endPointURL": "",
    "featureLimit": "1000000",
    "useDefaultSnippets": "false"
   }
  },
  {
   "typeName": "WFSServer",
   "capabilities": "null",
   "enabled": "false",
   "maxUploadFileSize": 0,
   "allowedUploadFileTypes": "",
   "properties": {
    "phone": "",
    "appSchemaURI": "http://10.73.9.20:6080/arcgis/services/tjrc/RCRouteV3/MapServer/WFSServer",
    "providerSite": "",
    "administrativeArea": "",
    "electronicMailAddress": "",
    "pathToStoredQueryFile": "",
    "enableTransactions": "false",
    "city": "",
    "hourOfService": "",
    "title": "",
    "postalCode": "",
    "customGetCapabilities": "false",
    "name": "RCRouteV3",
    "deliveryPoint": "",
    "role": "",
    "axisOrderWFS10": "longlat",
    "axisOrderWFS11": "latlong",
    "serviceTypeVersion": "",
    "accessConstraints": "",
    "positionName": "",
    "abstract": "",
    "onlineResource": "http://10.73.9.20:6080/arcgis/services/tjrc/RCRouteV3/MapServer/WFSServer",
    "facsimile": "",
    "keyword": "",
    "defMaxFeaturesValue": "",
    "individualName": "",
    "fees": "",
    "serviceType": "",
    "enableDefMaxFeatures": "false",
    "country": "",
    "providerName": "",
    "transactionsWithoutLocks": "false",
    "pathToCustomGetCapabilitiesFiles": "",
    "appSchemaPrefix": "tjrc_RCRouteV3",
    "contactInstructions": ""
   }
  },
  {
   "typeName": "SchematicsServer",
   "capabilities": "Query",
   "enabled": "false",
   "maxUploadFileSize": 0,
   "allowedUploadFileTypes": "",
   "properties": {}
  },
  {
   "typeName": "FeatureServer",
   "capabilities": "Create,Query,Update,Delete,Uploads,Editing",
   "enabled": "false",
   "maxUploadFileSize": 0,
   "allowedUploadFileTypes": "",
   "properties": {
    "creatorPresent": "false",
    "dataInGdb": "true",
    "versionedData": "false",
    "xssPreventionEnabled": "true",
    "allowGeometryUpdates": "true",
    "syncVersionCreationRule": "versionPerDownloadedMap",
    "allowOthersToQuery": "true",
    "syncEnabled": "false",
    "editorTrackingTimeZoneID": "UTC",
    "enableZDefaults": "false",
    "realm": "",
    "allowOthersToDelete": "false",
    "allowTrueCurvesUpdates": "false",
    "datasetInspected": "true",
    "editorTrackingRespectsDayLightSavingTime": "false",
    "zDefaultValue": "0",
    "enableOwnershipBasedAccessControl": "false",
    "editorTrackingTimeInUTC": "true",
    "allowOthersToUpdate": "false"
   }
  },
  {
   "typeName": "WCSServer",
   "capabilities": "null",
   "enabled": "false",
   "maxUploadFileSize": 0,
   "allowedUploadFileTypes": "",
   "properties": {
    "phone": "",
    "maxImageHeight": "",
    "maxImageWidth": "",
    "city": "",
    "providerWebsite": "",
    "title": "tjrc_RCRouteV3",
    "customGetCapabilities": "false",
    "name": "RCRouteV3",
    "province": "",
    "role": "",
    "accessConstraints": "无",
    "abstract": "",
    "onlineResource": "http://10.73.9.20:6080/arcgis/services/tjrc/RCRouteV3/MapServer/WCSServer",
    "keywords": "",
    "fax": "",
    "zipcode": "",
    "fees": "",
    "country": "",
    "responsiblePerson": "",
    "providerName": "",
    "responsiblePosition": "",
    "email": "",
    "address": "",
    "pathToCustomGetCapabilitiesFiles": "",
    "serviceHour": "",
    "contactInstructions": ""
   }
  },
  {
   "typeName": "WMSServer",
   "capabilities": "null",
   "enabled": "false",
   "maxUploadFileSize": 0,
   "allowedUploadFileTypes": "",
   "properties": {
    "reaspect": "false",
    "inheritLayerNames": "false",
    "contactPosition": "",
    "contactVoiceTelephone": "",
    "city": "",
    "contactFacsimileTelephone": "",
    "title": "tjrc_RCRouteV3",
    "contactOrganization": "",
    "customGetCapabilities": "false",
    "name": "WMS",
    "stateOrProvince": "",
    "accessConstraints": "",
    "abstract": "",
    "onlineResource": "http://10.73.9.20:6080/arcgis/services/tjrc/RCRouteV3/MapServer/WMSServer",
    "keyword": "",
    "postCode": "",
    "fees": "",
    "addressType": "",
    "pathToCustomSLDFile": "",
    "country": "",
    "address": "",
    "contactElectronicMailAddress": "",
    "pathToCustomGetCapabilitiesFiles": "",
    "contactPerson": "",
    "listSupportedCRS": ""
   }
  }
 ],
 "datasets": []
}'''})

    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    # Connect to URL and post parameters

    httpConn = http.client.HTTPConnection(serviceAddress, servicePort)
    httpConn.request("POST", URL, params, headers)
    response = httpConn.getresponse()
    if (response.status != 200):
        httpConn.close()
        print(
            "Error while fetch tokens from admin URL. Please check the URL and try again.")
        return
    else:
        data = response.read()
        httpConn.close()

        # Extract the token from it
        res = json.loads(data)
        return res


def serviceStateSwitching(serviceName, serviceState, username="siteadmin", password="siteadmin",
                          serviceAddress="10.73.9.20", servicePort="6080"):
    token = getToken(username, password, serviceAddress, servicePort)['token']
    print("开始执行", serviceState, " 当前token: ", token)
    # URL = "/arcgis/admin/services/tjrc/Boundary.MapServer/"+serviceState
    URL = "/arcgis/admin/services/" + serviceName + "/" + serviceState

    # URL-encode the token parameters:-
    params = urllib.parse.urlencode(
        {"Token": token, 'f': 'json'})

    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    # Connect to URL and post parameters

    httpConn = http.client.HTTPConnection(serviceAddress, servicePort)
    httpConn.request("POST", URL, params, headers)
    response = httpConn.getresponse()
    if (response.status != 200):
        httpConn.close()
        print(
            "Error while fetch tokens from admin URL. Please check the URL and try again.")
        return
    else:
        data = response.read()
        httpConn.close()
        print(serviceState, "执行完毕")
        # Extract the token from it
        res = json.loads(data)
        return res


def run():
    starttime = datetime.datetime.now()
    states = serviceStateSwitching("tjrc/RCRouteV3.MapServer", "status")  # 执行前先检查服务状态
    if states['configuredState'] == 'STARTED' and states['configuredState'] == states['realTimeState']:
        stopState = serviceStateSwitching("tjrc/RCRouteV3.MapServer", "stop")
        if stopState['status'] == 'success':
            startState = serviceStateSwitching("tjrc/RCRouteV3.MapServer", "start")
            endtime = datetime.datetime.now()
            executionTime = (endtime - starttime).seconds
            startState["executionTime"] = str(executionTime)+"s"
            print("执行时间： ", executionTime, "s")
            return startState
        else:
            return {"status": "failed", "message": "请检查服务"}
    elif states['configuredState'] == 'STOPPED' and states['configuredState'] == states['realTimeState']:
        startState = serviceStateSwitching("tjrc/RCRouteV3.MapServer", "start")
        if startState['status'] == 'success':
            endtime = datetime.datetime.now()
            executionTime = (endtime - starttime).seconds
            startState["executionTime"] = str(executionTime)+"s"
            print("执行时间： ", executionTime, "s")
            return startState
        else:
            return {"status": "failed", "message": "请检查服务"}
    else:
        return {"status": "failed", "message": "当前服务正处于正在开启或正在关闭状态中，请稍后再试"}
# run()

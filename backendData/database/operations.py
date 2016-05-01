import datetime
from bson.objectid import ObjectId
import math

from backendData.common.constants import *
from backendData.objects.app import *


def putFacebookAppsData():
    databaseCollections.iMASappsCollection.insert(
            {
                "AppName": "People counting",
                "AppMethodName": "EdgeDetector",
                "AppImage": "images/appImages/app3/appImage.jpg",
                "AppSourceImage": "images/appImages/app3/background.jpg",
                "AppResultImage": "images/appImages/app3/appResultImage.jpg",
                "AppUsedCount": 0,
                "AppCreatedTime": datetime.datetime.utcnow(),
                "AppDescription": "The number of people in a specific area is counted..",
                "AppType": "userCreatable"
            }
    )
    print("Inserted iMAS data")


def rowCount(dbCollection):
    return dbCollection.count()


def NumberOfiMASApps():
    return rowCount(databaseCollections.iMASappsCollection)


def numberOfiMASAppPages():
    total = NumberOfiMASApps()
    return math.ceil(total / common.numOfAppsPerPage)


def getiMASAppDetailsById(Id):
    document = databaseCollections.iMASappsCollection.find_one({'_id': ObjectId(Id)})
    obj = App(appid=document["_id"],
              appname=document["AppName"],
              appmethodname=document["AppMethodName"],
              appimage=document["AppImage"],
              appresultimage=document["AppResultImage"],
              appsourceimage=document["AppSourceImage"],
              appusedcount=document["AppUsedCount"],
              appdescription=document["AppDescription"],
              apptype=document["AppType"])

    return obj


def getiMASAppsIDList():
    return databaseCollections.iMASappsCollection.distinct('_id')

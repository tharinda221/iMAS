from backendData.database.getConnection import *

class common:
    def __init__(self):
        pass

    ApplicationSecret = ""
    numOfAppsPerPage = 8
    appID = ""
    #baseUrl = "http://" + host + ":" + str(port)
    # baseUrl = "http://jsapps.co"

class databaseCollections:
    def __init__(self):
        pass

    iMASappsCollection = getDatabase().iMASappsCollection

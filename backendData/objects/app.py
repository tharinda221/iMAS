class App(object):
    def __init__(self, appid="",
                 appname="",
                 appmethodname="",
                 appimage="",
                 appsourceimage="",
                 appresultimage="",
                 appusedcount="",
                 appcreatedtimedate="",
                 appdescription="",
                 appmessage="",
                 apptype=""
                 ):
        self.AppType = apptype
        self.AppMessage = appmessage
        self.AppDescription = appdescription
        self.AppCreatedTimeDate = appcreatedtimedate
        self.AppUsedCount = appusedcount
        self.AppResultImage = appresultimage
        self.AppSourceImage = appsourceimage
        self.AppImage = appimage
        self.AppMethodName = appmethodname
        self.AppName = appname
        self.AppID = appid
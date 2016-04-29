from flask_restful import Resource
from flask import make_response, render_template
from backendData.frontendOperations.indexOperations import *
from backendData.database.operations import *

facebookAppCount = NumberOfiMASApps()
FacebookAppList = getiMASAppsIDList()

class main(Resource):
    def get(self):
        global noOfAppsPagesFacebook, facebookUserObj, facebookAppCount, FacebookAppList
        startId, endId = getStartIdAndEndId(1, facebookAppCount)
        list = getAppList(startId, endId, FacebookAppList)
        headers = {'Content-Type': 'text/html'}
        # return make_response(render_template('index.html'), 200, headers)
        return make_response(
                render_template('facebook/facebookAdminApp/facebookPage.html', authorized=False, id=000,
                                name="tharinda", noOfAppsPagesFacebook=noOfAppsPagesFacebook,
                                facebookPageNum=1, pageAppList=list),
                200, headers)

class runApplication(Resource):
    def get(self, appId):
        appDetails = getiMASAppDetailsById(appId)
        headers = {'Content-Type': 'text/html'}
        return make_response(
                render_template('facebook/facebookAdminApp/facebookAppDetailPage.html', authorized=False,
                                id=00,
                                name="tharinda", appDetails=appDetails),
                200, headers)

from backendData.common.constants import *
from backendData.database.operations import *

noOfAppsPagesFacebook = numberOfiMASAppPages() + 1

def getStartIdAndEndId(PageNum, appCount):
    startId = (appCount - 1) - ((PageNum - 1) * common.numOfAppsPerPage)
    if (startId - (common.numOfAppsPerPage - 1)) > 0:
        endId = startId - (common.numOfAppsPerPage - 1)
        return startId, endId
    else:
        endId = 0
        return startId, endId

def getAppList(startId, endId, appList):
    list = []
    count = endId
    for i in range(endId, startId + 1):
        list.append(getiMASAppDetailsById(appList[count]))
        count += 1
    return list
import sys, os
import abc
import requests
from bs4 import BeautifulSoup

class ApkDownloader(object):
    __metaclass__ = abc.ABCMeta

    def consoleLog(self, output):
        toLog = True
        if toLog:
            print(output.encode('utf-8').decode(sys.stdout.encoding))

    def makeDirs(self, fileName):
        if not os.path.exists(self.parentFolder):
            os.makedirs(self.parentFolder)

        if not os.path.exists(self.parentFolder + os.sep + fileName):
            os.makedirs(self.parentFolder + os.sep + fileName)


    def downloadFile(self, fileName, url):
        response = requests.get(url, stream=True)
        print(('downloading ' + fileName + ' from ' + url).encode('utf-8').decode(sys.stdout.encoding))
        chunkSize = 10240
        fileSize = int(response.headers['Content-Length'])
        downloaded = 0
        barLength = 50
        fileNameSpacesRemoved = '_'.join(fileName.split(' '))
        filePath = self.parentFolder + os.sep + fileNameSpacesRemoved + os.sep + fileNameSpacesRemoved + '.apk'
        self.makeDirs(fileNameSpacesRemoved)
        with open(filePath, 'wb') as f:
            for data in response.iter_content(chunk_size=chunkSize):
                downloaded += len(data)
                f.write(data)
                done = int(barLength * downloaded / fileSize)
                sys.stdout.write("\r[%s%s] %fMB of %dMB (%d percent) of \"%s\" done" % ('=' * done, ' ' * (barLength-done), (float(downloaded) / (1024 * 1024)), (fileSize / (1024 * 1024)), (100 * downloaded / fileSize), fileName.encode('utf-8').decode(sys.stdout.encoding)))
                sys.stdout.flush()
        print('\n')

    @abc.abstractmethod
    def downloadApk(self, appName, appCode):
        return

    @abc.abstractmethod
    def searchApk(self, appName):
        return

    def verifyCorrectness(self, firstAppInfo):
        if (firstAppInfo['searchAppName'].lower() in firstAppInfo['foundAppName'].lower() or firstAppInfo['foundAppName'].lower() in firstAppInfo['searchAppName'].lower()):
            return True
        else:
            return False

    def searchAndDownloadApk(self, searchAppName):
        firstAppInfo = self.searchApk(searchAppName)
        appVerified = False
        if firstAppInfo:
            appVerified = self.verifyCorrectness(firstAppInfo)
        if appVerified:
            self.downloadApk(firstAppInfo['foundAppName'], firstAppInfo['foundAppCode'])
            return firstAppInfo
        else: return None

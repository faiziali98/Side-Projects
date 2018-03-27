from ApkDownloader import *

class ApkMirrorApkDownloader(ApkDownloader):
    def printGap(self):
        print('============================================================================');
    
    def downloadApk(self, appName, appCode):
        self.parentFolder = 'APKMirror'
        url = 'http://www.apkmirror.com/wp-content/themes/APKMirror/download.php?id=' + appCode
        self.downloadFile(appName, url)

    def getInfoFromDownloadPage(self, searchAppName, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        foundAppCode = soup.find('article')
        foundAppName = soup.find('h1', {'class' : 'app-title'})
        foundAppVersion = soup.find('div', {'class' : 'appspec-value'})
        if foundAppName and foundAppCode and foundAppVersion:
            foundAppName = foundAppName.text
            foundAppCode = foundAppCode['id'].split('-')[1]
            foundAppVersion = foundAppVersion.text.split('arm')[0].split(': ')[1]
            self.consoleLog('found "' +  foundAppName + '"')
            return {'searchAppName' : searchAppName, 'foundAppName' : foundAppName, 'foundAppCode' : foundAppCode, 'foundAppVersion' : foundAppVersion}
        elif soup.find('div', {'class' : 'dowrap'}):
            url = 'http://www.apkmirror.com' + soup.find('div', {'class' : 'dowrap'}).find('a')['href']
            return self.getInfoFromDownloadPage(searchAppName, url)
        else:
            return None

    def searchApk(self, searchAppName):
        self.consoleLog('searching for app "' +  searchAppName + '"...')
        url = 'http://www.apkmirror.com/?s=' + searchAppName + '&post_type=app_release&searchtype=apk'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        appList = soup.find('div', { 'class' : 'listWidget' })
        firstAppInfo = appList.find('div', {'class' : 'appRow'})
        if firstAppInfo:
            return self.getInfoFromDownloadPage(searchAppName, 'http://www.apkmirror.com/' + firstAppInfo.find('div').find_all('div', {'class' : 'table-cell'})[1].find('a')['href'])
        else:
            self.consoleLog('could not find anything for "' +  searchAppName + '"')
            return None

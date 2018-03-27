from ApkDownloader import *

class AnzhiApkDownloader(ApkDownloader):
	def downloadApk(self, appName, appCode):
		self.parentFolder = 'AnzhiApps'
		url = 'http://www.anzhi.com/dl_app.php?s=' + appCode + '&n=5'
		self.downloadFile(appName, url)

	def searchApk(self, searchAppName):
		# print(('searching for app "' +  searchAppName + '"...').encode(sys.stdout.encoding, errors='replace'))
		url = 'http://www.anzhi.com/search.php?keyword=' + searchAppName
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser")
		appList = soup.find("div", { "class" : "app_list" })
		if appList:
			appInfo = appList.find('ul').find('li').find("div", {"class" : 'app_info'})

			appTop = appList.find("span", {"class" : "app_version"})
			foundAppVersion = ''.join([c for c in appTop.text][3:])

			foundAppName = appInfo.find("span", {"class" : "app_name"}).find('a')
			foundAppCode = foundAppName['href'].split('_')[1].split('.')[0]
			# print(('found "' +  foundAppName.text + '"').encode(sys.stdout.encoding, errors='replace'))
			return {'searchAppName' : searchAppName, 'foundAppName' : foundAppName.text, 'foundAppCode' : foundAppCode, 'foundAppVersion' : foundAppVersion}
		else:
			# print(str(('could not find anything for "' +  searchAppName + '"').encode(sys.stdout.encoding, errors='replace')) + '\n')
			return None
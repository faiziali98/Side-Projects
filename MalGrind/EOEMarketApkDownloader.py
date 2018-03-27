from ApkDownloader import *

class EOEMarketApkDownloader(ApkDownloader):
	def downloadApk(self, appName, appCode):
		self.parentFolder = 'EOEApps'
		url = 'http://www.eoemarket.com/download/' + appCode + '_0'
		self.downloadFile(appName, url)

	def searchApk(self, searchAppName):
		# print(('searching for app "' +  searchAppName + '"...').encode(sys.stdout.encoding, errors='replace'))
		url = 'http://www.eoemarket.com/search_.html?keyword=' + searchAppName + '&page=1'
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser")
		appList = soup.find("div", { "class" : "Rleft" })
		if appList:
			firstAppInfo = appList.find("div", {"class" : 'listProfile'}).find('ol').find_all('li')
			foundAppVersion = firstAppInfo[1].text
			foundAppName = firstAppInfo[0].text
			foundAppCode = firstAppInfo[0].find('span').find('a')['href'].split('/')[-1].split('.')[0]
			# print(('found "' +  foundAppName.text + '"').encode(sys.stdout.encoding, errors='replace'))
			return {'searchAppName' : searchAppName, 'foundAppName' : foundAppName, 'foundAppCode' : foundAppCode, 'foundAppVersion' : foundAppVersion}
		else:
			# print(str(('could not find anything for "' +  searchAppName + '"').encode(sys.stdout.encoding, errors='replace')) + '\n')
			return None
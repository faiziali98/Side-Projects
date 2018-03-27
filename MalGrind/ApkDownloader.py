import sys, os
import abc
import requests
from bs4 import BeautifulSoup

class ApkDownloader(object):
	__metaclass__ = abc.ABCMeta

	def makeDirs(self, fileName):
		if not os.path.exists(self.parentFolder):
			os.makedirs(self.parentFolder)
		
		if not os.path.exists(self.parentFolder + '/' + fileName):
			os.makedirs(self.parentFolder + '/' + fileName)
		

	def downloadFile(self, fileName, url):
		response = requests.get(url, stream=True)
		print(('downloading ' + fileName + ' from ' + url).encode("utf-8"))
		chunkSize = 10240
		fileSize = int(response.headers['Content-Length'])
		downloaded = 0
		barLength = 50
		fileNameSpacesRemoved = '_'.join(fileName.split(' '))
		self.makeDirs(fileNameSpacesRemoved)
		filePath = self.parentFolder + '/' + fileNameSpacesRemoved + '/' + fileNameSpacesRemoved + '.apk'
		with open(filePath, 'wb') as f:
			for data in response.iter_content(chunk_size=chunkSize):
				downloaded += len(data)
				f.write(data)
				done = int(barLength * downloaded / fileSize)
				sys.stdout.write("\r[%s%s] %fMB of %dMB (%d percent) of %s done" % ('=' * done, ' ' * (barLength-done), (float(downloaded) / (1024 * 1024)), (fileSize / (1024 * 1024)), (100 * downloaded / fileSize), (fileName).encode(sys.stdout.encoding, errors='replace')))    
				sys.stdout.flush()
		print('\n')

	@abc.abstractmethod
	def downloadApk(self, appName, appCode):
		return

	@abc.abstractmethod
	def searchApk(self, appName):
		return

	def searchAndDownloadApk(self, searchAppName):
		firstAppInfo = self.searchApk(searchAppName)
		if firstAppInfo:
			self.downloadApk(firstAppInfo['foundAppName'], firstAppInfo['foundAppCode'])
			return firstAppInfo['foundAppName']
		else: return None

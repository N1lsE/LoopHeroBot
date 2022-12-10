
import os
from datetime import datetime

class Logger:
	"""Singleton to manage Logging in Console and Loggfile"""
	__instance = None
	__pathToLogFile = "logs"
	__logFileName = 'latest.log'


	@staticmethod
	def getInstance():
		if Logger.__instance == None:
			Logger()
		return Logger.__instance
	
	def __init__(self):
		if Logger.__instance != None:
			raise Exception('Logger exists already!')
		Logger.__instance = self

		if not os.path.exists(Logger.__pathToLogFile):
			os.makedirs(Logger.__pathToLogFile)
		with open(Logger.__pathToLogFile + '\\' + Logger.__logFileName, 'w') as logFile:
			logFile.write('Creation of latest.log file\n')

	def Log(self, string:str):
		print(string)
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		with open(Logger.__pathToLogFile + '\\' + Logger.__logFileName, 'a') as logFile:
			logFile.writelines(f'[{current_time}] {string}' + '\n')

def test_Logger():
	print('start Logger test')
	logger1 = Logger.getInstance()
	logger2 = Logger.getInstance()
	print(f'logger1: {logger1}')
	print(f'logger2: {logger2}')
	logger1.Log('Test log.')
	logger2.Log('Second test log. First one worked')
	print('finished Logger test')


if __name__ == '__main__':
	test_Logger()
	exit()
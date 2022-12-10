import psutil

def CheckRunningGameExists():
	for p in psutil.process_iter():
		if  'loop hero' in str(p).lower():
			return
	print('No running game was found. [main.py CheckRunningGameExists()]')
	exit()

def RunBot():
	CheckRunningGameExists()
	print('Starting the bot.')

if __name__ == '__main__':
	RunBot()
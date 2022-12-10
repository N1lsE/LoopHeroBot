import psutil
import Utilitys

l = Utilitys.Logger.getInstance()

def CheckRunningGameExists():
	for p in psutil.process_iter():
		if  'loop hero' in str(p).lower():
			return
	l.Log('No running game was found. [main.py CheckRunningGameExists()]')
	exit()

def RunBot():
	CheckRunningGameExists()
	l.Log('Starting the bot.')

if __name__ == '__main__':

	RunBot()
try:
	import requests
except:
	raise Exception("Requests needed!\nSee https://pypi.python.org/pypi/requests/ or use pip install requests")
try:
	import selenium
except:
	raise Exception("selenium 47.0 needed!\n")

from spider import *
from cookies import *
from datacontrol import *
from lotterypack import *


print "Jingdong Tool Package Module Loaded!"
print "Author: HiddenStrawberry"

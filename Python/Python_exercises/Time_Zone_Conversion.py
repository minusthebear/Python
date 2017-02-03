from datetime import datetime
from pytz import timezone
fmt = "%Y-%m-%d %H:%M:%S %Z%z"
zones = {'Portland': 'US/Pacific', 'London': 'Europe/London', 'New York': 'US/Eastern', 'Seoul': 'Asia/Seoul'} 


def start():
	now_pdx = datetime.now(timezone(zones['Portland']))
	first = 'The time in Portland is ' + str(now_pdx.strftime(fmt))
	print(first)
	for key in zones:
		if (key != 'Portland'):
			x = now_pdx.astimezone(timezone(zones[key]))
			dry(x, key)

def dry(l,x):
	msg = 'The time in ' + x + ' is ' + str(l.strftime(fmt))
	print(msg)
	convertHour(l,x)

def convertHour(l,s):
	msg = ''
	hour = int(l.strftime('%H'))
	if (hour >= 9 and hour <= 21):
		msg = 'The company branch is currently open in ' + s
	else:
		msg = 'The company branch is closed at this hour in ' + s
	print(msg)


if __name__ == "__main__":
	start()
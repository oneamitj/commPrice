'''
from datetime import date
from dateutil.rrule import rrule, DAILY

a = date(2013, 6, 16)
b = date(2014, 11, 10)

for dt in rrule(DAILY, dtstart=a, until=b):
    dates = dt.strftime("%m/%d/%Y")
    f_name = str(dates).replace("/","-")
    print "wget --post-data 'cdate=%s&pricetype=W' http://kalimatimarket.com.np/priceinfo/dlypricebulletin -O %s_wholesale.html" % (str(dates), str(f_name))
'''


'''
# !/usr/bin/env python
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


dates = []

for fil in  os.listdir("wholesale"):
	# f_name= 'wholesale/'+fil
	# print os.stat(f_name)
	dates.append(fil.replace("_wholesale.html", '').replace("-","/"))
	# if (os.stat(f_name).st_size<1024):
	# 	pass
	if len(dates)==10:
		break

x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
y = range(len(x))

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x,y)
plt.gcf().autofmt_xdate()

plt.show()
'''
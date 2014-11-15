#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib.dates import YEARLY, DateFormatter, rrulewrapper, RRuleLocator, drange, date2num, MONTHLY, DAILY, SU, WeekdayLocator
import datetime
import os

for files in  os.listdir("comm_csvs"):
	i=0
	
	f_name="comm_csvs/"+files

	read_file = open(f_name, 'r')

	dates = []
	price = []

	i = 0
	for line in read_file:
		i+=1
		if i < 2:
			continue
		line = line.split('\t')

		date = line[0].split('/')
		date = date2num(datetime.date(int(date[2]), int(date[0]), int(date[1])))

		dates.append(date)

		price_int = int(line[1].replace("\n",''))
		
		price.append(price_int)

	print "class %s:" % files.replace(".csv", '').replace(" ", "_")
	print "\t" + "dates = ", dates
	print
	print "\t" + "price = ", price
	print
	print


'''
i=0
for files in  os.listdir("comm_csvs"):
	i+=1
	print "elif choice == %d:"%i
	print "\tmain(%s)" % files.replace(".csv","").replace(" ", "_")
	print
'''
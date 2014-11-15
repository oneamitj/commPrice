# !/usr/bin/env python
import os
import csv

def main():
	for files in  os.listdir("ra_csvs"):
		i=0
		
		f_name="ra_csvs/"+files
		
		read_file = open(f_name, 'r')

		for line in read_file:
			i+=1
			if i<4:
				continue
			line_arr = line.split('\t')
			# print line_arr

			f_save = open(line_arr[0]+'.csv','a')

			if (os.stat(line_arr[0]+'.csv').st_size<1):
				# f_save.write(line_arr[0])
				# f_save.write('\n'+line_arr[1])
				f_save.write("Date\tAverage")

			# date = files.replace('_wholesale.html.csv','').split('-')

			# date = date[2]+'-'+date[1]+'-'+date[0]

			f_save.write('\n'+files.replace('-','/').replace('_wholesale.html.csv','') + '\t' + line_arr[4])

			f_save.close()
		read_file.close()


main()
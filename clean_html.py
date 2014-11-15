#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import sys

page = sys.argv[1]
soup = BeautifulSoup(open(page))


rows = soup.findAll('tr')
for tr in rows[1:]:
	cols = tr.findAll('td')
	for td in cols:
	    text = td.find(text=True) + '\t'
	    print text,
	print

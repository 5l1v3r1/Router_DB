#!/usr/bin/env python 
# -*- coding:utf-8 -*-
try: 
	import re
	import requests
	from bs4 import BeautifulSoup 
	import sys
	import os
	import argparse
	from beautifultable import BeautifulTable
	import optparse

except Exception as err:
	print "[!] "+str(err)
	sys.exit(0)

LIGHTRED = '\033[91m'
YL = '\033[33m'
GR = '\033[32m'
BL = '\033[37m'
baseUrl = "http://www.routerpasswords.com"

def GetRouterPassword(routerName):
	r = requests.post(baseUrl, data = {'findpass':'1','router':routerName,'findpassword':'Find+Password'})
	soup = BeautifulSoup(r.text,"lxml")
	"""
	for option in soup.find_all('option'):
		print "list"
	"""
	# Parse table specification
	table = soup.find("table")
	headings = [th.get_text() for th in table.find("tr").find_all("th")]
	datasets = []
	mylist = []
	for row in table.find_all("tr")[1:]:
	    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
	    datasets.append(dataset)
	
	for dataset in datasets:
	    for field in dataset:
	    	mylist.append(field[1])
	# Group forms for the table rows
	tmp = []
	s = []
	i = 0
	for x in mylist:
		i +=1
		tmp.append(x)
		if i == 5:
			if len(mylist) > 5:
				tmp = []
				i = 0
				s.append(tmp)
			else:
				s.append(tmp)	
	# Draw the table rows and columns		
	table = BeautifulTable()
	table.column_headers = ["Manufacturer", "Model", "Protocol","Username","Password"]
	for y in xrange(0,len(s)):
		if len(s[y]) > 0:
			table.append_row(s[y])
	print table

def banner():                                                                     
	print LIGHTRED+' ▄▄▄·▄▄▄ . ▐ ▄ ▄▄▄▄▄▄▄▄ ..▄▄ · ▄▄▄▄▄ ▄▄·  ▄ .▄ ▄▄▄· ▪   ▐ ▄ .▄▄ ·  ▄▄▄· ▄▄▌ ▐ ▄▌'
	print'▐█ ▄█▀▄.▀·•█▌▐█•██  ▀▄.▀·▐█ ▀. •██  ▐█ ▌▪██▪▐█▐█ ▀█ ██ •█▌▐█▐█ ▀. ▐█ ▀█ ██· █▌▐█'
	print' ██▀·▐▀▀▪▄▐█▐▐▌ ▐█.▪▐▀▀▪▄▄▀▀▀█▄ ▐█.▪██ ▄▄██▀▐█▄█▀▀█ ▐█·▐█▐▐▌▄▀▀▀█▄▄█▀▀█ ██▪▐█▐▐▌'
	print'▐█▪·•▐█▄▄▌██▐█▌ ▐█▌·▐█▄▄▌▐█▄▪▐█ ▐█▌·▐███▌██▌▐▀▐█ ▪▐▌▐█▌██▐█▌▐█▄▪▐█▐█ ▪▐▌▐█▌██▐█▌'
	print'.▀    ▀▀▀ ▀▀ █▪ ▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀ ·▀▀▀ ▀▀▀ · ▀  ▀ ▀▀▀▀▀ █▪ ▀▀▀▀  ▀  ▀  ▀▀▀▀ ▀▪'
	print '==============================> https://github.com/ihebski/Pentest-chainsaw'+GR


def GetRouterList():
	r = requests.post(baseUrl, data = {'findpass':'1','router':"CISCO",'findpassword':'Find+Password'})
	soup = BeautifulSoup(r.text,"lxml")
	print BL+'============(=()=)==============='
	print '  =======(Routers List)=======  '
	print '============(=()=)==============='
	for option in soup.find_all('option'):
		print option["value"]

def start():
	banner()
	pars = optparse.OptionParser(description="[*] Get the Routers Default Passwords")
	pars.add_option('-r', '--router', type="string",dest="router", help="router name",default=None)
	pars.add_option("-l", "--list",action="store_true", dest="lists",help="List of the routers")
	opts, args = pars.parse_args()	
	if opts.lists:
		GetRouterList()
	if opts.router:
		GetRouterPassword(opts.router.upper())	

def main(inp):
	print inp

if __name__ == '__main__':
	try:
		start()
	except KeyboardInterrupt as err:
		print "\n[!] By... :)"
		sys.exit(0)


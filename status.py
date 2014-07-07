#!/usr/bin/env python

import sys
import mechanize
import re
import HTMLParser
from BeautifulSoup import BeautifulSoup

browser = mechanize.Browser()
h = HTMLParser.HTMLParser()

browser.set_handle_robots(False)

browser.open("https://m.facebook.com")
browser._factory.is_html = True
browser.select_form(nr=0)

browser.form['email'] = sys.argv[1]
browser.form['pass'] = sys.argv[2]
browser.submit()

x = 0

while x != 3:
	input = raw_input('''Please select an option:
	To update your status enter 1
	To view your friends' statuses enter 2
	To quit this script enter 3\n''')
	x = int(input)
	if x == 1:
		status = raw_input('Please enter the status you would like to post.\n')
		browser._factory.is_html = True
		browser.select_form(nr=1)
		browser.form['status'] = status
		browser.submit()
	elif x == 2:
		page = browser.open('https://m.facebook.com')
		soup = BeautifulSoup(page.read())
		list = soup.findAll('div', {'class': re.compile('^c[abu]') })
		for l in list:
			a = l.find('div', {'data-sigil':'mfeed_pivots_message feed-story-highlight-candidate'})
			if a:
				print h.unescape(l.find('a', text=True))
				print h.unescape(a.find('span', text=True))
				print '\n'
	elif x != 3:
		print 'invalid input'

#!/usr/bin/env python

import sys
import mechanize
from BeautifulSoup import BeautifulSoup

browser = mechanize.Browser()
browser.set_handle_robots(False)

browser.open("https://m.facebook.com")
browser._factory.is_html = True
browser.select_form(nr=0)

browser.form['email'] = sys.argv[1]
browser.form['pass'] = sys.argv[2]
browser.submit()

x = 0

while x != 3:
	input = raw_input("Please select an option:\n\tTo update your status enter 1\n\tTo view your friends' statuses enter 2\n\tTo quit this script enter 3\n")
	x = int(input)
	if x == 1:
		status = raw_input('Please enter the status you would like to post.')
		browser._factory.is_html = True
		browser.select_form(nr=1)
		browser.form['status'] = status
		browser.submit()
	elif x == 2:
		page = browser.open('https://m.facebook.com')
		soup = BeautifulSoup(page.read())
		list = soup.findAll('div', {'class':'ca cb cu'})
		for l in list:
			a = l.find('div', {'class':'cx', 'data-sigil':'mfeed_pivots_message feed-story-highlight-candidate'})
			if not a is None:
				print l.find('a', text=True)
				print a.find('span', text=True)
				print '\n'
	elif x != 3:
		print 'invalid input'

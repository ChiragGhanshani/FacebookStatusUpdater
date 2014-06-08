import sys
import mechanize

browser = mechanize.Browser()
browser.set_handle_robots(False)

browser.open("https://m.facebook.com")
browser._factory.is_html = True
browser.select_form(nr=0)

browser.form['email'] = sys.argv[1]
browser.form['pass'] = sys.argv[2]
browser.submit()

browser._factory.is_html = True
browser.select_form(nr=1)
browser.form['status'] = sys.argv[3]
browser.submit()

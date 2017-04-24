from bs4 import BeautifulSoup
import sqlite3
import urllib2
import re

import util

ROOT_URL = 'http://www.planecrashinfo.com'

def create_schema(conn):
	cursor = conn.cursor()
	cursor.execute('DROP TABLE IF EXISTS pci;')

	query = 'CREATE TABLE IF NOT EXISTS pci('

	for e in util.attrs:
		# Skip ignored util
		if e['label'] in util.ignore:
			continue
		query += e['label']+' '+e['sql_attr']
	query = query[:-1]+')'

	cursor.execute(query)
	print 'PCI schema regenerated'

def insert_accident(conn, accident):
	query = 'INSERT INTO pci VALUES (%s)' % ','.join(accident)
	print query
	conn.execute(query)
	conn.commit()
	print 'Row inserted'

# Returns an array of accident details
def get_accident_details(url):
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	rows = soup.table.find_all('tr')
	mdy = re.split('\ |,\ ', rows[1].find_all('td')[1].string)
	mdy[0] = util.to_numeric_month(mdy[0])
	rtn = [
		'"%s/%s/%s"' % (mdy[2], mdy[0], mdy[1]),    # date as YEAR/MONTH/DAY
		#rows[2].find_all('td')[1].string,  # hour, very unpredictable
		'"%s"' % rows[3].find_all('td')[1].string,  # location
		'"%s"' % rows[4].find_all('td')[1].string,  # operator
		'"%s"' % rows[5].find_all('td')[1].string,  # flight_no
		'"%s"' % rows[6].find_all('td')[1].string,  # route
		'"%s"' % rows[7].find_all('td')[1].string,  # ac_type
		'"%s"' % rows[8].find_all('td')[1].string,  # registration
		'"%s"' % rows[9].find_all('td')[1].string,  # construction or serial number / Line or fuselage number
		rows[10].find_all('td')[1].string.split(':')[1][0], # passengers aboard
		rows[10].find_all('td')[1].string.split(':')[2][0], # crew aboard
		rows[11].find_all('td')[1].string.split(':')[1][0], # passender fatalities
		rows[11].find_all('td')[1].string.split(':')[2][0], # crew fatalities
		rows[12].find_all('td')[1].string, # ground fatalities
		'"%s"' % (rows[13].find_all('td')[1].string).replace('"', '')  # summary
	]
	
	# Replace ? with NULLs
	for i in range(len(rtn)):
		rtn[i] = 'NULL' if rtn[i] in ['?', '"?"'] else rtn[i]

	return rtn
	
# Scrape a single year
def insert_year(conn, year):
	if year < 1920:
		print "Years before 1920 not available"
		return
	
	url = 'http://www.planecrashinfo.com/%s/%s.htm' % (year, year)
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	rows = soup.table.find_all('tr')[1:]
	for r in rows:
		href = r.find_all('a')[0]['href']
		accident_url = '%s/%s/%s' % (ROOT_URL, year, href)
		insert_accident(conn, get_accident_details(accident_url))

def insert_year_range(conn, start, end):
	for i in range(start, end+1):
		insert_year(conn, i)

def main():
	conn = sqlite3.connect('../test.db')
	create_schema(conn)

	url1 = ROOT_URL+'/2001/2001-42.htm'
	url2 = ROOT_URL+'/1922/1922-7.htm'
	insert_year_range(conn, 1920, 1925)
	
if __name__ == '__main__':
	main()
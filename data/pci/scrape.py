from bs4 import BeautifulSoup
import sqlite3
import urllib2
import re
import sys

import util

BASE_URL = 'http://www.planecrashinfo.com'

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

def save_accident_csv(accident, csv_file):
	# I really need to stop doing these
	line = ','.join(accident).replace('\'', '').replace('\n', '').replace('  ', '').replace('\t', '').encode('utf-8')
	csv_file.write(line+'\n')

# Scrape a single year
def save_year(year):
	if year < 1920:
		print "Years before 1920 not available"
		return
	
	url = '%s/%s/%s.htm' % (BASE_URL, year, year)
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	rows = soup.table.find_all('tr')[1:]

	if conn == 'CSV':
		csv_file = open('csv/%s.csv' % str(year), 'w')
		for r in rows:
			href = r.find_all('a')[0]['href']
			accident_url = '%s/%s/%s' % (BASE_URL, year, href)
			save_accident_csv(get_accident_details(accident_url), csv_file)
		csv_file.close()
		print "Saved year %s to CSV" % year
		return 

def save_year_range(start, end):
	for i in range(start, end+1):
		save_year(i)

def main():	
	start_year = int(sys.argv[1]) if len(sys.argv) > 1 else 1920
	end_year = int(sys.argv[2]) if len(sys.argv) > 2 else 1921
	save_year_range(start_year, end_year)
	
if __name__ == '__main__':
	main()
from bs4 import BeautifulSoup
import urllib2
import re

import attributes

ROOT_URL = 'http://www.planecrashinfo.com'

# TODO
'''def create_schema(conn, db_path):
	cursor = conn.cursor()
	cursor.execute('DROP TABLE IF EXISTS pci;')

	query = 'CREATE TABLE IF NOT EXISTS pci('

	for e in attributes.attrs:
		# Skip ignored attributes
		if e['label'] in attributes.ignore:
			continue
		query += e['label']+' '+e['sql_attr']
	query = query[:-1]+')'

	cursor.execute(query)'''

# Returns an array of incident details
def get_accident_details(url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.table.find_all('tr')
    rtn = [
        rows[1].find_all('td')[1].string, # date
        rows[2].find_all('td')[1].string, # hour
        rows[3].find_all('td')[1].string, # location
        rows[4].find_all('td')[1].string, # operator
        rows[5].find_all('td')[1].string, # flight_no
        rows[6].find_all('td')[1].string, # route
        rows[7].find_all('td')[1].string, # ac_type
        rows[8].find_all('td')[1].string,  # registration
        rows[9].find_all('td')[1].string,  # construction or serial number / Line or fuselage number
        rows[10].find_all('td')[1].string,  # passengers aboard
        rows[11].find_all('td')[1].string,  # fatalities
        rows[12].find_all('td')[1].string,  # ground fatalities
        rows[13].find_all('td')[1].string  # summary
    ]
    
    # Clean the data
    for i in range(len(rtn)):
        # Replace ? with None
        rtn[i] = None if rtn[i] == '?' else rtn[i]
        # TODO: Extract passenger and crew member count
        if i == 9:
            found = re.search('(?<=passengers:)', rtn[i])
            if not found:
                print 'ERROR scrapping passenger count'
                return
            print found
    
    return rtn
    
# Scrape a single year
def get_accident_urls(year):
    if year < 1920:
        return
    
    url = 'http://www.planecrashinfo.com/%s/%s.htm' % (year, year)
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.table.find_all('tr')[1:]
    for r in rows:
        href = r.find_all('a')[0]['href']
        accident_url = '%s/%s/%s' % (ROOT_URL, year, href)
        print get_accident_details(accident_url)

def main():
    url1 = ROOT_URL+'/2001/2001-42.htm'
    url2 = ROOT_URL+'/1922/1922-7.htm'
    #get_accident_urls(1922)
    get_accident_details(url2)
    
    
if __name__ == '__main__':
    main()
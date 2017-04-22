from bs4 import BeautifulSoup
import urllib2

def get_accident_details(url):
    print 'Fetching page'
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
        rows[8].find_all('td')[1].string  # registration
    ]
    
    print rtn

def main():
    url = 'http://www.planecrashinfo.com/2001/2001-42.htm'
    get_accident_details(url)
    
if __name__ == '__main__':
    main()
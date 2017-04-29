import os
import sqlite3

import util

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

def insert_csv_file(f, conn):
	query = 'INSERT INTO pci VALUES'
	while True:
		line = f.readline()[:-1]
		if line == '':
			break
		query += '(%s),' % line

	conn.execute(query[:-1])
	conn.commit()
	#print '%s inserted' % f.name

def main():
	conn = sqlite3.connect('../data.db')
	create_schema(conn)

	for dirpath, dirname, filenames in os.walk('./csv/'):
		for fn in filenames:
			if fn[-4:] != '.csv':
				print 'Skipping non-CSV file: %s' % fn
				continue
			f = open('csv/%s' % fn)
			insert_csv_file(f, conn)
			f.close()

	print 'PCI data inserted'
	conn.close()

if __name__ == '__main__':
	main()
import sqlite3
import util

def create_schema(conn):
	cursor = conn.cursor()
	cursor.execute('DROP TABLE IF EXISTS ntsb;')

	query = 'CREATE TABLE IF NOT EXISTS ntsb('

	for e in util.attrs:
		if e['label'] in util.ignore:
			continue
		query += e['label']+' '+e['sql_attr']
	query = query[:-1]+')'

	cursor.execute(query)
	print 'NTSB schema regenerated'

def insert_data(conn, file):
	cursor = conn.cursor()
	query = 'INSERT INTO ntsb VALUES '
	
	while True:
		line = file.readline()[:-1]
		if line == '':
			break

		line = line.replace('"', '').split(' | ')

		values = []

		# Modify each field value according to set rules
		for i in range(len(util.attrs)):
			entry = line[i]
			# Ignore some util
			if util.attrs[i]['label'] in util.ignore:
				continue
			# Deal wth NULLs
			if line[i] in util.null_values:
				values.append('NULL')
				continue
			# Insert quotes for varchars
			if util.attrs[i]['sql_attr'][:7] == 'varchar':
				entry = '"%s"' % line[i]
			# Insert date as YEAR/MONTH/DAY
			if util.attrs[i]['label'] == 'date':
				mdy = line[i].split('/')
				entry = '"%s/%s/%s"' % (mdy[2], mdy[0], mdy[1])
			values.append(entry)

		query += '('+','.join(values)+'),'

	cursor.execute(query[:-1])
	conn.commit()
	print "NTSB data inserted"

def main():
	file = open('cleaned.txt')
	conn = sqlite3.connect('../data.db')

	create_schema(conn)
	insert_data(conn, file)

	conn.close()

if __name__ == '__main__':
	main()

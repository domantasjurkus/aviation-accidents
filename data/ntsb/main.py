import sqlite3
import util
# aviation_data.txt extracted from the US National Transportation Safety Board:
# https://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx

def create_schema(conn):
	cursor = conn.cursor()
	cursor.execute('DROP TABLE IF EXISTS ntsb;')

	query = 'CREATE TABLE IF NOT EXISTS ntsb('

	for e in util.attrs:
		# Skip ignored util
		if e['label'] in util.ignore:
			continue
		query += e['label']+' '+e['sql_attr']
	query = query[:-1]+')'

	cursor.execute(query)

def insert_data(conn, file, truncate=False):
	cursor = conn.cursor()
	# Delete previous data if requested
	if truncate:
		print "Truncating table for new insertions"
		cursor.execute('DELETE FROM ntsb;')
		conn.commit()

	# Inserting all data with a single query
	query = 'INSERT INTO ntsb VALUES '
	line = 'hamster'
	
	while True:
		# Read line, drop newline, remove double-quotes
		line = file.readline()[:-1]
		if line == '':
			break

		line = line.replace('"', '').split(' | ')

		# Values for insertion
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
	print "Rows inserted"

# Parse the file and store the information in the project DB
def main():
	file = open('cleaned.txt')
	conn = sqlite3.connect('../test.db')

	create_schema(conn)
	insert_data(conn, file, True)

	conn.close()

if __name__ == '__main__':
	main()

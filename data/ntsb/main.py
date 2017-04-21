import sqlite3
import attributes
# aviation_data.txt extracted from the US National Transportation Safety Board:
# https://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx

def create_schema(conn, db_path):
	cursor = conn.cursor()
	cursor.execute('DROP TABLE IF EXISTS ntsb;')

	query = 'CREATE TABLE IF NOT EXISTS ntsb('

	for e in attributes.attrs:
		# Skip ignored attributes
		if e['label'] in attributes.ignore:
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
		for i in range(len(attributes.attrs)):
			entry = line[i]
			# Ignore some attributes
			if attributes.attrs[i]['label'] in attributes.ignore:
				continue
			# Deal wth NULLs
			if line[i] in attributes.null_values:
				values.append('NULL')
				continue
			# Insert quotes for varchars
			if attributes.attrs[i]['sql_attr'][:7] == 'varchar':
				entry = '"'+line[i]+'"'
			# Insert quotes for dates which are expressed as TEXT
			if attributes.attrs[i]['sql_attr'] == 'text,':
				entry = '"'+line[i]+'"'
			values.append(entry)

		query += '('+','.join(values)+')'
		query += ','

	cursor.execute(query[:-1])
	conn.commit()
	print "Rows inserted"

# Parse the file and store the information in the project DB
def main():
	file = open('cleaned.txt')

	conn = sqlite3.connect('../test.db')

	create_schema(conn, '../test.db')
	insert_data(conn, file, True)

	conn.close()

if __name__ == '__main__':
	main()

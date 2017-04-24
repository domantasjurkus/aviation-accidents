ignore = ['hour']

attrs = [
	{ 'label': 'date', 'sql_attr': 'text,' },
    { 'label': 'hour', 'sql_attr': 'int,' },
    { 'label': 'location', 'sql_attr': 'varchar(32),' },
    { 'label': 'operator', 'sql_attr': 'varchar(32),' },
    { 'label': 'flight_no', 'sql_attr': 'varchar(8),' },
    { 'label': 'route', 'sql_attr': 'varchar(32),' },
    { 'label': 'ac_type', 'sql_attr': 'varchar(32),' },
    { 'label': 'registration', 'sql_attr': 'varchar(16),' },
    { 'label': 'cn_ln', 'sql_attr': 'varchar(16),' },
    { 'label': 'passengers_aboard', 'sql_attr': 'int,' },
    { 'label': 'crew_aboard', 'sql_attr': 'int,' },
    { 'label': 'passenger_fatalities', 'sql_attr': 'int,' },
    { 'label': 'crew_fatalitites', 'sql_attr': 'int,' },
	{ 'label': 'ground_fatalities', 'sql_attr': 'int,' },
	{ 'label': 'summary', 'sql_attr': 'varchar(4096),' },
]

def to_numeric_month(label):
    if label.lower() == 'january': return '01'
    if label.lower() == 'february': return '02'
    if label.lower() == 'march': return '03'
    if label.lower() == 'april': return '04'
    if label.lower() == 'may': return '05'
    if label.lower() == 'june': return '06'
    if label.lower() == 'july': return '07'
    if label.lower() == 'august': return '08'
    if label.lower() == 'september': return '09'
    if label.lower() == 'october': return '10'
    if label.lower() == 'november': return '11'
    if label.lower() == 'december': return '12'
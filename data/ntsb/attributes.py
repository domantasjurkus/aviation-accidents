import collections

null_values = ['', 'N/A', 'NULL']

# Ignore some attributes since they will likely not be needed
ignore = ['amateur_built', 'air_carrier', 'far_description', 'schedule', 'publication_date']

# All attributes in the data file
attrs = [
    { 'label': 'event_id', 'sql_attr': 'varchar(16),' },
    { 'label': 'investigation_type', 'sql_attr': 'varchar(16),' },
    { 'label': 'accident_number', 'sql_attr': 'varchar(16),' },
    { 'label': 'event_date', 'sql_attr': 'text,' },
    { 'label': 'location', 'sql_attr': 'varchar(32),' },
    { 'label': 'country', 'sql_attr': 'varchar(32),' },
    { 'label': 'latitude', 'sql_attr': 'float(8),' },
    { 'label': 'longitude', 'sql_attr': 'float(8),' },
    { 'label': 'airport_code', 'sql_attr': 'varchar(8),' },
    { 'label': 'airport_name', 'sql_attr': 'varchar(64),' },
    { 'label': 'injury_severity', 'sql_attr': 'varchar(16),' },
    { 'label': 'aircraft_damage', 'sql_attr': 'varchar(16),' },
    { 'label': 'aircraft_category', 'sql_attr': 'varchar(16),' },
    { 'label': 'registration_number', 'sql_attr': 'varchar(16),' },
    { 'label': 'make', 'sql_attr': 'varchar(16),' },
    { 'label': 'model', 'sql_attr': 'varchar(16),' },
    { 'label': 'amateur_built', 'sql_attr': 'boolean,' },
    { 'label': 'number_of_engines', 'sql_attr': 'int(1),' },
    { 'label': 'engine_type', 'sql_attr': 'varchar(16),' },
    { 'label': 'far_description', 'sql_attr': 'varchar(32),' },
    { 'label': 'schedule', 'sql_attr': 'varchar(32),' },
    { 'label': 'purpose_of_flight', 'sql_attr': 'varchar(32),' },
    { 'label': 'air_carrier', 'sql_attr': 'varchar(32),' },
    { 'label': 'total_fatal_injuries', 'sql_attr': 'int(4),' },
    { 'label': 'total_serious_injuries', 'sql_attr': 'int(4),' },
    { 'label': 'total_minor_injuries', 'sql_attr': 'int(4),' },
    { 'label': 'total_uninjured', 'sql_attr': 'int(4),' },
    { 'label': 'weather_condition', 'sql_attr': 'varchar(16),' },
    { 'label': 'broad_phase_of_flight', 'sql_attr': 'varchar(16),' },
    { 'label': 'report_status', 'sql_attr': 'varchar(32),' },
    { 'label': 'publication_date', 'sql_attr': 'text,' }
]
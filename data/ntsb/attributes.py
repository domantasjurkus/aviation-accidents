import collections

null_values = ['', 'N/A', 'NULL']

# Ignore some attributes since they will likely not be needed
ignore = ['amateur_built', 'air_carrier', 'far_description', 'schedule', 'publication_date']

# All attributes in the data file
attrs = []
attrs.append({ 'label': 'event_id', 'sql_attr': 'varchar(16),' })
attrs.append({ 'label': 'investigation_type', 'sql_attr': 'varchar(16),' })
attrs.append({ 'label': 'accident_number', 'sql_attr': 'varchar(16),' })
attrs.append({ 'label': 'event_date', 'sql_attr': 'text,' })
attrs.append({ 'label': 'location', 'sql_attr': 'varchar(32),' })
attrs.append({ 'label': 'country', 'sql_attr': 'varchar(32),' })
attrs.append({ 'label': 'latitude', 'sql_attr': 'float(8),' })
attrs.append({ 'label': 'longitude', 'sql_attr': 'float(8),' })
attrs.append({ 'label': 'airport_code', 'sql_attr': 'varchar(8),' })
attrs.append({ 'label': 'airport_name', 'sql_attr': 'varchar(64),' })
attrs.append({ 'label': 'injury_severity', 'sql_attr': 'varchar(16),' })
attrs.append({ 'label': 'aircraft_damage', 'sql_attr': 'varchar(16),' })
attrs.append({ 'label': 'aircraft_category', 'sql_attr': 'varchar(16),' })
attrs.append({ 'label': 'registration_number', 'sql_attr': 'varchar(16),' })
attrs.append({ 'label': 'make', 'sql_attr': 'varchar(16),' })
attrs.append({ 'label': 'model', 'sql_attr': 'varchar(16),' })
attrs.append({ 'label': 'amateur_built', 'sql_attr': 'boolean,' })
attrs.append({ 'label': 'number_of_engines', 'sql_attr': 'int(1),' })
attrs.append({ 'label': 'engine_type', 'sql_attr': 'varchar(16),' })
attrs.append({ 'label': 'far_description', 'sql_attr': 'varchar(32),' })
attrs.append({ 'label': 'schedule', 'sql_attr': 'varchar(32),' })
attrs.append({ 'label': 'purpose_of_flight', 'sql_attr': 'varchar(32),' })
attrs.append({ 'label': 'air_carrier', 'sql_attr': 'varchar(32),' })
attrs.append({ 'label': 'total_fatal_injuries', 'sql_attr': 'int(4),' })
attrs.append({ 'label': 'total_serious_injuries', 'sql_attr': 'int(4),' })
attrs.append({ 'label': 'total_minor_injuries', 'sql_attr': 'int(4),' })
attrs.append({ 'label': 'total_uninjured', 'sql_attr': 'int(4),' })
attrs.append({ 'label': 'weather_condition', 'sql_attr': 'varchar(16),' })
attrs.append({ 'label': 'broad_phase_of_flight', 'sql_attr': 'varchar(16),' })
attrs.append({ 'label': 'report_status', 'sql_attr': 'varchar(32),' })
attrs.append({ 'label': 'publication_date', 'sql_attr': 'text,' })
The purpouse of this directory is to gather crash info from various sources, importing all data into a single database.

To create and populate `data.db` run `python main.py`.

### [US National Transportation Safety Board](https://www.ntsb.gov)
Data importable via `ntsb/import.py`.

### [Aviation Safety Network](https://aviation-safety.net/database/)
Sent an email for data access - waiting for reply.

### [Plane Crash Info](http://www.planecrashinfo.com/database.htm)
Website scrapped into CSV files in case future scrapping is needed and the site implements request blocking. Data importable via `pci/import.py`.

The purpouse of this directory is to gather crash data from various sources and to import it in a single database.

### [US National Transportation Safety Board](https://www.ntsb.gov)
Data parsed and stored in an SQLite database.

### [Aviation Safety Network](https://aviation-safety.net/database/)
Sent an email for data access - waiting for reply.

### [Plane Crash Info](http://www.planecrashinfo.com/database.htm)
Set up scrapping script.

`*` Years scrapped: [1908, 1925]
`*` Years remaining: [1926, 2017]

`TODO`:

- Check that repeating values are not inserted

- consider saving output to auxilary CSV file in case the site starts blocking requests while older entries need to be re-scrapped.
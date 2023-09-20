# postgresPusher


The repository provides a code snippet for uploading the csv files to a postgres database

For connecting the database we have used 'sqlalchemy' and 'psycopg2'

The files are handled using 'pandas'

In order to get the attributes for each CSV we have extracted the info from 'schemas.json' files in DATA directory

In order to establish the connection we have connection variables set up in '.env' file to provide the mandatory info such as:
* username    
* host
* port    
* database name
* password
* directory path (where CSV has been stored)



NOTE: Data set has been copied from https://github.com/dgadiraju/retail_db.git repository

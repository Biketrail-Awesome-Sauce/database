Our live website at www.mnbikeways.org runs on Ubuntu 14.04. After that I will give details
on setting things up.

###Install Postgres and Postgis and GDAL
* sudo apt-get update
* sudo apt-get install -y postgresql postgresql-contrib postgis postgresql-9.3-postgis-2.1 gdal-bin
    
###Install pgRouting
* sudo add-apt-repository ppa:georepublic/pgrouting-stable
* sudo apt-get update
* sudo apt-get install -y postgresql-9.3-pgrouting

###Create Postgres user and create database (keep this information for making config.py file)
######this will prompt you for a database password
* sudo -u postgres createuser -P USER_NAME_HERE
* sudo -u postgres createdb -O USER_NAME_HERE DATABASE_NAME_HERE

###A Database command that needs to be run
* sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION pgrouting;" DATABASE_NAME_HERE

###Some things that are needed but I'll leave it to you to determine if your system has it
* Java 7 or 8
* Python 2 or 3

###Getting Solr set up
* Get this: https://archive.apache.org/dist/lucene/solr/4.1.0/solr-4.1.0-src.tgz version of Solr and untar it
* Replace the schema.xml file in the solr-4.1.0/example/solr/collection1/conf with the schema.xml file at the root of this repo

###Make config.py file
- In the config.py file:
* dbName=YOUR_DATABASE_NAME
* dbUser=YOUR_USER
* dbPassword=YOUR_PASSWORD
* Place this file at root of project

###:sparkles:Get Python requirements
- When you installed python earlier you should have gotten Pip, the python package manager
* so pip install -r requirements.txt
* The requirements.txt file is in the root directory

###Load the database with data
* from the root of this project run:
* python manage.py migrate
* python manage.py loaddata whole_database.json
* It will take a while since it is a large database

###Create routable data
* using setup.sql file
* psql -f setup.sql -d YOUR_DATABASE_NAME

###Load Solr with data
* python manage.py rebuild_index

###Start up the Django Development Server
* python manage.py runserver


####And you're good to go. After the first time the only thing you should have to do is python manage.py runserver to turn it on.
    



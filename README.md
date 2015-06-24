# catalog_jewelry_app
udacity full stack nanodegree project 3 completed by Xiang Zhao Mirko
05/23/2015

GENERAL DESCRIPTION
-------------------
This is a project including sql schema in a virtual box instance using vagrant. This is a web app where registered users are able to create and modify jewelry collections. Not logged in users are also able to browse existing collections.

MODULES
-------------------
project.py: main python file which will create a Flask app and run it locally on localhost:5000

database_setup.py: includes database settings and schema, running this file will cerate a sqlite:///ecommerce.db 

db_helper.py: Database functions are stored in this file, it is then imported and used in project.py

lotsofitems.py: running this script will create some sample collections and users to populate the database

emptyDatabase.py: this is a helper script to delete all instances in the database without dropping it

client_secrets.json: you need to create your own google oauth credentials from https://console.developers.google.
com/ after registering and creating an app, go under credentials on the left column and click 'dowload JSON' 

fb_client_secrets.json: register your app at https://developers.facebook.com/ and obtain the app id and client secret to be replaced accordign to this json file format

static folder: includes all css files, fonts files, and media files necessary to recreate the web page
templates folder: includes all html template files used by flask to render teh different pages



python libraries and frameworks used: 
psycopg2==2.4.5
requests==2.7.0
httplib2==0.9.1
Flask-Login==0.2.11
Flask==0.10.1
gunicorn==19.3.0
Jinja2==2.7.3
oauth==1.0.1
oauth2client==1.4.11
SQLAlchemy==1.0.5
Werkzeug==0.10.4

INSTALLATION
-------------------
Install Git, Vagrant, and Virtual Box  
-Git: If you do not have a version of git installed, please visit http://git-scm.com/downloads  
-Vagrant: in order to install Vagrant, plese visit https://www.vagrantup.com/downloads  
-VirtualBox: in order to install Virtual Box, please visit https://www.virtualbox.org/wiki/Downloads  

CONFIGURATION
-------------------
-git clone https://github.com/xiangormirko/catalog_jewelry_app.git 
-using terminal navigate to the fouder in '/vagrant'  
-type 'vagrant up'  
-after the inizial setting up, type 'vagrant ssh' to log into the instance  
-navigate to 'cd /vagrant' to access the share files  

DATABASE & TABLES
-------------------
-After you are logged into vagrant navigate to the app folder and run the file database_setup.py to create the database 
-Run the file lotsofitems.py to populate with a few sample entries
-Run project.py to get the app up and running
-Navigate to localhost:5000 to check that everything is running correctly
-You may use emptyDatabase.py to erase records in the database 

JSON API ENDPOINTS
-------------------
# displays items in a collection by providing collection id
@app.route('/collection/<int:collection_id>/items/JSON')

# displays information on a specific item by providing both collection and item id
@app.route('/collection/<int:collection_id>/items/<int:item_id>/JSON')

# displays all collections
@app.route('/collection/JSON')

# displays all users
@app.route('/users/JSON')




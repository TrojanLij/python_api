from pg import DB
import random
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

db = DB(host=config['mysqlDB']['hostname'], user=config['mysqlDB']['username'], passwd=config['mysqlDB']['password'], dbname=config['mysqlDB']['database']) #connect to DB with given credentials and information

db.query("DROP TABLE users;")
print "Dropped"

db.query("CREATE TABLE users( id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, caller_id VARCHAR(20) NOT NULL);")  
print "Created"

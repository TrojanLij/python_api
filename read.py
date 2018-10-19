from pg import DB
import random

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

db = DB(host=config['mysqlDB']['hostname'], user=config['mysqlDB']['username'], passwd=config['mysqlDB']['password'], dbname=config['mysqlDB']['database']) #connect to DB with given credentials and information

def new_user_id():
    user_rand_gen_id = random.randint(100000000, 1000000000)
    return user_rand_gen_id


print(db.query("SELECT * FROM users"))

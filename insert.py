from pg import DB
import random

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

db = DB(host=config['mysqlDB']['hostname'], user=config['mysqlDB']['username'], passwd=config['mysqlDB']['password'], dbname=config['mysqlDB']['database']) #connect to DB with given credentials and information

loop = 21

def user_get_gen():
    name_user_rand_gen = "test" + str(random.randint(1, 999))
    return name_user_rand_gen

def new_user_id():
    user_rand_gen_id = random.randint(100000000, 1000000000)
    return user_rand_gen_id

while loop > 1:
    user_gen_name = str(user_get_gen())
    user_gen_id = str(new_user_id())

    db.query("INSERT INTO users (name, caller_id) VALUES ('" + user_gen_name + "', '" + user_gen_id + "');")
    loop = loop - 1
    

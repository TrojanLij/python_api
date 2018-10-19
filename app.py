from flask import Flask, jsonify, abort, make_response, json, request
import requests

from pg import DB

#flask ip and port for development env, reset to 127.0.0.1 for ip and 5000 for port if using local hosting only

flask_ip = '192.168.36.189' #string with ip
flask_port = 80 #intiger with port

app = Flask(__name__)

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

#connect to DB with given credentials and information
db = DB(host=config['mysqlDB']['hostname'], user=config['mysqlDB']['username'], passwd=config['mysqlDB']['password'], dbname=config['mysqlDB']['database']) 


#get id (INT) from database of specific user and print as JSON file. GET METHOD!
@app.route('/api/db/<int:id_of_user>', methods=['GET'])
def get_db_id(id_of_user):
    
    #query that gets specific information from DB corresponding with given information
    q = db.query("SELECT * FROM users WHERE (id = '" + str(id_of_user) + "');")
    q.getresult()

    for row in q.getresult():
        
        #prep string and concatenate string with info
        ugly_json = '{"id":' + str(row[0]) + ',"name":"' + str(row[1]) + '","caller_id":"' + str(row[2]) + '"}'

        #parse the ugly JSON string
        parsed = json.loads(ugly_json)
        return make_response(jsonify(parsed), 200)


#get id (STRING) from database of specific user and print as JSON file. GET METHOD!
@app.route('/api/db/<string:name_of_user>', methods=['GET'])
def get_db_name(name_of_user):

    #query that gets specific information from DB corresponding with given information
    q = db.query("SELECT * FROM users WHERE (name LIKE '" + name_of_user + "');")
    q.getresult()

    for row in q.getresult():
        #prep string and concatenate string with info
        ugly_json = '{"id":' + str(row[0]) + ',"name":"' + str(row[1]) + '","caller_id":"' + str(row[2]) + '"}'

        #parse the ugly JSON string
        parsed = json.loads(ugly_json)
        return make_response(jsonify(parsed), 200)

@app.route('/api/db', methods=['POST'])
def create_user():
    req_data = request.get_json()

    user_name = req_data['name']
    caller_id = req_data['caller_id']

    q = db.query("INSERT INTO users (name, caller_id) VALUES ('" + user_name + "', '" + caller_id + "');")
    q.getresult()
    return make_response(jsonify({'success': 'uploaded'}), 200)

#outputed error but works as intended
#    return q.getresult()
#AttributeError: 'str' object has no attribute 'getresult'

#Error handler for if something is not found

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


app.run(host=flask_ip, port=flask_port, debug=True)

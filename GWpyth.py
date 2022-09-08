from flask import Flask
from flask_restful import Resource, Api, reqparse
import growattServer
import os
import ast

USER = os.getenv('API_USER')
PASSWORD = os.getenv('API_PASSWORD')
FAILED_LOGIN_COUNT = 0
gwapi = growattServer.GrowattApi()

app = Flask(__name__)
api = Api(app)

#app.config["DEBUG"]=True

class Reading(Resource):
    def get(self):
        try:
            plant_info = gwapi.plant_info(plant_id)
        except Exception:
            global FAILED_LOGIN_COUNT
            FAILED_LOGIN_COUNT += 1
            GWLogin()
        else:
            return{'plant_info': plant_info},200

api.add_resource(Reading, '/reading') # '/reading' is the entry point
@app.route('/', methods=['GET'])
def home():
    return "<h1>Growatt Server REST</h1><p>This site is a prototype API for reading growatt server data.</p><p>Read URL is <host>/reading"

def GWLogin():
    return gwapi.login(USER, PASSWORD)

login_response = gwapi.login(USER, PASSWORD)
plantlist = gwapi.plant_list(login_response['user']['id'])
plant = plantlist['data'][0]
plant_id = plant['plantId']

if __name__ == '__main__':
    app.run(host='0.0.0.0')

import time
import os
import string
import secrets
from flask import (Flask, 
    request, abort, jsonify, Response,render_template)
from flask_cors import CORS
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
from random import shuffle
import json
from sqlalchemy import Column, String, Integer, Float, Boolean

from models import (AnyData,db)



class config_test:
    SECRET_KEY=secrets.token_urlsafe(5000)
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
    #    os.path.join(os.path.dirname(os.path.abspath(__file__)), "db/test.sqlite"))
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SQLALCHEMY_DATABASE_URI="sqlite:////db/test.sqlite"
    #SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
    #    os.path.join(os.path.dirname(os.path.abspath(__file__)), "db\\test.sqlite"))
    print(SQLALCHEMY_DATABASE_URI)





app = Flask(__name__)
app.config.from_object(config_test)
db.app = app
db.init_app(app)


try:
    db.create_all()
except Exception as e:
    raise(e)



try:
    if len(AnyData.query.all())==0:
        data= AnyData()
        data.insert()
except:
    pass

@app.route('/')
def hello():
    try:
        data= AnyData.query.order_by(AnyData.id).first()
        data.number = data.number+1
        data.update()
        data_from_db = data.number
    except e:
        print(str(e),flush=True)

    to_return ="A variable from the database: "
    try:
        to_return += str(data_from_db)
    except e:
        to_return += "Error: Can't read the database variable"
        print(str(e),flush=True)

    to_return += "<br>"
    to_return += "An environmental variable called SECRET: "
    try:
        to_return += str(os.environ["SECRET"])
    except:
        to_return += "Error: Can't read the environmental variable"
    return to_return

if __name__ == '__main__':
    app.run(host="127.0.0.1",debug=False,port=5000)
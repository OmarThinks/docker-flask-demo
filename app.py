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

"""for env_var in os.environ:
    print(env_var,flush=True)
    try:
        print(str(os.environ[env_var]),flush=True)
    except:
        pass
    print("_________")
"""




class config_test:
    #SECRET_KEY=os.urandom(32)
    SECRET_KEY=secrets.token_urlsafe(5000)
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
    #    os.path.join(os.path.dirname(os.path.abspath(__file__)), "db/test.sqlite"))
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    #SQLALCHEMY_DATABASE_URI="sqlite:////db\\test.sqlite"
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "db\\test.sqlite"))
    print(SQLALCHEMY_DATABASE_URI)





app = Flask(__name__)
app.config.from_object(config_test)
#print(app.config['SECRET_KEY'],flush=True)
db.app = app
db.init_app(app)


try:
    db.create_all()
except Exception as e:
    raise(e)



@app.route('/')
def hello():
    to_return ="A variable from the database: "
    try:
        to_return += str(len(AnyData.query.all()))
    except:
        to_return += "Error: Can't read the database variable"
    to_return += "<br>"
    to_return += "An environmental variable called SECRET: "
    try:
        to_return += os.environ["SECRET"]
    except:
        to_return += "Error: Can't read the environmental variable"
    return to_return

if __name__ == '__main__':
    app.run(host="127.0.0.1",debug=False,port=5000)
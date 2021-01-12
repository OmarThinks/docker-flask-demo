import os
from sqlalchemy import Column, String, Integer, Float, Boolean
from flask_sqlalchemy import SQLAlchemy
import json


db=SQLAlchemy()



class AnyData(db.Model):

    id = Column(Integer(), primary_key=True)
    number = Column(Integer(), primary_key=False)

    def __init__(self):
        self.number = 1

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()





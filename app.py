from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash

# from sqlalchemy import create_engine, asc, desc, \
#     func, distinct
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.serializer import loads, dumps

# from database_setup import Base, Things

import random
import string
import logging
import json
import os
import requests
import database
app = Flask(__name__, static_url_path='')
app._static_folder = os.path.abspath("")

# Connect to database and create database session
# engine = create_engine('sqlite:///flaskstarter.db')
# Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
# session = DBSession()


# Display all things

@app.route('/', methods = ['GET', 'POST'])
def start() :
    return main()
@app.route('/main', methods = ['GET', 'POST'])
def main():
    db = database.Database()
    temperature = db.getTemperatures()
    waterquality = db.getQualities()
    waterlevel = db.getLevels()
    hour = waterLevelHour(waterlevel)
    return render_template('main.html', temperature=temperature,waterlevel=waterlevel, waterquality=waterquality, hour=hour)

def waterLevelHour(waterlevel) :
    return int(waterlevel[0]['level']) - int(waterlevel[1]['level'])
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

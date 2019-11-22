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
import unittest


class TestSum(unittest.TestCase):

    def test_temperature(self, temp):
        self.assertEqual(temp, '22', "Should be 21 as it is the first entry in DB")

if __name__ == '__main__':
    unittest.main()

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
    test = 1
    #test = TestSum().test_temperature(db.getTemperatures()[0]['temperature']);
    hour = waterLevelHour()
    return render_template('main.html', temperature=temperature,waterlevel=waterlevel, waterquality=waterquality, hour=hour, test=test)

def waterLevelHour() :
    totalwater = 0
    db = database.Database()
    waterlevels = db.getAllLevels()
    for index, water in enumerate(waterlevels) :
        if index == 0 :
            continue
        delta = int(water['level']) - int(waterlevels[index-1]['level'])
        if delta > 5 :
            totalwater = totalwater + delta
    return int(totalwater)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

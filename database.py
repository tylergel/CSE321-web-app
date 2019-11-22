from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash

# from sqlalchemy import create_engine, asc, desc, \
#     func, distinct
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.serializer import loads, dumps

# from database_setup import Base, Things
import requests
import random
import string
import json
import pymysql
import os

class Database:
    def __init__(self):
        host = os.environ.get('host')
        user = os.environ.get('user')
        password=os.environ.get('password')
        db=os.environ.get('db')
        # host = "107.180.27.226"
        # user = "tylergel"
        # password = "tylergel"
        # db = "water-filter-app"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
    def getTemperatures(self) :
        self.cur.execute("SELECT * FROM temperature order by id DESC LIMIT 25")
        result = self.cur.fetchall()
        return result
    def getQualities(self):
        self.cur.execute("SELECT * FROM quality order by id DESC LIMIT 25")
        result = self.cur.fetchall()
        return result
    def getLevels(self):
        self.cur.execute("SELECT * FROM level order by id DESC  LIMIT 25")
        result = self.cur.fetchall()
        return result
    def getAllLevels(self):
        self.cur.execute("SELECT * FROM level order by id DESC  LIMIT 720")
        result = self.cur.fetchall()
        return result

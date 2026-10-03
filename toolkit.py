import mysql.connector
from datetime import datetime
from sqlalchemy import create_engine
def mysqlconnector():

 connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="DozieMySQL2026!",
    database="world"
 )
 return connection

def createsqlengine():
 engine = create_engine(
    "mysql+mysqlconnector://root:DozieMySQL2026!@localhost:3306/world")

 return engine



#!/usr/bin/env python3
import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.58",
  user="root",
  passwd=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE glpi")
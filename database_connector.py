import mysql.connector
from decouple import config


mydb = mysql.connector.connect(
    host = config('HOST'),
    user= config('USERNAME'),
    password = config('PASSWORD'),
    database = config('DATABASE')
)
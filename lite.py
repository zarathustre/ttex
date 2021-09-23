import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    cnx = None

    try:
        cnx = sqlite3.connect(db_file)
        return cnx
    except Error as e:
        print(e)

    return cnx


def execute_query(cnx, query):
    try:
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
    except Error as e:
        print(e)


def execute_query_var(cnx, query, var):
    try:
        cursor = cnx.cursor()
        cursor.execute(query, var)
        cnx.commit()
    except Error as e:
        print(e)


def fetch_query(cnx, query):
    data = None

    try:
        cursor = cnx.cursor()
        data = cursor.execute(query).fetchall()
        return data
    except Error as e:
        print(e)

    return data


def fetch_query_var(cnx, query, var):
    data = None

    try:
        cursor = cnx.cursor()
        data = cursor.execute(query, var).fetchall()
        return data
    except Error as e:
        print(e)

    return data
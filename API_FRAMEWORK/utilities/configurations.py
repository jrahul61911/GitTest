import configparser
import mysql.connector
from mysql.connector import Error

def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


connector_config = {

    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password'],
    'database': getConfig()['SQL']['database'],
    'host': getConfig()['SQL']['host']

}


def getConnection():
    try:
      conn = mysql.connector.connect(**connector_config)
      if conn.is_connected():
        print("It's succesful")
        return conn
    except Error as e:
        print(e)


def getQuery(query):

    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row





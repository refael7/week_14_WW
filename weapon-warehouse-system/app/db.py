import mysql.connector
from mysql.connector.connection import MySQLConnectionAbstract
import os


def connection():
    conn = mysql.connector.connect(
    host=os.getenv("MYSQL_ROOT_HOST") ,
    user=os.getenv("MYSQL_ROOT_USER"),
    password=os.getenv("MYSQL_ROOT_PASSWORD"),
    database=os.getenv("MYSQL_ROOT_DB"))
    return conn




def create_table():
    conn = connection()
    return conn.cursor().execute("""
    CREATE TABLE IF NOT EXIST weapons_list (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    weapon_id VARCHAR(250), 
                    weapon_name VARCHAR(250),
                    weapon_type VARCHAR(250), 
                    range_km INT,
                    weight_kg FLOAT,
                    manufacturer VARCHAR(250), 
                    origin_country VARCHAR(250), 
                    storage_location VARCHAR(250) ,
                    year_estimated INT, 
                    level_risk VARCHAR(250))""")


def insert_weapons_list():
    conn = connection()
    cursor = conn.cursor()
    insert_table = """
        INSERT INTO weapons_list (
        weapon_id,
        weapon_name,
        weapon_type,
        range_km,
        weight_kg,
        manufacturer,
        origin_country,
        storage_location,
        year_estimated,
        risk_level ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """


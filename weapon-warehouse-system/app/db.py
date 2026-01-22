import mysql.connector
from mysql.connector.connection import MySQLConnectionAbstract



def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="weather_db"
    )
    return conn




def create_table(mydb:MySQLConnectionAbstract):
    my_cursor = mydb.cursor()
    my_cursor.execute("""
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

def insert_weapons_list(conn, data: dict):
    query = """
    INSERT INTO weather_records (
        weapon_id , 
        weapon_name ,
        weapon_type , 
        range_km ,
        weight_kg ,
        manufacturer , 
        origin_country , 
        storage_location  ,
        year_estimated , 
        level_risk 
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data["weapon_id"],
        data["weapon_name"],
        data["weapon_type"],
        data["range_km"],
        data["weight_kg"],
        data["manufacturer"],
        data["origin_country"],
        data["storage_location"],
        data["year_estimated"],
        data["level_risk"]

    )
    cursor = conn.cursor()
    cursor.execute(query, values)
# Add whatever it is needed to interface with the DB Table corso
from database import DB_connect
from database.DB_connect import get_connection, DBConnect
from model import corso
from model.corso import Corso

def get_corsi():
    cnx = DB_connect.get_connection()
    result = []
    if cnx is None:
        print("Connessione fallita")
    else:
        cursor = cnx.cursor(dictionary=True)
        query = """select c.nome 
                   from corso c"""
        cursor.execute(query)

        for row in cursor:
            result.append(
                Corso(row["codins"],
                      row["crediti"],
                      row["nome"],
                      row["pd"]
                      ))

        cursor.close()
        cnx.close()

    return result

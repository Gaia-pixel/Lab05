# Add whatever it is needed to interface with the DB Table corso
from database import DB_connect
from database.DB_connect import get_connection, DBConnect
from model import corso
from model.corso import Corso
from model.studente import Studente


def get_corsi():
    cnx = DB_connect.get_connection()
    result = []
    if cnx is None:
        print("Connessione fallita")
    else:
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT c.codins, c.crediti, c.nome, c.pd
                FROM corso c"""
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

def getIscrittiCorso(corso):
    cnx = DB_connect.get_connection()
    result = []
    if cnx is None:
        print("Connessione fallita")
    else:
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT s.matricola, s.nome, s.cognome, s.CDS
                    FROM studente s, iscrizione i
                    WHERE s.matricola = i.matricola and i.codins = %s"""
        cursor.execute(query, (corso,))

        for row in cursor:
            result.append(
                Studente(row["matricola"],
                      row["nome"],
                      row["cognome"],
                      row["CDS"]
                      ))

        cursor.close()
        cnx.close()

    return result

def getStudenteMatricola2(matricola):
    cnx = DB_connect.get_connection()
    result = []
    if cnx is None:
        print("Connessione fallita")
    else:
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT s.*
FROM iscritticorsi.studente s
WHERE s.matricola  = %s"""
        cursor.execute(query, (matricola,))

        for row in cursor:
            result.append(
                Studente(row["matricola"],
                      row["nome"],
                      row["cognome"],
                      row["CDS"]
                      ))

        cursor.close()
        cnx.close()

    return result

def getStudenteMatricola(matricola) -> Studente | None:
    """
        Funzione che data una matricola ricerca nel database lo studente corrispondente (se presente)
        :param matricola: la matricola dello studente da ricercare
        :return: uno studente, se presente
        """
    cnx = get_connection()
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM studente WHERE matricola = %s", (matricola,))
        row = cursor.fetchone()
        if row is not None:
            result = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
        else:
            result = None
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None


def getcorsiStudente(matricola):
    cnx = DB_connect.get_connection()
    result = []
    if cnx is None:
        print("Connessione fallita")
    else:
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT c.* FROM iscritticorsi.iscrizione i, iscritticorsi.corso c WHERE i.codins = c.codins and matricola = %s"""
        cursor.execute(query, (matricola,))

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
from database import corso_DAO


class Model:
    def __init__(self):
        pass

    def get_corsi(self):
        return corso_DAO.get_corsi()

    def get_iscrittiCorso(self, corso):
        return corso_DAO.getIscrittiCorso(corso)

    def get_studenteMatricola(self, matricola):
        return corso_DAO.getStudenteMatricola(matricola)

    def get_corsiStudente(self, matricola):
        return corso_DAO.getcorsiStudente(matricola)
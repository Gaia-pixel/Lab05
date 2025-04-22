from database import corso_DAO


class Model:
    def __init__(self):
        pass


    def get_corsi(self):
        return corso_DAO.get_corsi()
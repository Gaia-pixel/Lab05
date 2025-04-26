
class Corso:
    codins: str = ""
    crediti: int = 0
    nome: str = ""
    pd: int = 0

    def __init__(self, codins: str, crediti: int, nome: str, pd: int):
        self.codins = codins
        self.crediti = crediti
        self.nome = nome
        self.pd = pd


    def __str__(self):
        return f"{self.nome} ({self.codins})"

    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)
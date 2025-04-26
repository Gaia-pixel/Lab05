class Studente:
    matricola: int
    nome: str
    cognome: str
    CDS: str

    def __init__(self, matricola: int, nome: str, cognome: str, CDS: str):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.CDS = CDS

    def __str__(self):
        return f"{self.nome} {self.cognome} ({self.matricola})"

    def __hash__(self):
        return hash(self.matricola)





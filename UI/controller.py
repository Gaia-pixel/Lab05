import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._idmap_corsi = {}
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.corso_selezionato = None

    def handle_cercaIscritti(self, e):
        if self.corso_selezionato is None:
            self._view.create_alert("selezionare un corso!")
            return
        iscritti = self._model.get_iscrittiCorso(self.corso_selezionato)
        if iscritti is None:
            self._view.create_alert("Problema nella connessione al database!")
            return
        else:
            self._view.txt_result.controls.append(ft.Text(f"ci sono {len(iscritti)} iscritti a questo corso"))
            for studente in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{studente}"))

        self._view.update_page()

        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()


    def handle_cercaStudente(self, e):
        self.matricola = self._view.txt_matricola.value
        if self.matricola == "":
            self._view.create_alert("matricola non esistente!")
            return

        studente = self._model.get_studenteMatricola(self.matricola)
        if studente is None:
            self._view.create_alert("Problema nella connessione al database!")
            return
        else:
           self._view.txt_nome.value = f"{studente.nome}"
           self._view.txt_cognome.value = f"{studente.cognome}"

        self._view.update_page()


    def handle_cercaCorsi(self, e):
        self.matricola = self._view.txt_matricola.value
        if self.matricola == "":
            self._view.create_alert("matricola non esistente!")
            return

        corsi = self._model.get_corsiStudente(self.matricola)
        if corsi is None:
            self._view.create_alert("Problema nella connessione al database!")
            return
        else:
            self._view.txt_result.controls.append(ft.Text(f"I corsi che segue lo studente con matricola {self.matricola} sono {len(corsi)}:"))
            for c in corsi:
                self._view.txt_result.controls.append(ft.Text(f"{c}"))

        self._view.update_page()


    def leggi_corso(self, e):
        self.corso_selezionato = self._view.dd_corso.value

    def populate_dd_corso(self):
        for corso in self._model.get_corsi():
            self._idmap_corsi[corso.codins] = corso
            self._view.dd_corso.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
        self._view.update_page()
import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._idmap_corsi = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.corso_selezionato = None

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()


    def leggi_corso(self, e):
        self.corso_selezionato = self._view.dd_corso.value

    def populate_dd_corso(self):
        
        for corso in self._model.get_corsi():
            self._idmap_corsi[corso.codins] = corso
            self._view.dd_corso.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
        self._view.update_page()
import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dd_musei(self):
        musei= self._model.get_musei()
        if musei is not None:
            opzioni_museo = []
            for museo in musei:
                opzioni_museo.append(ft.dropdown.Option(key = museo.id, text = museo.nome))
            self._view.seleziona_museo.options = opzioni_museo
            self._view.seleziona_museo.on_change = self.museo_selezionato_change

    def popola_dd_epoca(self):
        epoche = self._model.get_epoche()
        epoche_uniche = sorted(list(set(epoche)))
        opzioni_epoca = []
        for epoca in epoche_uniche:
            opzioni_epoca.append(ft.dropdown.Option(key = epoca, text = epoca))
        self._view.seleziona_epoca.options = opzioni_epoca
        self._view.seleziona_epoca.on_change = self.epoca_selezionata_change

        self._view.page.update()

    # CALLBACKS DROPDOWN
    # TODO
    def museo_selezionato_change(self, e):

        self.museo_selezionato = e.control.value #valore id selezionato
        print(f"Museo selezionato: {self.museo_selezionato}")


    def epoca_selezionata_change(self, e):

        self.epoca_selezionata = e.control.value #valore epoca selezionata
        print(f"Epoca selezionata: {self.epoca_selezionata}")

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti_filtrati(self):
        self._view.clear_output()
        museo_key = self.museo_selezionato
        epoca_key = self.epoca_selezionata


        #chiedo al Model la lista di oggetti Artefatto filtrati
        lista_artefatti = self._model.get_artefatti_filtrati(
            museo=museo_key,
            epoca=epoca_key
        )

        if lista_artefatti is None:
            self._view.append_output("Errore: Impossibile recuperare i dati dal database.", bold=True)
            self._view.page.update()
            return


        if len(lista_artefatti) == 0:
            self._view.append_output("Nessun artefatto trovato con i filtri selezionati.", bold=True)
            self._view.page.update()
            return

        for artefatto in lista_artefatti:
            visualizza_artefatto = f"ID: {artefatto.id} | Nome: {artefatto.nome} | Epoca: {artefatto.epoca} | ID museo: {artefatto.id_museo}"
            self._view.append_output(visualizza_artefatto)

        self._view.page.update()
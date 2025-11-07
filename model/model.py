from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        artefatti_totali = self._artefatto_dao.read_artefatto()

        if artefatti_totali is None:
            return None

        risultato_filtrato = []

        for artefatto in artefatti_totali:
            #il filtro del museo deve essere o none o uguale all'id selezionato
            filtro_museo = (museo is None) or (str(artefatto.id_museo) == str(museo))
            #il filtro dell'epoca deve essere o none o uguale all'epoca selezionata
            filtro_epoca = (epoca is None) or (artefatto.epoca == epoca)

            #se supero i filtri allora posso mostrare l'artefatto
            if filtro_museo and filtro_epoca:
                risultato_filtrato.append(artefatto)

        return risultato_filtrato



    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        lista_epoche = []
        artefatti = self._artefatto_dao.read_artefatto()

        if artefatti is None:
            return None

        for artefatto in artefatti:
            if artefatto.epoca is not None:
                lista_epoche.append(artefatto.epoca)
        return lista_epoche


    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        lista_musei = self._museo_dao.read_museo()

        if lista_musei is None:
            print('Errore di connessione o recupero dati.')
            return None

        if len(lista_musei) == 0:
            print('Nessun museo presente nel database')
            return None

        return lista_musei




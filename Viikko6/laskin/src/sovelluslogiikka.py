class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen = 0

    def plus(self, operandi):
        self._tallenna_tila()
        self._arvo += operandi

    def miinus(self, operandi):
        self._tallenna_tila()
        self._arvo -= operandi

    def nollaa(self):
        self._tallenna_tila()
        self._arvo = 0

    def _tallenna_tila(self):
        self._edellinen = self._arvo

    def kumoa(self):
        self._arvo, self._edellinen = self._edellinen, self._arvo

    def arvo(self):
        return self._arvo

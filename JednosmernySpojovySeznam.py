class Uzel:
    def __init__(self, hodnota):
        self.hodnota = hodnota
        self.dalsi = None


class JednosmernySeznam:
    def __init__(self):
        self.prvni = None

    def pridat(self, hodnota):
        novy = Uzel(hodnota)
        if self.prvni is None:
            self.prvni = novy
            return
        aktualni = self.prvni
        while aktualni.dalsi is not None:
            aktualni = aktualni.dalsi
        aktualni.dalsi = novy

    def vypsat(self):
        aktualni = self.prvni
        while aktualni is not None:
            print(aktualni.hodnota)
            aktualni = aktualni.dalsi


seznam = JednosmernySeznam()
for x in [10, 20, 30, 40, 50]:
    seznam.pridat(x)

seznam.vypsat()

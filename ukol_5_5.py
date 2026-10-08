class Uzel:
    def __init__(self, hodnota):
        self.hodnota = hodnota
        self.predchozi = None
        self.dalsi = None


class ObousmernySeznam:
    def __init__(self):
        self.prvni = None
        self.posledni = None

    def pridat(self, hodnota):
        novy = Uzel(hodnota)
        if self.posledni is None:
            self.prvni = self.posledni = novy
        else:
            novy.predchozi = self.posledni
            self.posledni.dalsi = novy
            self.posledni = novy

    def vypsat_dopredu(self):
        aktualni = self.prvni
        while aktualni is not None:
            print(aktualni.hodnota)
            aktualni = aktualni.dalsi

    def vypsat_dozadu(self):
        aktualni = self.posledni
        while aktualni is not None:
            print(aktualni.hodnota)
            aktualni = aktualni.predchozi


seznam = ObousmernySeznam()
for x in [10, 20, 30, 40, 50]:
    seznam.pridat(x)

print("Od prvniho k poslednimu:")
seznam.vypsat_dopredu()
print("Od posledniho k prvnimu:")
seznam.vypsat_dozadu()

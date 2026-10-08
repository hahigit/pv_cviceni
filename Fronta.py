class PrazdnaFrontaException(Exception):
    pass


class Uzel:
    def __init__(self, hodnota):
        self.hodnota = hodnota
        self.predchozi = None
        self.dalsi = None


class Fronta:
    def __init__(self):
        self._prvni = None
        self._posledni = None
        self._pocet = 0

    def add(self, hodnota):
        novy = Uzel(hodnota)
        if self._posledni is None:
            self._prvni = self._posledni = novy
        else:
            novy.predchozi = self._posledni
            self._posledni.dalsi = novy
            self._posledni = novy
        self._pocet += 1

    def pop(self):
        if self._prvni is None:
            raise PrazdnaFrontaException("Fronta je prazdna")
        uzel = self._prvni
        self._prvni = uzel.dalsi
        if self._prvni is None:
            self._posledni = None
        else:
            self._prvni.predchozi = None
        self._pocet -= 1
        return uzel.hodnota

    def count(self):
        return self._pocet

    def clear(self):
        self._prvni = None
        self._posledni = None
        self._pocet = 0

    def popAll(self):
        vysledek = []
        while self._prvni is not None:
            vysledek.append(self.pop())
        return vysledek


if __name__ == "__main__":
    f = Fronta()
    for x in [1, 2, 3, 4, 5]:
        f.add(x)
    print("Pocet:", f.count())
    print("pop:", f.pop())
    print("Pocet:", f.count())
    print("popAll:", f.popAll())
    print("Pocet:", f.count())

    f.add("a")
    f.add("b")
    f.clear()
    print("Po clear, pocet:", f.count())

    try:
        f.pop()
    except PrazdnaFrontaException as e:
        print("Chyba:", e)

class PrazdnyZasobnikException(Exception):
    pass


class Uzel:
    def __init__(self, hodnota):
        self.hodnota = hodnota
        self.dalsi = None


class Zasobnik:
    def __init__(self):
        self._vrchol = None
        self._pocet = 0

    def add(self, hodnota):
        novy = Uzel(hodnota)
        novy.dalsi = self._vrchol
        self._vrchol = novy
        self._pocet += 1

    def pop(self):
        if self._vrchol is None:
            raise PrazdnyZasobnikException("Zasobnik je prazdny")
        uzel = self._vrchol
        self._vrchol = uzel.dalsi
        self._pocet -= 1
        return uzel.hodnota

    def count(self):
        return self._pocet

    def clear(self):
        self._vrchol = None
        self._pocet = 0

    def popAll(self):
        vysledek = []
        while self._vrchol is not None:
            vysledek.append(self.pop())
        return vysledek


if __name__ == "__main__":
    z = Zasobnik()
    for x in [1, 2, 3, 4, 5]:
        z.add(x)
    print("Pocet:", z.count())
    print("pop:", z.pop())
    print("Pocet:", z.count())
    print("popAll:", z.popAll())
    print("Pocet:", z.count())

    z.add("a")
    z.add("b")
    z.clear()
    print("Po clear, pocet:", z.count())

    try:
        z.pop()
    except PrazdnyZasobnikException as e:
        print("Chyba:", e)

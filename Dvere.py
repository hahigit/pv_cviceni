class ZamceneDvereException(Exception):
    pass


class Dvere:
    def __init__(self, zamceno=False):
        self.zamceno = zamceno

    def otevrit(self):
        if self.zamceno:
            raise ZamceneDvereException("Dvere jsou zamcene")


d = Dvere(zamceno=True)
try:
    d.otevrit()
    print("Prosel jsem")
except ZamceneDvereException as e:
    print("Dvere jsou zamcene, nemuzes je otevrit")

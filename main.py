from Bottle import Bottle
from Door import Door

lahev = Bottle(50)
print(lahev.capacity_l)

d = Door(zamceno=True)
try:
    d.otevrit()
    print("Prosel jsem")
except ZamceneDvereException as e:
    print("Dvere jsou zamcene, nemuzes je otevrit")
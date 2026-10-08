from Auto import Auto

auto = Auto(30, 12.5)      # nádrž 30 l, spotřeba 12,5 l/100 km

auto.natankuj(22.5)        # nádrž byla prázdná, takže teď je v ní 22,5 l
auto.popojed(20)           # 20 km při 12,5 l/100 km = spotřeba 2,5 l

print(auto.aktualni_stav_nadrze())   # 20.0
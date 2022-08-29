dikt = {1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "piec", 6: "szesc", 7: "siedem"}

# wzór
dict_comprehhension = {a: b for a, b in dikt.items()}

# zrob dicta z kluczem od 3 do 5
od_trzech_do_pieciu = {a: b for a, b in dikt.items() if 5 >= a >= 3}
print()

# przemnóż klucz razy 4, wartosc ma być str "klucz" przykład: {4:"klucz"}
mnozenie = {a*4: "klucz" for a, b in dikt.items()}
print()

# zrob dicta zamień klucz na str a do wartosci dodaj "klucz"
zmien_klucz = {str(a): f"{b} klucz" for a, b in dikt.items()}
print()

# zrob dicta {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7"}
zrobienie_dicta = {a: f"{a}" for a, b in dikt.items()}
print()
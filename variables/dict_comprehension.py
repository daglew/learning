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

# zrób dicta tylko z kluczmi większymi od 3
klucz_wiekszy_od_trzech = {a: b for a, b in dikt.items() if a > 3}
print(klucz_wiekszy_od_trzech)

# zrób dict comprehennsion uzywając listy lista_for_dict =[1,2,3,4,5,6,7,8,9,10]
# wynik {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
lista_for_dict = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
z_listy_dict = {a: a*a for a in lista_for_dict}
print(z_listy_dict)

# zrób dicta z {"1": True, 2: 0.1, "str":"str", 4:(0), 6:[]}
# wrzuć tylko wartości gdzie kuczem jest int a wartością ma być typ wartości
k = {"1": True, 2: 0.1, "str": "str", 4: (0, 1, 2), 6: []}
kluczem_int = {a: type(b) for a, b in k.items() if isinstance(a, int)}
print(kluczem_int)

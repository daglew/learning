moj_dict = {"slownik": "wartosc", 20: [3, 4]}

#  wyciagam wartosc tak jak w liscie tylko po kluczu
wyciagam_powartosci_klucza = moj_dict[20]
print(wyciagam_powartosci_klucza)

# iteracja po dicts
dict_34 = {"foka": "morze", "pingwin": "lodowiec"}
for key, value in dict_34.items():
    print(key, value)
print()
for key in dict_34.keys():
    print(key)
print()
for value in dict_34.values():
    print(value)

# sprawdzam instancje zwraca True lub False
sprawdzam_instancje = isinstance(moj_dict, dict)
print(sprawdzam_instancje)

# sprawdzam typ
sprawdzam_typ = type(moj_dict)
print(sprawdzam_typ)

# setdefault()	Zwraca wartość określonego klucza. Jeśli klucz nie istnieje: włóż klucz o określonej wartości
wartosc_2 = {"foka": "morze", "wielblad": "piasek", "pingwin": "lodowiec"}
zwraca_wartosc_klucza = wartosc_2.setdefault("wielblad", "pies")
print(zwraca_wartosc_klucza)

# clear()	Usuwa wszystkie elementy ze słownika
usuwa_wszystko = {"pies": "dog", 4: [2, 90]}
print(usuwa_wszystko)
usuwa_wszystko.clear()
print(usuwa_wszystko)

# copy()	Zwraca kopię słownika
zwraca_kopie = moj_dict.copy()
print(zwraca_kopie)

# fromkeys()	Zwraca słownik z określonymi kluczami i wartością
to_dict = {"cat": "kot", "horse": "kon"}
to_klucz = 20
to_wartosc_i_klucz= dict.fromkeys(to_dict, to_klucz)
print(to_wartosc_i_klucz)

# get()	Zwraca wartość podanego klucza
wartosc_1 = {"foka": "morze", "wielblad": "piasek", "pingwin": "lodowiec"}
wartosc_podanego_klucza = wartosc_1.get("pingwin")
print(wartosc_podanego_klucza)

# items()	# items() Zwraca listę zawierającą tuple dla każdej pary klucz-wartość
zwraca_tuple = moj_dict.items()
print(zwraca_tuple)


# keys()    #Zwraca listę zawierającą klucze słownika
lista_zawiera_klucze = moj_dict.keys()
print(lista_zawiera_klucze)

# pop()	Usuwa element z podanym kluczem
moj_dict.pop(20)
print(moj_dict)

# popitem()	Usuwa ostatnią wstawioną parę klucz-wartość
wartosc_1 = {"foka": "morze", "wielblad": "piasek", "pingwin": "lodowiec"}
wartosc_1.popitem()
print(wartosc_1)

# update()	Aktualizuje słownik za pomocą określonych par klucz-wartość
wartosc_1 = {"foka": "morze", "wielblad": "piasek", "pingwin": "lodowiec"}
wartosc_1.update({"kura": "ziarno"})
print(wartosc_1)

# values()	Zwraca listę wszystkich wartości w słowniku
print(wartosc_1.values())


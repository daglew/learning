moja_tupla = (24, 86, "looop")

# sprawdzam instancje zwraca True lub False
sprawdzam_instancje = isinstance(moja_tupla, tuple)
print(sprawdzam_instancje)

# sprawdzam typ
sprawdzam_typ = type(moja_tupla)
print(sprawdzam_typ)

#  wyciagam wartosc
wyciagam_indeks_2 = moja_tupla[2]
print(wyciagam_indeks_2)

#  iteruje po tuple
for element in moja_tupla:
    print(element)

#  robie f""
przykladowy_fstr = f"Tutaj wklejam zmienna moja tupla: {moja_tupla}"
print(przykladowy_fstr)

# podmieniam wartosc w tuple
lista_z_mojej_tuple = list(moja_tupla)
print(lista_z_mojej_tuple)
lista_z_mojej_tuple[2] = 5
print(lista_z_mojej_tuple)
konwertuje_do_tuple = tuple(lista_z_mojej_tuple)
print(konwertuje_do_tuple)

# count()	zlicza ilosc podanej frazy w tuple, zwraca inta
print(moja_tupla.count(24))


# index()	wyszukuje po wartosci tuple jego indeks
print(moja_tupla.index(24))

# dodawanie tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
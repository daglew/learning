moja_lista = [10, 100, 1000]

# sprawdzam instancje zwraca True lub False
sprawdzam_instancje = isinstance(moja_lista, list)
print(sprawdzam_instancje)

# sprawdzam typ
sprawdzam_typ = type(moja_lista)
print(sprawdzam_typ)

#  wyciagam wartosc
wyciagam_indeks_2 = moja_lista[2]
print(wyciagam_indeks_2)

# wyciaganie wartosci bardziej zlozone
lista_z = [23, True, ["ko", 87, None, [5, "rower"]]]
lista_z_rower = lista_z[2][3][1]
print(lista_z_rower)

#  iteruje po list
for element in moja_lista:
    print(f"x+{element}")
print()
# lists comprehension
nowa_lista = [print(f"x+{element}") for element in moja_lista]

#  robie f""
przykladowy_fstr = f"Tutaj wklejam zmienna moja liste: {moja_lista}"
print(przykladowy_fstr)

# podmieniam wartosc w lista
print(moja_lista)
moja_lista[1] = 200
print(moja_lista)

# count()	zlicza ilosc podanej frazy w lista, zwraca inta
print(moja_lista.count(10))

# index()	wyszukuje po wartosci lista jego indeks
print(moja_lista.index(1000))

# dodawanie lista
lista_1 = [5, 25, "piec"]
lista_2 = ["jeden", 1, 21]
lista_3 = lista_1 + lista_2
print(lista_3)

# append()	dodaje element do listy
lista_x = [2, None, 89, False, 91, [45, 5]]
lista_x.append(222)
print(lista_x)

# clear()	usuwa cala zarartosc listy
moja_lista_0 = [5, 6, 7]
moja_lista_0.clear()
print(moja_lista_0)

# copy()	zwraca kopie listy
v = moja_lista.copy()
print(v)

# count()	zlicza ilosc podanej frazy w lists, zwraca inta
moja_lista_90 = [10, 100, 1000]
print(moja_lista_90.count(1000))

# extend()	poszerzam liste o wartosci z dodawanej listy
# moja_lista.extend()
lista_xyz = [1, 2, 3]
lista_ac = [4, 5, 6]
# lista_xyz.append(lista_ac)
lista_xyz.extend(lista_ac)
print(lista_xyz)

# index()	Zwraca indeks pierwszego elementu o określonej wartości
print(moja_lista.index(10))

# insert()	dodaje element na określonej pozycji
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# pop()	usuwa element w liscie po indeksie
moja_lista.pop(1)
print(moja_lista)

# remove()	Usuwa element o określonej wartości
moja_lista.remove(10)
print(moja_lista)

# reverse()	Odwraca kolejność na liście( pierwszy sposob)
moja_lista_6 = [10, 100, 1000]
moja_lista_6.reverse()
print(moja_lista_6)
# odwracam liste na drugi sposob
print(moja_lista_6[::-1])

# sort()	Sorts the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)



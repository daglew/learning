this_list = ["sil", 56, 89.5, True, "uuu"]
second_list = [189, 8, (), "por", 56.7]

print(len(this_list), len(second_list))
# metoda len() powoduje sprawdzenie dlugosci listy

# podmiana wartosci w liscie
this_list = ["sil", 56, 89.5, True, "uuu"]
print(this_list[0])
this_list[0] = "try"
print(this_list)

second_list = [189, 8, (), "por", 56.7]
second_list[1] = "lol"
print(second_list[1])


# metoda clear() czysci liste
this_list = ["sil", 56, 89.5, True, "uuu"]
this_list.clear()
print(this_list)


# metoda remove() usuwa wartosc pozycji z listy odejmowanie
this_list = ["sil", 56, 89.5, True, "uuu"]
this_list.remove("uuu")
print(this_list)

# metoda pop() usuwa element o indeksie np.3
this_list = ["sil", 56, 89.5, True, "uuu"]
this_list.pop(3)
print(this_list)

# iteracja=powtorzenie
this_list = ["sil", 56, 89.5, True, "uuu"]

# petla for przejdzie po kazdym elemencie w this_list nastepnie wyprintuje go
for element in this_list:
    print(element)

# petla if
this_list = ["sil", 56, 89.5, True, "uuu"]

if this_list == ["sil", 56, 89.5, True, "uuu"]:
    print(f"Prawda ta lista się równa weż zmienną i ją wyprintuj: {this_list}")
else:
    print(f"Ta lista: {this_list} nie jest prawdą ")

print(type(this_list))


a = 12
b = 9
if b > a:
    print(f"wartosc b: {b} jest wieksze od wartosci a: {a} ")
else:
    print(f"wartosc b: {b} nie jest wieksza od wartosci a: {a}")


if b < a and b < 8:
    print(f"wartosc b: {b} jest wieksze od wartosci a: {a} ")
elif b == 9:
    print(f"wartosc b: {b} jest rowna 9 ")
else:
    print(f"wartosc b: {b} nie jest wieksza od wartosci a: {a}")


try:
    assert b>a, f"B:{b} nie jest wieksze od {a}"
except AssertionError:
    raise Exception(f"wartosc b:{b}, nie jest wieksze od {a}")

lista_do_iteracji = [1, 2, 3, 45, 6, 6, 7, 77, (), "strig", True, None, False]

nowa_lista = []

for element in lista_do_iteracji:
    nowa_lista.append(element)

print(nowa_lista)

lista_do_iteracji_2 = [1, 2, 3, 45, 6, 6, 7, 77]

nowa_lista_2 = []

# metoda apppend() dodaje do listy element
for element in lista_do_iteracji_2:
    nowy_element = element * 2
    nowa_lista_2.append(nowy_element)

print(nowa_lista_2)

prawda = False
falsz = False

if prawda == True:
    print(f"prawda: {prawda}")
else:
    print(f"falsz: {prawda}")

if prawda != True:
    print(f"zmienna prawda: {prawda} != True")
else:
    print(f"zmienna prawda: {prawda} == True")

string = "dsfsdfsdadfsfsda"
nowa_lista_str_wykrzyknik = []

for element in string:
    nowy_element = f"{element}!"
    nowa_lista_str_wykrzyknik.append(nowy_element)
print(nowa_lista_str_wykrzyknik)

if string == []:
    print(f"zmienna string: {string} jest pusta lista")
else:
    print(f"zmienna string: {string} nie jest pusta lista")

imie = "dagmara"
nazwisko = "lewandowska"
dlugosc_imie = len(imie)
dlugosc_nazwisko = len(nazwisko)
print(f"dlugosc mojego imienia to: {dlugosc_imie} moje imie to: {imie}")
print(f"dlugosc mojego nazwiska to: {dlugosc_nazwisko} moje nazwisko to: {nazwisko}")

if dlugosc_imie == 8:
    print("ok")
else:
    print("nieok")

if nazwisko == "lewadowska":
    print(f"to prawda: {nazwisko} to lewandowska")
else:
    print(f"to nieprawda: {nazwisko} moje nazwisko to lewandowska")

for litera in nazwisko:
    if litera == "l":
        print(f"litera l:{litera}")

lista = [9, "po", 7.89]

for element in lista:
    if element == 9:
        print(f"element 9: {element}")
    elif element == "po":
        print(f"element 'po': {element}")
    else:
        print(f"element to 7.89: {element}")



lista_2 = [4, 7, 90]
lista_3 = []

for element in lista_2:
    lista_3.append(element)

for element in lista_2:
    nowy_element = element*2
    lista_3.append(nowy_element)

lista_3.pop(1)

if lista_2 == lista_3:
    print(f"tak to prawda ze lista_2:{lista_2} jest rowna lista_3:{lista_3}:")
else:
    print(f"nie to nieprawda lista_2:{lista_2} nie jest rowna lista_3:{lista_3}")
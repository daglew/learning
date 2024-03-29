
""""
zrob assercie wykorzystaj try except blok do przechwycenia wyjatku AssertionError

"""

zmienna = 3
druga_zmienna = "dwa"

# printowanie wyjatku
try:
    assert zmienna == druga_zmienna, f"Wartosc zmiennej: {zmienna} nie jest wartosci drugiej zmiennej: {druga_zmienna}"
except AssertionError as ex:
    print(ex)

# wyrzucanie wyjatku
lista1 = [6]
string1 = "oko"

try:
    assert lista1 == string1, f"Wartosc lista1: {lista1}, nie jest wartosci string1: {string1}"
except AssertionError as hgfgnfnfnnfnfnfn:
    raise Exception(f"Przechwycilam wyjatek hgfgnfnfnnfnfnfn: {hgfgnfnfnnfnfnfn}, przy sprawdaniu asserci wartosci "
                    f"lista1: {lista1}, oraz wartosci string1: {string1}")
# druga_zmienna = "oko"

# printowanie wyjatku
try:
    assert zmienna == druga_zmienna, f"Wartosc zmiennej: {zmienna} nie rowna sie wartosci drugiej zmiennej: {druga_zmienna}"
except AssertionError as ex:
    print(ex)


# wyrzucanie wyjatku
lista1 = [6]
string1 = "oko"

try:
    assert lista1 == string1, f"Wartosc lista1: {lista1}, nie jest rowna wartosci string1: {string1}"
except AssertionError as hgfgnfnfnnfnfnfn:
    raise Exception(f"Przechwycilam wyjatek hgfgnfnfnnfnfnfn: {hgfgnfnfnnfnfnfn}, przy sprawdaniu asserci wartosci "
                    f"lista1: {lista1}, oraz wartosci string1: {string1}")

"""
napisz funkcje ktora przyjmuje zmienna
w tej funkcji jezeli zmienna nie jest float wyrzuc wyjatek
zwroc zmienna
"""

zmienna_float = 123
# zmienna_float = 1.23

def funkcjia_ktora_przyjmuje_zmienna(zmienna):
    if not isinstance(zmienna, float):
        raise Exception(f"Podany typ danych: {zmienna_float} nie jest floatem")
    return zmienna

funkcjia_ktora_przyjmuje_zmienna(zmienna_float)

""""
funkcja przyjmuje list
sprawdz czy lista ma wartosc w srodku
jesli niema wyrzuc wyjatek
nastepnie przeiteruj po wartosciach - for
zamien je w str
i dodaj xd
zwroc liste z nowymi wartosciami
exception (podana lista jest pusta)
"""

lista_zmienna = []
lista_ze_zmiennymi = [10, "rrr", 1.45, (5, 89), {"a": 23}]


def funkcja_przyjmuje_list(lista):
    if lista == []:
        raise Exception(f"Podana lista: {lista} jest pusta")

    lista_z_nowymi_wartosciami = []
    for element in lista:
        string_plus_xd = f"{element}xd"
        lista_z_nowymi_wartosciami.append(string_plus_xd)

    list_comprehension = [f"{element}xd" for element in lista]


    return lista_z_nowymi_wartosciami, list_comprehension




# funkcja_przyjmuje_list(lista=lista_zmienna)
lista_z_nowymi_wartosciami, list_comprehension = funkcja_przyjmuje_list(lista=lista_ze_zmiennymi)
print(lista_z_nowymi_wartosciami)
print(list_comprehension)


"""
funkcja ktora przyjmuje listy
warunkiem wstepnym ktory przyjmuje lista
dlugosc listy ma byc dluzsza niz dwa objekty w lisiecie
w przeciwnym wypadku ma wyrzucic wyjatek (error) ze lista jest za krotka 
przeiterowac po elemencie od 3 do ostatniego (slices)
sprawdz typ elementu 
wrzucic typ elementu i nazwe elementu jako f"" do nowej_listy
"""

lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = [7, 8]

def dluzsza_niz_dwa_objekty(lista):
    if not len(lista) > 2:
        raise Exception(f"Podana lista: {lista} jest za krotka")

    lista_z_typem_elementu = []
    for element in lista[3::]:
        f_string = f"{type(element)} {element}"
        lista_z_typem_elementu.append(f_string)

    return lista_z_typem_elementu


a = dluzsza_niz_dwa_objekty(lista=lista_1)
# b = dluzsza_niz_dwa_objekty(lista=lista_2)

print(a)
# print(b)
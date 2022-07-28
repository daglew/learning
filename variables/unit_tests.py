
#
# # funkcja_przyjmuje_list(lista=lista_zmienna)
# lista_z_nowymi_wartosciami, list_comprehension = funkcja_przyjmuje_list(lista=lista_ze_zmiennymi)
# print(lista_z_nowymi_wartosciami)
# print(list_comprehension)
#
# """
# 1. Obórć string aby otrzymać wynik poniżej
# string_1 = "who are you"
# wynik = "you are who"
#
# 2. drugim kroku zrób z tego funkcję która będzie wykorzystywała powyższy kod
#
# 3. Zrób test swojej funkcji
#
# """
#
# string_1 = "who are you"
#
# lista_ze_str = string_1.split()
# obrocona_lista = lista_ze_str[::-1]
#
# # lista_ze_str.reverse()
# print(obrocona_lista)
#
#
# string_1 = "who are you"
#
#
# def obracam_str(zmienna: str):
#     lista_ze_str = zmienna.split()
#     obrocona_lista = lista_ze_str[::-1]
#     lista_na_str = ' '.join([str(elem) for elem in obrocona_lista])
#     return lista_na_str
#
# t = obracam_str(zmienna=string_1)
# t1 = obracam_str(zmienna="kota ma Ala")
#
# print(t)
# print(t1)
#
# def test_obracam_str():
#     str = "Psa ma Zosia"
#     expected_result = "Zosia ma Psa"
#     current_result = obracam_str(zmienna=str)
#     assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result: {current_result}."
#
# test_obracam_str()
#
# reverse= "ddfed eedcced efefve"

"""
napisz funkcje ktora przyjmuje zmienna typu int, str, bool, float
zwraca element jezlei okaze sie instancja danego typu
napisz testy
(if, elif, else)
"""
zmienna = 4

def sprawdzam_typ(zmienna):
    if isinstance(zmienna, str):
        return zmienna
    elif isinstance(zmienna, float):
        return zmienna
    elif isinstance(zmienna, bool):
        return zmienna
    elif isinstance(zmienna, int):
        return zmienna
    else:
        return Exception(f"Inny tym zmiennej: {zmienna}")

print(sprawdzam_typ(zmienna=zmienna))

def test_sprawdzam_czy_int():
    zmienna = 4
    expected_result_int = zmienna
    current_result = sprawdzam_typ(zmienna=zmienna)
    assert expected_result_int == current_result, f"Expected result: {expected_result_int}" \
                                                  f"is not equal to current result: {current_result}"

test_sprawdzam_czy_int()


def test_sprawdzam_czy_str():
    zmienna = ""
    expected_result_str = zmienna
    current_result = sprawdzam_typ(zmienna=zmienna)
    assert expected_result_str == current_result, f"Expected result: {expected_result_str}" \
                                                  f"is not equal to current result: {current_result}"

test_sprawdzam_czy_str()


def test_sprawdzam_czy_bool():
    zmienna = True
    expected_result_bool = zmienna
    current_result = sprawdzam_typ(zmienna=zmienna)
    assert expected_result_bool == current_result, f"Expected result: {expected_result_bool}" \
                                                  f"is not equal to current result: {current_result}"

test_sprawdzam_czy_bool()


def test_sprawdzam_czy_float():
    zmienna = 2.23
    expected_result_float = zmienna
    current_result = sprawdzam_typ(zmienna=zmienna)
    assert expected_result_float == current_result, f"Expected result: {expected_result_float}" \
                                                  f"is not equal to current result: {current_result}"

test_sprawdzam_czy_float()

def test_sprawdzam_czy_error():
    zmienna = ()
    expected_result_error = zmienna
    current_result = sprawdzam_typ(zmienna=zmienna)
    assert expected_result_error != current_result, f"Expected result: {expected_result_error}" \
                                                  f" is equal to current result: {current_result}"

test_sprawdzam_czy_error()

"""
please write the functions which is taking lists as a variable,
in list you will have every single variable
and your function will be creating new list
which will be return only ints and floats

please write the tests for this function
"""
list_one = [1, 4.56, (78, "po"), None, 9.99, 101, 3.24, "org", 8]


def funkcja_ktora_przyjmuje_liste(list00):
    new_list = []
    for element in list00:
        if isinstance(element, int):
            new_list.append(element)
        elif isinstance(element, float):
            new_list.append(element)

    return new_list


o = funkcja_ktora_przyjmuje_liste(list00=list_one)
print(o)


def test_funkcji_ktora_przyjmuje_liste():
    zmienna = [1, 4.56, (78, "po"), None, 9.99, 101, 3.24, "org", 8]
    expected_result = [1, 4.56, 9.99, 101, 3.24, 8]
    current_result = funkcja_ktora_przyjmuje_liste(list00=zmienna)
    assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result: {current_result}."

test_funkcji_ktora_przyjmuje_liste()

def test_funkcji_ktora_przyjmuje_liste_length():
    zmienna = [1, 4.56, (78, "po"), None, 9.99, 101, 3.24, "org", 8]
    expected_result = 6
    current_result = funkcja_ktora_przyjmuje_liste(list00=zmienna)
    assert expected_result == len(current_result), f"Expected length result: {expected_result} is not equal to current length result: {len(current_result)}."

test_funkcji_ktora_przyjmuje_liste_length()

def test_funkcji_ktora_przyjmuje_liste_negative():
    zmienna = [1, 4.56, (78, "po"), None, 9.99, 101, 3.24, "org", 8]
    expected_result = [1, 4.56, {"r": "l"}, 9.99, 101, 3.24, 8]
    current_result = funkcja_ktora_przyjmuje_liste(list00=zmienna)
    assert expected_result != current_result, f"Expected result: {expected_result} is equal to current result: {current_result}."

test_funkcji_ktora_przyjmuje_liste_negative()

def test_funkcji_ktora_przyjmuje_liste_type():
    zmienna = [1, 4.56, (78, "po"), None, 9.99, 101, 3.24, "org", 8]
    current_result = funkcja_ktora_przyjmuje_liste(list00=zmienna)
    assert isinstance(current_result, list), f"Current result: {current_result} is not instance of list."

test_funkcji_ktora_przyjmuje_liste_type()



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

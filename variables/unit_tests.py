
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
#
# """
# napisz funkcje ktora przyjmuje zmienna typu int, str, bool, float
# zwraca element jezlei okaze sie instancja danego typu
# napisz testy
# (if, elif, else)
# """
# zmienna = 4
#
# def sprawdzam_typ(zmienna):
#     if isinstance(zmienna, str):
#         return zmienna
#     elif isinstance(zmienna, float):
#         return zmienna
#     elif isinstance(zmienna, bool):
#         return zmienna
#     elif isinstance(zmienna, int):
#         return zmienna
#     else:
#         return Exception(f"Inny tym zmiennej: {zmienna}")
#
# print(sprawdzam_typ(zmienna=zmienna))
#
# def test_sprawdzam_czy_int():
#     zmienna = 4
#     expected_result_int = zmienna
#     current_result = sprawdzam_typ(zmienna=zmienna)
#     assert expected_result_int == current_result, f"Expected result: {expected_result_int}" \
#                                                   f"is not equal to current result: {current_result}"
#
# test_sprawdzam_czy_int()
#
#
# def test_sprawdzam_czy_str():
#     zmienna = ""
#     expected_result_str = zmienna
#     current_result = sprawdzam_typ(zmienna=zmienna)
#     assert expected_result_str == current_result, f"Expected result: {expected_result_str}" \
#                                                   f"is not equal to current result: {current_result}"
#
# test_sprawdzam_czy_str()
#
#
# def test_sprawdzam_czy_bool():
#     zmienna = True
#     expected_result_bool = zmienna
#     current_result = sprawdzam_typ(zmienna=zmienna)
#     assert expected_result_bool == current_result, f"Expected result: {expected_result_bool}" \
#                                                   f"is not equal to current result: {current_result}"
#
# test_sprawdzam_czy_bool()
#
#
# def test_sprawdzam_czy_float():
#     zmienna = 2.23
#     expected_result_float = zmienna
#     current_result = sprawdzam_typ(zmienna=zmienna)
#     assert expected_result_float == current_result, f"Expected result: {expected_result_float}" \
#                                                   f"is not equal to current result: {current_result}"
#
# test_sprawdzam_czy_float()
#
# def test_sprawdzam_czy_error():
#     zmienna = ()
#     expected_result_error = zmienna
#     current_result = sprawdzam_typ(zmienna=zmienna)
#     assert expected_result_error != current_result, f"Expected result: {expected_result_error}" \
#                                                   f" is equal to current result: {current_result}"
#
# test_sprawdzam_czy_error()
#
#
# """
# please write the functions which is taking lists as a variable,
# in list you will have every single variable
# and your function will be creating new list
# which will be return only ints and floats
#
# please write the tests for this function
# """
# list_one = [1, 4.56, (78, "po"), None, 9.99, 101, 3.24, "org", 8]
#
#
# def funkcja_ktora_przyjmuje_liste(list00):
#     new_list = []
#     for element in list00:
#         if isinstance(element, int):
#             new_list.append(element)
#         elif isinstance(element, float):
#             new_list.append(element)
#
#     return new_list
#
#
# o = funkcja_ktora_przyjmuje_liste(list00=list_one)
# print(o)
#
#
# def test_funkcji_ktora_przyjmuje_liste():
#     zmienna = [1, 4.56, (78, "po"), None, 9.99, 101, 3.24, "org", 8]
#     expected_result = [1, 4.56, 9.99, 101, 3.24, 8]
#     current_result = funkcja_ktora_przyjmuje_liste(list00=zmienna)
#     assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result: {current_result}."
#
# test_funkcji_ktora_przyjmuje_liste()
#
# def test_funkcji_ktora_przyjmuje_liste_length():
#     zmienna = [1, 4.56, (78, "po"), None, 9.99, 101, 3.24, "org", 8]
#     expected_result = 6
#     current_result = funkcja_ktora_przyjmuje_liste(list00=zmienna)
#     assert expected_result == len(current_result), f"Expected length result: {expected_result} is not equal to current length result: {len(current_result)}."
#
# test_funkcji_ktora_przyjmuje_liste_length()
#
# def test_funkcji_ktora_przyjmuje_liste_negative():
#     zmienna = [1, 4.56, (78, "po"), None, 9.99, 101, 3.24, "org", 8]
#     expected_result = [1, 4.56, {"r": "l"}, 9.99, 101, 3.24, 8]
#     current_result = funkcja_ktora_przyjmuje_liste(list00=zmienna)
#     assert expected_result != current_result, f"Expected result: {expected_result} is equal to current result: {current_result}."
#
# test_funkcji_ktora_przyjmuje_liste_negative()
#
# def test_funkcji_ktora_przyjmuje_liste_type():
#     zmienna = [1, 4.56, (78, "po"), None, 9.99, 101, 3.24, "org", 8]
#     current_result = funkcja_ktora_przyjmuje_liste(list00=zmienna)
#     assert isinstance(current_result, list), f"Current result: {current_result} is not instance of list."
#
# test_funkcji_ktora_przyjmuje_liste_type()
#
# """
# stworz kalkulator (dwie liczy i dzialanie jako string)
# """
#
#
# def kalkulator(liczba_1: int, liczba_2: int, dzialanie: str):
#     if not isinstance(liczba_1, int) or not isinstance(liczba_2, int):
#         return Exception(f"Liczba_1: {liczba_1} lub liczba_2: {liczba_2} nie jest int.")
#     if not isinstance(dzialanie, str):
#         return Exception(f"Dzialanie: {dzialanie} nie jest str.")
#
#     if dzialanie == "dodawanie":
#         return liczba_1 + liczba_2
#     elif dzialanie == "odejmowanie":
#         return liczba_1 - liczba_2
#     elif dzialanie == "mnozenie":
#         return liczba_1 * liczba_2
#     elif dzialanie == "dzielenie":
#         return liczba_1 / liczba_2
#     else:
#         return f"Bad result {dzialanie}, expected dzialanie: dodawanie, odejmowanie, mnozenie, dzielenie"
#
#
# dodwanie = kalkulator(liczba_1=1, liczba_2=2, dzialanie="dodawanie")
# print(dodwanie)
# odejmowanie = kalkulator(liczba_1=1, liczba_2=2, dzialanie="odejmowanie")
# print(odejmowanie)
# mnozenie = kalkulator(liczba_1=1, liczba_2=2, dzialanie="mnozenie")
# print(mnozenie)
# dzielenie = kalkulator(liczba_1=1, liczba_2=2, dzialanie="dzielenie")
# print(dzielenie)
# bledzne_dzialanie = kalkulator(liczba_1=1, liczba_2=2, dzialanie="cokolwiek")
# print(bledzne_dzialanie)
#
# sprawdzam_instancje_int = dzielenie = kalkulator(liczba_1="lol", liczba_2=2, dzialanie="dzielenie")
# print(sprawdzam_instancje_int)
# sprawdzam_instancje_str = mnozenie = kalkulator(liczba_1=1, liczba_2=2, dzialanie=10)
# print(sprawdzam_instancje_str)
#
# # unit testy funkcji kalkulator
# def test_funkcji_kalkulator_dodawanie():
#     expected_result = 3
#     current_result = kalkulator(liczba_1=1, liczba_2=2, dzialanie="dodawanie")
#     assert expected_result == current_result, f"Expected result: {expected_result} is equal to current " \
#                                               f"result: {current_result}."
# test_funkcji_kalkulator_dodawanie()
#
# def test_funkcji_kalkulator_odejmowanie():
#     expected_result = -1
#     current_result = kalkulator(liczba_1=1, liczba_2=2, dzialanie="odejmowanie")
#     assert expected_result == current_result, f"Expected result: {expected_result} is equal to current " \
#                                               f"result: {current_result}."
# test_funkcji_kalkulator_odejmowanie()
#
# def test_funkcji_kalkulator_mnozenie():
#     expected_result = 2
#     current_result = kalkulator(liczba_1=1, liczba_2=2, dzialanie="mnozenie")
#     assert expected_result == current_result, f"Expected result: {expected_result} is equal to current " \
#                                               f"result: {current_result}."
# test_funkcji_kalkulator_mnozenie()
#
# def test_funkcji_kalkulator_dzielenie():
#     expected_result = 0.5
#     current_result = kalkulator(liczba_1=1, liczba_2=2, dzialanie="dzielenie")
#     assert expected_result == current_result, f"Expected result: {expected_result} is equal to current " \
#                                               f"result: {current_result}."
# test_funkcji_kalkulator_dzielenie()
#
#
# def test_funkcji_kalkulator_bledne_dzialanie_str():
#     dzialanie = "pop"
#     expected_result = f"Bad result {dzialanie}, expected dzialanie: dodawanie, odejmowanie, mnozenie, dzielenie"
#     current_result = kalkulator(liczba_1=1, liczba_2=2, dzialanie=dzialanie)
#     assert expected_result == current_result, f"Expected result: {expected_result} is equal to current " \
#                                               f"result: {current_result}."
# test_funkcji_kalkulator_bledne_dzialanie_str()
#
# def test_funkcji_kalkulator_bledna_instancja_liczby1():
#     liczba_1 = "pop"
#     liczba_2 = 2
#     expected_result = Exception(f"Liczba_1: {liczba_1} lub liczba_2: {liczba_2} nie jest int.")
#     current_result = kalkulator(liczba_1=liczba_1, liczba_2=liczba_2, dzialanie="dzielenie")
#     assert expected_result.args[0] == current_result.args[0], f"Expected result: {expected_result} is equal to current " \
#                                               f"result: {current_result}."
# test_funkcji_kalkulator_bledna_instancja_liczby1()
#
# def test_funkcji_kalkulator_bledna_instancja_liczby2():
#     liczba_1 = 1
#     liczba_2 = "pop"
#     expected_result = Exception(f"Liczba_1: {liczba_1} lub liczba_2: {liczba_2} nie jest int.")
#     current_result = kalkulator(liczba_1=liczba_1, liczba_2=liczba_2, dzialanie="dzielenie")
#     assert expected_result.args[0] == current_result.args[0], f"Expected result: {expected_result} is equal to current " \
#                                               f"result: {current_result}."
# test_funkcji_kalkulator_bledna_instancja_liczby2()
#
# def test_funkcji_kalkulator_bledna_instancja_liczby1_liczba_2():
#     liczba_1 = "pop1"
#     liczba_2 = "pop2"
#     expected_result = Exception(f"Liczba_1: {liczba_1} lub liczba_2: {liczba_2} nie jest int.")
#     current_result = kalkulator(liczba_1=liczba_1, liczba_2=liczba_2, dzialanie="dzielenie")
#     assert expected_result.args[0] == current_result.args[0], f"Expected result: {expected_result} is equal to current " \
#                                               f"result: {current_result}."
# test_funkcji_kalkulator_bledna_instancja_liczby1_liczba_2()
#
# def test_funkcji_kalkulator_bledna_instancja_dzialanie():
#     liczba_1 = 1
#     liczba_2 = 2
#     dzialanie = 50
#     expected_result = Exception(f"Dzialanie: {dzialanie} nie jest str.")
#     current_result = kalkulator(liczba_1=liczba_1, liczba_2=liczba_2, dzialanie=dzialanie)
#     assert expected_result.args[0] == current_result.args[0], f"Expected result: {expected_result} is equal to current " \
#                                               f"result: {current_result}."
# test_funkcji_kalkulator_bledna_instancja_dzialanie()
#
#
# """
# stworz funkcje ktora bedzie przyjmowala liste z roznymi typami zmiennych
# przytypuj liste przy parametrze(tylko lista bedzie brana do funkcji)
# funkcja bedzie tworzyla liste
# ktora bedzie brala tylko inty i wrzuca do nowej listy
# napisz do tej funkcji testy
# """
#
# lista_z_rozymi_typami = [54, 89, 0, "kot", (1.34, 5, "pies"), 100, 999]
#
# def przyjmuje_liste_z_roznymi_typam(lista: list):
#     docelowa_lista = []
#     for el in lista:
#         if isinstance(el, int):
#             docelowa_lista.append(el)
#         if isinstance(el, tuple) or isinstance(el, list):
#             for element in el:
#                 if isinstance(element, int):
#                     docelowa_lista.append(element)
#
#     if len(lista) >= 1 and len(docelowa_lista) < 1:
#         raise Exception(f"Lista przekazana jako parametr: {lista}, nie zawiera intów. Docelowa lista:{docelowa_lista}"
#                         f"jest pusta")
#     return docelowa_lista
#
# print(przyjmuje_liste_z_roznymi_typam(lista=lista_z_rozymi_typami))
#
# def test_przyjmuje_liste_z_roznymi_typam():
#     zmienna = [54, 89, 0, "kot", (1.34, 5, "pies"), 100, 999]
#     expected_result = [54, 89, 0, 5, 100, 999]
#     current_result = przyjmuje_liste_z_roznymi_typam(lista=zmienna)
#     assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result: {current_result}"
#
# test_przyjmuje_liste_z_roznymi_typam()
#
# def test_przyjmuje_liste_z_roznymi_typam_negative():
#     zmienna = [54, 89, 0, "kot", (1.34, 5, "pies"), 100, 999]
#     expected_result = [54, 89, 0, "kot", 100, 999]
#     current_result = przyjmuje_liste_z_roznymi_typam(lista=zmienna)
#     assert expected_result != current_result, f"Expected result: {expected_result} is equal to current result: {current_result}"
#
# test_przyjmuje_liste_z_roznymi_typam_negative()
#
# def test_przyjmuje_liste_z_roznymi_typam_type():
#     zmienna = [54, 89, 0, "kot", (1.34, 5, "pies"), 100, 999]
#     current_result = przyjmuje_liste_z_roznymi_typam(lista=zmienna)
#     assert isinstance(current_result, list), f"Expected result: {current_result} is not instance of list"
#
# test_przyjmuje_liste_z_roznymi_typam_type()
#
# def test_przyjmuje_liste_z_roznymi_typam_wrong_parameter():
#     zmienna = ["kot"]
#     docelowa_lista = []
#     expected_result = f"Lista przekazana jako parametr: {zmienna}, nie zawiera intów. Docelowa lista:{docelowa_lista}jest pusta"
#     current_result = None
#
#     try:
#         przyjmuje_liste_z_roznymi_typam(lista=zmienna)
#     except Exception as ex:
#         current_result = ex.args[0]
#
#     assert current_result is not None
#     assert current_result == expected_result, f"Expected result: {expected_result} is not eqoal to current result: {current_result}."
#
#
# test_przyjmuje_liste_z_roznymi_typam_wrong_parameter()

"""
napisz funkcje ktora bedzie wyciagala kazda wartosc z dicta
sprawdzala czy ta wartosc jest lista
jezeli jest lista to bedzie iterwala i wrzucala do nowej listy elementy z tej listy
jezeli nie jest ma wyrzucic wyjatek bo ten dict przyjmuje listy jako wartosci
napisz test jednostkowy (unit test)
"""
# dict_one = {"foka": [2, 4], "wielblad": [5, 10], "pingwin": [3, 6]}
# dict_negative = {"foka": [2, 4], "wielblad": "tron", "pingwin": [3, 6]}
# dict_puste_listy = {"foka": [], "wielblad": [], "pingwin": []}
# lista = dict.values(dict_one)
# print(lista)
def funkcja_wyciaga_wartosc_z_dicta(dict):
    if not len(dict.values()) >= 1:
        raise Exception(f"Podany dict: {dict} nie zawiera wartosci.")
    pusta_lista = []
    for element in dict.values():
        if isinstance(element, list):
            for elementtt in element:
                pusta_lista.append(elementtt)
        if not isinstance(element, list):
            raise Exception(f"Podany dict: {dict} przyjmuje inny typ jako wartosci.")

    if pusta_lista == []:
        raise Exception(f"Podane wartosci w dict: {dict.values()} sa nieprawidlowe")
    return pusta_lista


# print(funkcja_wyciaga_wartosc_z_dicta(dict=dict_one))
# funkcja_wyciaga_wartosc_z_dicta(dict=dict_negative)
# funkcja_wyciaga_wartosc_z_dicta(dict=dict_puste_listy)
# funkcja_wyciaga_wartosc_z_dicta(dict={})


def test_pozytywny_funkcja_wyciaga_wartosc_z_dicta():
    zmienna = {"foka": [2, 4], "wielblad": [5, 10], "pingwin": [3, 6]}
    expected_result = [2, 4, 5, 10, 3, 6]
    current_result = funkcja_wyciaga_wartosc_z_dicta(dict=zmienna)
    assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result:" \
                                              f" {current_result}."

# test_pozytywny_funkcja_wyciaga_wartosc_z_dicta()

def test_negatywny_funkcja_wyciaga_wartosc_z_dicta():
    zmienna = {"foka": [2, 4], "wielblad": "tron", "pingwin": [3, 6]}
    expected_result = f"Podany dict: {zmienna} przyjmuje inny typ jako wartosci."
    current_result = None
    try:
         funkcja_wyciaga_wartosc_z_dicta(dict=zmienna)
    except Exception as ex:
        current_result = ex.args[0]

    assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result: " \
                                              f"{current_result}."

test_negatywny_funkcja_wyciaga_wartosc_z_dicta()

def test_pustej_listy_funkcja_wyciaga_wartosc_z_dicta():
    zmienna = {"foka": [], "wielblad": [], "pingwin": []}
    expected_result = f"Podane wartosci w dict: {zmienna.values()} sa nieprawidlowe"
    current_result = None
    try:
        funkcja_wyciaga_wartosc_z_dicta(dict=zmienna)
    except Exception as ex:
        current_result = ex.args[0]
    assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result: {current_result}."

test_pustej_listy_funkcja_wyciaga_wartosc_z_dicta()

def test_dict_funkcja_wyciaga_wartosc_z_dicta():
    zmienna = {}
    expected_result = f"Podany dict: {zmienna} nie zawiera wartosci."
    current_result = None
    try:
        funkcja_wyciaga_wartosc_z_dicta(dict=zmienna)
    except Exception as ex:
        current_result = ex.args[0]
    assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result: {current_result}."


test_dict_funkcja_wyciaga_wartosc_z_dicta()


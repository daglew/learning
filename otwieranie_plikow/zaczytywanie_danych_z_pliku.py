# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.com/python/python_file_open.asp
# https://www.w3schools.com/python/python_file_write.asp

import os

# UPRAWNIENIA DO ODCZYTU PLIKOW

write = "'w' - write jest to uprawnienie do zmian w pliku badz modyfikacji"
read = "'r' - read jest to uprawnienie do odczytu pliku bez mozliwosci modyfikacji"

# ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PATH_TO_PLIK_TXT = f"{ROOT_DIR}/otwieranie_plikow/pliki/plik_txt.txt"
# PATH_TO_PLIK_TXT = os.path.join(ROOT_DIR, "otwieranie_plikow/pliki/plik_txt.txt")


# jak otwierac plik tekstowy
# with open(PATH_TO_PLIK_TXT, "r") as plik:
#     z = plik.read()
#     lista_z_z = z.rsplit("\n")
#     print(lista_z_z)

    # Druga metoda usuniecia \n

    # a = plik.readlines()
    # nowa_lista = []
    # for element in a:
    #     usuniecie_n = element.replace("\n", "")
    #     nowa_lista.append(usuniecie_n)
    # print(nowa_lista)

"""
z kodu powzej zrob funkcje zunifikuj ja zeby przyjmowala rozne pliki tekstowe
zwrc liste str podzielona bez \n
i opisz zmiennne tak zeby byly unikatowe i jednoznaczne co sie dzieje
napisz testy

"""
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_TO_PLIK_TXT_1 = f"{ROOT_DIR}/otwieranie_plikow/pliki/plik_txt.txt"
PATH_TO_PLIK_TXT_2 = f"{ROOT_DIR}/otwieranie_plikow/pliki/plik_txt_2.txt"
PATH_TO_PLIK_TXT_3 = f"{ROOT_DIR}/otwieranie_plikow/pliki/plik_txt_3.txt"


def funkcja_zaczytywanie_plikow(PATH):
    if not isinstance(PATH, str):
        raise Exception(f"Podana sciezka: {PATH} nie jest instancja klasy string.")

    try:
        with open(PATH, "r") as plik:
            plik_do_zaczytania = plik.read()
            lista_odseparowana_przecinkami_bez_new_line = plik_do_zaczytania.rsplit("\n")
    except FileNotFoundError:
        raise Exception(f"Brak podanego folderu w sciezce: {PATH}.")

    if len(lista_odseparowana_przecinkami_bez_new_line) < 1 or (len(lista_odseparowana_przecinkami_bez_new_line) == 1 and lista_odseparowana_przecinkami_bez_new_line[0] == ""):
        raise Exception(f"Plik jest pusty: {lista_odseparowana_przecinkami_bez_new_line}, lub zawiera jeden element ktory jest pustym str.")

    return lista_odseparowana_przecinkami_bez_new_line

# a = funkcja_zaczytywanie_plikow(PATH=PATH_TO_PLIK_TXT_2)
# b = funkcja_zaczytywanie_plikow(PATH=PATH_TO_PLIK_TXT_1)
# c = funkcja_zaczytywanie_plikow(PATH="2")
# d = funkcja_zaczytywanie_plikow(PATH=PATH_TO_PLIK_TXT_3)
# print()


"""
pozytywny
negatywny

dlugosc listy dluzsza niz 0
czy zwraca nam liste
"""


def test_pozytywny_funkcja_zaczytywanie_plikow():
    sciezka_1 = f"{ROOT_DIR}/otwieranie_plikow/pliki/plik_txt.txt"
    expected_result = ['1 one', '2 two', '3 three', '4 four', '5 five', '6 six', '7 seven', '8 eight', '9 nine', '10 ten']
    current_result = funkcja_zaczytywanie_plikow(PATH=sciezka_1)
    assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result: {current_result}."

test_pozytywny_funkcja_zaczytywanie_plikow()


def test_negatywny_instancji_sciezki_funkcja_zaczytywanie_plikow():
    bledna_sciezka_jako_lista = [f"{ROOT_DIR}/otwieranie_plikow/pliki/plik_txt.txt"]
    expected_result = f"Podana sciezka: {bledna_sciezka_jako_lista} nie jest instancja klasy string."
    current_result = None
    try:
        funkcja_zaczytywanie_plikow(PATH=bledna_sciezka_jako_lista)
    except Exception as ex:
        current_result = ex.args[0]
    assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result: {current_result}." \

test_negatywny_instancji_sciezki_funkcja_zaczytywanie_plikow()


def test_negatywny_bledna_sciezka_funkcja_zaczytywanie_plikow():
    bledna_sciezka = f"{ROOT_DIR}/otwieranie_plikow/pliki/plik_xdxdxdxd.txt"
    expected_result = f"Brak podanego folderu w sciezce: {bledna_sciezka}."
    current_result = None
    try:
        funkcja_zaczytywanie_plikow(PATH=bledna_sciezka)
    except Exception as ex:
        current_result = ex.args[0]
    assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result: {current_result}." \


test_negatywny_bledna_sciezka_funkcja_zaczytywanie_plikow()

def test_funkcja_zaczytywanie_plikow_pusty_plik():
    pusta_lista = [""]
    pusty_plik_do_zaczytania = f"{ROOT_DIR}/otwieranie_plikow/pliki/plik_txt_3.txt"
    expected_result = f"Plik jest pusty: {pusta_lista}, lub zawiera jeden element ktory jest pustym str."
    current_result = None
    try:
        funkcja_zaczytywanie_plikow(PATH=pusty_plik_do_zaczytania)
    except Exception as ex:
        current_result = ex.args[0]
    assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result: {current_result}." \

test_funkcja_zaczytywanie_plikow_pusty_plik()



"""
napisz test ktory bedzie wykorzystywal funkcje do odczytu pliku 
i sprawdzal czy numer 5 znajduje sie w odczytanym pliku
"""

def test_obecnosci_5_funkcja_zaczytywanie_plikow():
    #expected variabls
    sciezka_1 = f"{ROOT_DIR}/otwieranie_plikow/pliki/plik_txt.txt"
    expected_result = '5 five'
    # current_result = None

    #current
    lista = funkcja_zaczytywanie_plikow(PATH=sciezka_1)
    for element in lista:
        if element == expected_result:
            current_result = element

    #sprawdz expected result i current result
    assert expected_result == current_result, f"Expected result: {expected_result} " \
                                              f"is not equal to current result: {current_result}."
test_obecnosci_5_funkcja_zaczytywanie_plikow()


"""
napisz test ktory sprawdza czy kazdy element w liscie jest str
"""

def test_sprawdzajacy_instancje_elementow_w_funkcja_zaczytywanie_plikow():
    sciezka_1 = f"{ROOT_DIR}/otwieranie_plikow/pliki/plik_txt.txt"
    expected_instance = str

    lista = funkcja_zaczytywanie_plikow(PATH=sciezka_1)

    for element in lista:
        assert isinstance(element, expected_instance), f"Element: {element} is not instance string."

test_sprawdzajacy_instancje_elementow_w_funkcja_zaczytywanie_plikow()
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
PATH_TO_PLIK_TXT_2 = f"{ROOT_DIR}/otwieranie_plikow/pliki/plik_txt.txt_2"
PATH_TO_PLIK_TXT = os.path.join(ROOT_DIR, "otwieranie_plikow/pliki/plik_txt.txt")

def funkcja_zaczytywanie_plikow(PATH):
    if not isinstance(PATH, str):
        raise Exception(f"Podana sciezka: {PATH} nie jest instancja klasy string.")
    try:
        with open(PATH, "r") as plik:
            plik_do_zaczytania = plik.read()
            lista_odseparowana_przecinkami_bez_new_line = plik_do_zaczytania.rsplit("\n")
    except FileNotFoundError:
        raise Exception(f"Brak podanego folderu w sciezce: {PATH}.")

    return lista_odseparowana_przecinkami_bez_new_line


# a = funkcja_zaczytywanie_plikow(PATH=PATH_TO_PLIK_TXT_2)
# b = funkcja_zaczytywanie_plikow(PATH=PATH_TO_PLIK_TXT)
c = funkcja_zaczytywanie_plikow(PATH="2")
print()


"""
dlugosc listy dluzsza niz 0
czy zwraca nam liste

"""

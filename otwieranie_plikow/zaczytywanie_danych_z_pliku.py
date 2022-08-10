# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.com/python/python_file_open.asp
# https://www.w3schools.com/python/python_file_write.asp

import os

# UPRAWNIENIA DO ODCZYTU PLIKOW

write = "'w' - write jest to uprawnienie do zmian w pliku badz modyfikacji"
read = "'r' - read jest to uprawnienie do odczytu pliku bez mozliwosci modyfikacji"

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_TO_PLIK_TXT = f"{ROOT_DIR}/otwieranie_plikow/pliki/plik_txt.txt"
# PATH_TO_PLIK_TXT = os.path.join(ROOT_DIR, "otwieranie_plikow/pliki/plik_txt.txt")


# jak otwierac plik tekstowy
with open(PATH_TO_PLIK_TXT, "r") as plik:
    z = plik.read()
    lista_z_z = z.rsplit("\n")
    print(lista_z_z)

    # Druga metoda usuniecia \n

    # a = plik.readlines()
    # nowa_lista = []
    # for element in a:
    #     usuniecie_n = element.replace("\n", "")
    #     nowa_lista.append(usuniecie_n)
    # print(nowa_lista)



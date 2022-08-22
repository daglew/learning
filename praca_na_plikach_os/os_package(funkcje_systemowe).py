# https://www.geeksforgeeks.org/os-module-python-examples/
import os
import stat

#
# #  zwraca aktualna sciezke pracy CWD
# cwd = os.getcwd()
# print(f"To jest aktualna sciezka pracy: {cwd}.")
#
#
#
# #  zmiana aktualnej sciezki
#
# def current_path():
#     print("Current working directory before")
#     print(os.getcwd())
#     print()
#
#
# current_path()
# os.chdir("../")
# current_path()

# stworzenie pliku

cwd_1 = os.getcwd()
print(cwd_1)
os.mkdir("new_dir")

# usuniecie pliku
os.rmdir(f"{cwd_1}\\new_dir")

# nadawniae uprawnień uprawnien pliku
uprawnienie = stat.S_IRWXU
plik = "D:\\repositories\\learning\\praca_na_plikach_os\\new_txt.txt"
os.chmod(plik, uprawnienie)

# sprawdzenie czy cos jest plikiem
plik_1 = "D:\\repositories\\learning\\praca_na_plikach_os\\new_txt.txt"
sprawdzenie = os.path.isfile(path=plik_1)
print(sprawdzenie)

# sprawdzenie czy cos jest folderem
folder_1 = "D:\\repositories\\learning\\praca_na_plikach_os"
sprawdzenie = os.path.isdir(folder_1)
print(sprawdzenie)

# sprawdzenie czy w ogóle path istnieje
plik_2 = "D:\\repositories\\learning\\praca_na_plikach_os\\new_txt.txt"
sprawdzenie = os.path.exists(path=plik_1)
print(sprawdzenie)

# listowanie plików z folderu
folder_2 = "D:\\repositories\\learning\\praca_na_plikach_os"
lista_plikow = os.listdir(folder_2)
print(lista_plikow)


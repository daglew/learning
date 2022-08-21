# https://www.geeksforgeeks.org/os-module-python-examples/
import os
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

# sprawdzenie czy cos jest plikiem

# sprawdzenie czy cos jest folderem
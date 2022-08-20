# https://www.geeksforgeeks.org/os-module-python-examples/
import os

#  zwraca aktualna sciezke pracy CWD
cwd = os.getcwd()
print(f"To jest aktualna sciezka pracy: {cwd}.")



#  zmiana aktualnej sciezki

def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()


current_path()
os.chdir("../")
current_path()

# dodanie pliku

# usuniecie pliku

# sprawdzenie uprawnien pliku

# sprawdzenie czy cos jest plikiem

# sprawdzenie czy cos jest folderem
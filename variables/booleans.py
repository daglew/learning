moj_boolean = True or False

# sprawdzenie instancji
sprawdzam_instancje = isinstance(moj_boolean, bool)
print(sprawdzam_instancje)

# sprawdzam typ
sprawdzam_typ = type(moj_boolean)
print(sprawdzam_typ)

#  robie f""
przykladowy_fboolean = f"Tutaj wklejam zmienna moj boolean : {moj_boolean}"
print(przykladowy_fboolean)

#  przyrownanie przykladowych intow
print(10 > 1)
print(10 == 1)
print(10 < 1)

#  warunkuje if, else booleans
arbuz = 6
banany = 2

if arbuz > banany:
    print(f"Banany: {banany} jest ich więcej niż arbuzów: {arbuz}")
else:
    print(f"Banany: {banany} jest ich mniej niż arbuzów: {arbuz}")

#  zwraca True
print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#  zwraca False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#  uzywajac metody len(ktora zwraca z ilu znakow sklada sie napis) zwraca 0 lub False

#
def my_function():
  return True

if my_function():
  print("YES!")
else:
  print("NO!")

print()
"""
napisz funkcje sprawdzajaca warunek uzyj if, elif, else
"""
zmienna = 5
def moja_funkcja(zmienna):
    if zmienna <= 6:
        return f"Zmienna: {zmienna} nie jest większa ani równa {6} "
    elif zmienna >= 6:
        return f"Zmienna: {zmienna} nie jest mniejsza ani równa {6} "
    else:
        return f"Zmienna: {zmienna} nie jest większa, mniejsza ani równa {6}. Zmienna moze nie być intem "

wywoluje_funkcje = moja_funkcja(zmienna)
print(wywoluje_funkcje)

"""
zrob liste z roznymi typami danych (str, tuple 2 x, boolean)
napisz funkcje ktoa bedzie sprawdzala instancje kazdego elementu 
jezeli instancja jest prawda to wrzucic do nowej listy if, elif, else
"""

lista_z_roznymi_typami = ["jeden", [], (3, 1.56), True, "kon", (False, 4)]
lista_z_roznymi_typami_2= ["jeden", (3, 1.56), True, "kon", (False, 4)]

def sprawdzenie_instancji_w_liscie(lista):
    pusta_lista_na_typ = []

    for element in lista:
        if isinstance(element, str):
            pusta_lista_na_typ.append(element)
        elif isinstance(element, tuple):
            pusta_lista_na_typ.append(element)
        elif isinstance(element, bool):
            pusta_lista_na_typ.append(element)
        else:
            return f"Brak podenego typu danych element: {element}. Wymagane typy to: str, tuple, boolean"
    return pusta_lista_na_typ


l = sprawdzenie_instancji_w_liscie(lista=lista_z_roznymi_typami)
print(l)
l2 = sprawdzenie_instancji_w_liscie(lista=lista_z_roznymi_typami_2)
print(l2)


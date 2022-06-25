lista = [2, "pol", [1, 2, 3], ("wez", 9, 56, 5.43, True, False, None)]
dikt = {"gg": [4, 8], "kk": [11, 22], "hh": [98, 54]}
pozycja_tupla = lista[3]
pozycja_lista = lista[2]
print(pozycja_tupla)
print(len(pozycja_lista))


for pozycja in pozycja_lista:
    print(f"elementy z pozycja_lista to: {pozycja}")

print("zadanie")

for pozycja in pozycja_tupla:
    print(f"elementy z pozycja_tupla to: {pozycja}")


def printuj_pozycje(podstaw_liste):
    for pozycja in podstaw_liste:
        print(f"elementy z {str(podstaw_liste)} to: {pozycja}")
print()

lista_string = ["rytm", "oto"]

for pozycja in lista_string:
    if pozycja == "rytm":
        print(f"pierwsza pozycja z listy: {pozycja}")
    elif pozycja == "oto":
        print(f"druga pozycja z listy: {pozycja}")
    else:
        print(f"nie znaleziono warunku dla pozycji {pozycja}")


print()
dikt = {"gg": [4, 8], "kk": [11, 22], "hh": [98, 54]}

klucz_kk = dikt["kk"]
print(f"przed: {klucz_kk}")
klucz_kk.append(5)
print(f"po: {klucz_kk}")

for pozycja in klucz_kk:
    if pozycja > 11:
        print(f"pozycja wieksza od 11: {pozycja}")
    elif pozycja <= 11:
        print(f"pozycja mniejsza lub rowna 11: {pozycja}")
    else:
        print(f"pozycja nie spelnia warunkow {pozycja}")

liczba = "4"
liczba_int = int(liczba)
print(liczba_int)
print(type(liczba_int))



x = 3
assert x == 3, "sdfsdfsdsdffsd"


def wyswietl_pozycje(pozycja):
    if len(pozycja) == 7:
        print(f"Pozycja to: {pozycja} dlugosc pozycji to: {len(pozycja)}")
    elif len(pozycja) == 3:
        print(f"Pozycja to: {pozycja} dlugosc pozycji to: {len(pozycja)}")
    else:
        print("nic")


wyswietl_pozycje(pozycja=pozycja_lista)



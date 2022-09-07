# funkcja która nic nie zwraca tylko printuje

def funkcja_ktora_nie_zwraca(lista):
    for element in lista:
        if isinstance(element, int):
            print(f"Iznstancja podanego elementu jest int.")
        elif isinstance(element, list):
            print(f"Iznstancja podanego elementu jest list.")
        elif isinstance(element, str):
            print(f"Iznstancja podanego elementu jest str.")
        else:
            print(f"Nie wyszukano podanej instancji klasy.")


rodzina = ["mama", 78, "tata", "corka", (2, 8), "syn"]

funkcja_ktora_nie_zwraca(lista=rodzina)


# funkcja która przyjmuje dwa parametry i je zwraca
def funkcja_ktora_zwraca_dwa_paraetry(parametr1, parametr2):
    return parametr1, parametr2

xyz = funkcja_ktora_zwraca_dwa_paraetry(parametr1=2, parametr2=3)
print(xyz)

x, y = funkcja_ktora_zwraca_dwa_paraetry(parametr1=2, parametr2=3)
print(x)
print(y)

#  c,d zamieniaja sie wartosciami
c = 5
d = 10

c, d = d, c
print(c, d)


# funkcja która zwraca np dodawanie liczb
def dodawanie(zmienna11, zmienna22):
    return zmienna11+zmienna22

wynik = dodawanie(zmienna11=11, zmienna22=22)
print(wynik)

# dodawanie f""
def dodawanie_f_str(zmienna111, zmienna222):
    wynik1 = zmienna111+zmienna222
    return f"zmienna111 {zmienna111} + zmienna222 {zmienna222} = wynik1 {wynik1} "

wynik1 = dodawanie_f_str(zmienna111=111, zmienna222=222)
print(wynik1)


# funkcja która przyjmuje liste i sprawdza wszystkie typy, następnie zwraca dicta który zawiera jako klucz element a jako wartość typ

lista45 = [23, "ohy", True, (78, "or"), None, 0]

def sprawdza_typy(lista):
    nowy_dict = {}
    for element in lista:
        if isinstance(element, str):
            nowy_dict.update({element: type(element)})
        elif isinstance(element, int):
            nowy_dict.update({element: type(element)})
        elif isinstance(element, tuple):
            nowy_dict.update({element: type(element)})
        elif isinstance(element, bool):
            nowy_dict.update({element: type(element)})
        elif isinstance(element, float):
            nowy_dict.update({element: type(element)})
    return nowy_dict


xx = sprawdza_typy(lista45)
print(xx)

# funkcja która przyjmuje parametr który jest przypisany ale możemy go nadpisać


def miejsce_do_siedzenia(krzesla, stol=1):
    return f"Ilosc stolow: {stol} z iloscia krzesel: {krzesla}"


print(miejsce_do_siedzenia(krzesla=3, stol=2))
print(miejsce_do_siedzenia(krzesla=3))
print(miejsce_do_siedzenia(krzesla=2))




# funkcja która przyjmuje parametry liczba1, liczba2 i mnożnik_liczba_1 (który będzie przypisany jako boolean) jako None,
# następnie funkcja nam zwróci wynik mnożenia ale jak mnożnik nie będzie Nonem to liczba jeden będzie przemnożona przez 4

def mnozenie(liczba1, liczba2, mnoznik_liczba_1: bool=None):
    if mnoznik_liczba_1 is not None:
        liczba_1_x_4 = liczba1 * 4
        wynik = liczba_1_x_4 * liczba2
    else:
        wynik = liczba1*liczba2
    return wynik

print(mnozenie(liczba1=1, liczba2=2))
print(mnozenie(liczba1=1, liczba2=2, mnoznik_liczba_1=True))
print(mnozenie(liczba1=1, liczba2=2, mnoznik_liczba_1=False))


# kombinacja alpejska

def kombinacja_alpejska(zdjecia, ramki=6, albumy=7, ksiazki: bool = None):
    try:
        if ksiazki is None:
            ilosc_miejsc_na_zdj = ramki + albumy
            potrzebne_miejsce = zdjecia - ilosc_miejsc_na_zdj
        else:
           potrzebne_miejsce = zdjecia - ramki
        return potrzebne_miejsce
    except TypeError:
        raise Exception("Ktoras ze zmiennych ma zly typ.")



print(kombinacja_alpejska(zdjecia=345, ramki=45, ksiazki=True))
print(kombinacja_alpejska(zdjecia=345))
print(kombinacja_alpejska(zdjecia=345, ramki=[], ksiazki="sy"))

#  funkcja ktora przyjmuje inty, print kazdego elementu oraz print listy w liscie

lista_int = [2, 4, 6, [5, 10, 15]]
def funkcja_przyjmuje_liste(lista):
    for ele in lista:
        if isinstance(ele, list):
            for elee in ele:
                print(f"element z listy w liscie: {elee}")
        else:
            print(f"element z listy: {ele}")

funkcja_przyjmuje_liste(lista_int)

"""
funkcja ktora przyjmuje liste
lista, a w niej kolejna lista i w niej jeszcze jedna lista
stworz nowa_liste i wszystkie typy danych maja zostac w jedej nowej liscie
bez list w srodku
zwroc nowa liste
"""
pierwotna_lista = [5, 55, ["gocha", 4, 8, [99, 9]]]


def listy_w_liscie_w_liscie(lista):
    nowa_lista = []
    for eleme1 in lista:
        if isinstance(eleme1, list):
            for eleme2 in eleme1:
                if isinstance(eleme2, list):
                    for eleme3 in eleme2:
                        nowa_lista.append(eleme3)
                else:
                    nowa_lista.append(eleme2)
        else:
            nowa_lista.append(eleme1)

    return nowa_lista


p = listy_w_liscie_w_liscie(pierwotna_lista)
print(p)


"""
napisz funkcję która będze zaczytywała dane z najbardziej zagnieźdźonych elementów, sprawdzała ich instancje i wrzucała typ zmiennej do nowej listy
lista = [1, True, 1.23, [1,2,3,4,[1, False, 1.23, "str"]]]  
dict = {"pierwszy": [1, True, 1.23, [1,2,3,4,[1, False, 1.23, "str"]]] }
"""

lista1 = [1, True, 1.23, [1, 2, 3, 4, [1, False, 1.23, "str"]]]
dict1 = {"pierwszy": [1, True, 1.23, [1, 2, 3, 4, [1, False, 1.23, "str"]]]}


def zaczytanie_najbardziej_zagniezdzonych_elementow(zmienna):
    if isinstance(zmienna, list):
        lista = zmienna
    elif isinstance(zmienna, dict):
        lista = zmienna["pierwszy"]
    else:
        raise Exception("Bledny typ danych.")

    nowa_lista = []

    for g in lista:
        if isinstance(g, list):
            for element2 in g:
                if isinstance(element2, list):
                    for ostatni_elemen in element2:
                        nowa_lista.append(type(ostatni_elemen))
    return nowa_lista


typy_lista = zaczytanie_najbardziej_zagniezdzonych_elementow(lista1)
print(typy_lista)

typy_dict = zaczytanie_najbardziej_zagniezdzonych_elementow(dict1)
print(typy_dict)

bledby_typ = zaczytanie_najbardziej_zagniezdzonych_elementow("kk")
print(bledby_typ)

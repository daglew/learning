# x = 2
# y = "3"
# z = []
#
# '''
# Funkcja ktora przyjmuje zmienne i sprawdza czy zmienne sa str? Czy int?
# Jesli zmienna jest stringiem wyprintuj wartosc zmiennej, jesli int wyprintuj wartosc zmiennej. Jesli nie jest str ani
# int, wyprintuj "Błędna zmienna. {zmienna} nie jest to str ani int"
# isinstance
# '''
# def sprawdzam_zmienna(zmienna):
#    if isinstance(zmienna, int):
#        return f"Zmianna {zmienna} jest int."
#    elif isinstance(zmienna, str):
#        return  f"Zmienna {zmienna} jest str."
#    else:
#        return f"Błędna zmienna. Zmienna {zmienna} nie jest str ani int."
#
# spr_x = sprawdzam_zmienna(zmienna=x)
# spr_y = sprawdzam_zmienna(zmienna=y)
# spr_z = sprawdzam_zmienna(zmienna=z)
#
# print(spr_x)
# print(spr_y)
# print(spr_z)
#
# """
# zrob liste = [1,"2",(3), [4,6], {"key":1}]
# zrob funkcje ktora bedzie przyjmowala liste
# nastepnie przeiteruj po tej liscie
# sprawdź typ ziennej
# wyprintuj typ każdej zmiennej
# """
# lista_1 = [1, "2", (), [4, 6], {"key": 1}]
#
# def sprawdz_typ(lista):
#     for element in lista:
#         typ_elementu = type(element)
#         print(typ_elementu)
#
# sprawdz_typ(lista=lista_1)
#
# s = sprawdz_typ(lista=lista_1)
# print(s)
#
#
#
# """
# zrob funkcje ktora bedzie dodawala dwie wartosci i zwracala wynik
# """
#
#
# def dodawanie(zmienna_1, zmienna_2):
#      wynik = zmienna_1+zmienna_2
#      return wynik
#
# dodawanie(zmienna_1=1,zmienna_2=5)
# po=dodawanie(zmienna_1=1,zmienna_2=5)
# print(po)


'''
Stworz funkcje akwarium ktora bedzie przyjmowala trzy zmienne
ilosc_glonow, ilosc_rybek, temperatura_wody.
Jeżeli temperatura wody jest mniejsza niz 21 stopni to umiera jedna rybka i zdychaja dwa glony.
Jeżeli temperatura jest wyzsza niż 21 stopni zwroc liczbe glonow i liczbe rybek.
Jeżeli temperatura rybek jest wyzsza niz 23 stopnie to powstaja dwie dodatkowe rybki i glony pozostaja niezmienne, ma zwrocic liczbe rybek i glonow.
'''


# def akwarium(ilosc_glonow, ilosc_rybek, temperatura_wody):
#     if temperatura_wody in range(0, 21):
#         ilosc_rybek_minus_1 = ilosc_rybek - 1
#         ilosc_glonow_minus_2 = ilosc_glonow - 2
#         return f" Liczba rybek to: {ilosc_rybek_minus_1}. Liczba glonów to: {ilosc_glonow_minus_2}"
#     elif temperatura_wody > 21:
#         return f"Ilość glonów to: {ilosc_glonow}. Ilość rybek to: {ilosc_rybek}"
#     elif temperatura_wody > 23:
#         ilosc_rybek_plus_2 = ilosc_rybek + 2
#         return f"Ilość rybek to: {ilosc_rybek_plus_2}. Ilość glonów to: {ilosc_glonow}."
#     else:
#         return f"Wrong value"


#
#
# ko = akwarium(ilosc_glonow=10, ilosc_rybek=15, temperatura_wody=20)
# print(ko)
#
# koa = akwarium(ilosc_glonow=10, ilosc_rybek=15, temperatura_wody=28)
# print(koa)
#
# kob = akwarium(ilosc_glonow=10, ilosc_rybek=15, temperatura_wody=22)
# print(kob)
#
# koc = akwarium(ilosc_glonow=10, ilosc_rybek=15, temperatura_wody=-1)
# print(koc)


# """
# Stwórz funkcje kalkulator
# funkcja przyjmuje zmienne liczba_1, liczba_2, dzialanie
# jeżeli działanie równa się dodawanie to ma zwrocic wynik dodawania liczb
# powtórz to dla dzielenia, odejmowania i mnozenia
# dodaj elsa jezeli ktos przekaże złe działanie
# """
#
#
# def kalkulator(liczba_1, liczba_2, dzialanie):
#     if dzialanie == "dodawanie":
#         return liczba_2+liczba_1
#     elif dzialanie == "odejmowanie":
#         return liczba_1-liczba_2
#     elif dzialanie == "mnozenie":
#         return liczba_1 * liczba_2
#     elif dzialanie == "dzielenie":
#         return liczba_1 / liczba_2
#     else:
#         return f"Bad result {dzialanie}"
#
#
# dodawanie = kalkulator(liczba_1=4, liczba_2=3, dzialanie="dodawanie")
# print(dodawanie)
# odejmowanie =kalkulator(liczba_1=4, liczba_2=3, dzialanie="odejmowanie")
# print(odejmowanie)
# mnozenie =kalkulator(liczba_1=4, liczba_2=3, dzialanie="mnozenie")
# print(mnozenie)
# dzielenie =kalkulator(liczba_1=4, liczba_2=3, dzialanie="dzielenie")
# print(dzielenie)
# dzielenie1 =kalkulator(liczba_1=4, liczba_2=3, dzialanie="eeeee")
# print(dzielenie1)


"""
Napisz funkcje mnozenie wartosci z listy *2 +5
"""
def mnozenie(lista):
    pusta_lista= []
    for element in lista:
        nowy_elemeny = element*2+5
        pusta_lista.append(nowy_elemeny)
    return pusta_lista

lista8 = [2, 4, 6, 1.23]
trr = mnozenie(lista=lista8)
print(trr)
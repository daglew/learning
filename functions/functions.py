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


# """
# Napisz funkcje mnozenie wartosci z listy *2 +5
# """
# def mnozenie(lista):
#     pusta_lista= []
#     for element in lista:
#         nowy_elemeny = element*2+5
#         pusta_lista.append(nowy_elemeny)
#     return pusta_lista
#
# lista8 = [2, 4, 6, 1.23]
# trr = mnozenie(lista=lista8)
# print(trr)

# """
# stworz funkcje ktora zwraca zmienna
# """
#
# def zwracam_zmienna(zmienna):
#     return zmienna
#
# lop=zwracam_zmienna(zmienna=2)
# print(lop)

# """
# stworz funkcje zakupy ktora przyjmuje dwie zmienne ilosc, koszyk
# jezeli koszyk jest True to zwroc f"ilosc zakupow niose w koszyku"
# jezeli koszyk jest False to ma zwrocic f"ilosc zakupow niose w siatce"
# """
#
# def zakupy(ilosc, koszyk):
#     if koszyk == True:
#         return f"Ilość zakupow: {ilosc}  niose w koszyku"
#     elif koszyk == False:
#         return f"Ilość zakupow: {ilosc}  niose w siatce"
#     else:
#         return f"Ilość zakupow: {ilosc} nie mam siatki ani koszyka"
#
# lidl= zakupy(ilosc=50, koszyk=True)
# lidl_1= zakupy(ilosc=50, koszyk=False)
# lidl_2= zakupy(ilosc=50, koszyk=6)
#
# print(lidl)
# print(lidl_1)
# print(lidl_2)


# """
# stworz funkcje ktora iteruje po liscie i mnozy licze przez siebie i zwraca nowa liste z tymi zmiennymi
# """
#
# def iteruje_po_liscie(lista):
#     pusta=[]
#     for element in lista:
#         element_razy_element = element * element
#         pusta.append(element_razy_element)
#     return pusta
#
# eee= iteruje_po_liscie(lista=[4,5,4,44])
# print(eee)


class Koszyk:
    def __init__(self, warzywa, owoce, nabial):
        self.warzywa = warzywa
        self.owoce = owoce
        self.nabial = nabial

    def wyrzuc_warzywo(self):
        self.warzywa = self.warzywa - 1
        return self.warzywa

    def wyrzuc_owoc(self):
        self.owoce = self.owoce - 1
        return self.owoce

    def wyrzuc_nabial(self):
        self.nabial = self.nabial - 1
        return self.nabial

    def dodaj_warzywo(self):
        self.warzywa = self.warzywa + 1
        return self.warzywa

    def dodaj_owoc(self):
        self.owoce = self.owoce + 1
        return self.owoce

    def dodaj_nabial(self):
        self.nabial = self.nabial + 1_000_000
        return self.nabial

    def sumuj_koszyk(self):
        return self.nabial + self.owoce + self.warzywa


biedra = Koszyk(warzywa=10, owoce=3, nabial=2)

wy_warzywo = biedra.wyrzuc_warzywo()
print(wy_warzywo)

wy_owoc = biedra.wyrzuc_owoc()
print(wy_owoc)

wy_nabial = biedra.wyrzuc_nabial()
print(wy_nabial)

dod_warz = biedra.dodaj_warzywo()
print(dod_warz)

dod_owo = biedra.dodaj_owoc()
print(dod_owo)

dod_nab = biedra.dodaj_nabial()
print(dod_nab)

sumu_kosz = biedra.sumuj_koszyk()
print(sumu_kosz)






# biedra_sumuj_koszyk = biedra.sumuj_koszyk()
# print(biedra_sumuj_koszyk)
#
# wyrzucony_owoc = biedra.wyrzuc_owoc()
# print(wyrzucony_owoc)
# print(biedra.owoce)
#
# biedra_sumuj_koszyk2 = biedra.sumuj_koszyk()
# print(biedra_sumuj_koszyk2)

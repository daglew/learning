# """
# 1. Stworz liste rodzina
# 2. Dodaj do listy członków rodziny
# 3. Zrób pętlę for dla listy rodzina
# 4. Sprawdź w pętli czy poszczególne imiona znajdują się w liście, jeżeli tak to wyprintuj że to imie: ... się znajduje w liście
# 5. W przeciwnym wypadku wypirintuj że się nie znajduje, daj taką informację żeby było jasne co się wydarzyło
# """
# rodzina = ["hubert", "dagmara", "zosia", "jan", "zbyszek", "barbara"]
#
# for czlonek in rodzina:
#     if czlonek == "hubert":
#         print(f"czlonek: {czlonek} równa się 'hubert'")
#     elif czlonek == "dagmara":
#         print(f"czlonek: {czlonek} rowma sie 'dagmara'")
#     elif czlonek == "zosia":
#         print(f"czlonek: {czlonek} rowna sie 'zosia'")
#     elif czlonek == "jan":
#         print(f"czlonek: {czlonek} rowna sie 'jan'")
#     elif czlonek == "zbyszek":
#         print(f"uwaga nieznajomy {czlonek}")
#     else:
#         print(f"Nie znalazłem imienia: {czlonek} do przyrównania")
#
#
# """
# 1. Stwórz dicta dom, gdzie key będzie "rodzina", value będzie lista z członkami, kolejna pozycją będzie "zwierzeta"
#     a value będzie lista gdzie będą zwierzęta w naszym domu
# 2. Wyciągnij z dicta po key te listy, przypisz do zmiennych dom_rodzina, dom_zwierzęta
# 3. Skorzystaj z kodu z pierwszego zadania, wykonaj dwie pętle for i sprawdź czy poszczególne pozycje znajdują się w liście,
#     wyprintuj, jeżeli nie wypirntuj że nie
# """
#
# dom = {
#     "rodzina": ["hubert", "dagmara", "zosia", "jan"],
#     "zwierzeta": ["puszek", "mordzia"]
# }
#
# dom_rodzina = dom["rodzina"]
#
#
# for czlonek in dom_rodzina:
#     if czlonek == "hubert":
#         print(f"czlonek: {czlonek} równa się 'hubert'")
#     elif czlonek == "dagmara":
#         print(f"czlonek: {czlonek} rowma sie 'dagmara'")
#     elif czlonek == "zosia":
#         print(f"czlonek: {czlonek} rowna sie 'zosia'")
#     elif czlonek == "jan":
#         print(f"czlonek: {czlonek} rowna sie 'jan'")
#     elif czlonek == "zbyszek":
#         print(f"uwaga nieznajomy {czlonek}")
#     else:
#         print(f"Nie znalazłem imienia: {czlonek} do przyrównania")
#
# print()
# dom_zwierzeta = dom["zwierzeta"]
#
# for czlonek in dom_zwierzeta:
#     if czlonek == "puszek":
#         print(f"czlonek: {czlonek} równa się 'puszek'")
#     elif czlonek == "mordzia":
#         print(f"czlonek: {czlonek} rowma sie 'mordzia'")
#     else:
#         print(f"Nie znalazłem imienia: {czlonek} do przyrównania")
#
#
#
#
# """
# Stwórz funkcję która ułatwi wykonanie tych pętli
# """
#
#
# def sprawdz_liste(lista):
#     for czlonek in lista:
#         if czlonek == "hubert":
#             print(f"czlonek: {czlonek} równa się 'hubert'")
#         elif czlonek == "dagmara":
#             print(f"czlonek: {czlonek} rowma sie 'dagmara'")
#         elif czlonek == "zosia":
#             print(f"czlonek: {czlonek} rowna sie 'zosia'")
#         elif czlonek == "jan":
#             print(f"czlonek: {czlonek} rowna sie 'jan'")
#         elif czlonek == "zbyszek":
#             print(f"uwaga nieznajomy {czlonek}")
#         elif czlonek == "puszek":
#             print(f"czlonek: {czlonek} równa się 'puszek'")
#         elif czlonek == "mordzia":
#            print(f"czlonek: {czlonek} rowma sie 'mordzia'")
#         else:
#             print(f"Nie znalazłem imienia: {czlonek} do przyrównania")
#
# print("3 ZADANIE")
# sprawdz_liste(lista=dom_zwierzeta)
# print()
# sprawdz_liste(lista=dom_rodzina)
#
# x = ["beata", "kamila", "magda"]
# print()
# sprawdz_liste(lista=x)
#
# """
# Stwórz listę [2,4,6,8,8,10] z listy [1,2,3,4,4,5]
# """
# lista_1 = [1, 2, 3, 4, 4, 5]
# lista_2 = []
# for elememt in lista_1:
#     nowy_element = elememt *2
#     print(nowy_element)
#     lista_2.append(nowy_element)
# print(lista_2)
#
# # list comprehenssion
# lista_3 = [element*2 for element in lista_1]
# lista_4 = [element.capitalize() for element in dom_rodzina]
# lista_5 = [f"element: {element}" for element in dom_rodzina]
# # wykonaj akcje na elemencie dla każdego elementu w liscie_1
#
# print(lista_3)
# print(lista_4)
# print(lista_5)
#
#
# """
# Stwórz zmienną "test" podnieś pierwszą literę
# """
# a = "test"
# print(a.capitalize())
#
# """
# Stwórz zmienną "1" zamień ją na int
# """
# b = 1
# print(f"{b}")
# print(type(b))
#
# """
# Stwórz zmienną "test" podnieś cały wyraz
# """
# c = "test"
# print(c.upper())
#
# """
# Stwórz zmienną "test" zamień t na j
# """
# d = "tekst"
# print(d.replace("t", "j"))
#
# """
# Stwórz zmienną [1, 2, "str", (), [1, 2, 3, [1, 3, 4]], "xd"], wyciągnij listę [1, 2, 3, [1, 3, 4]]
#
# """
# e = [1, 2, "str", (), [1, 2, 3, [1, 3, 4]], "xd"]
# e_1 = e[4]
# print(e_1)
#
# """
# Stwórz zmienną [1, 2, "str", (), [1, 2, 3, [1, 3, 4]], "xd"], wyciągnij listę [1, 3, 4]
# """
# f = [1, 2, "str", (), [1, 2, 3, [1, 3, 4]], "xd"]
# f_1 = f[4]
# f_2 = f_1[3]
# print(f_2)
#
# """
# Stwórz zmienną dict {1:"xd", 2:"3", 3:[5, 6, 7]}
# z klucza 1 podnieś pierwszą literę
# z klucza 2 zmień typ zmiennej na int
# z klucza 3 przeiteruj po liście sprawdź czy 6 w liście jak jest to wyprintuj "Liczba sześć:... jest w liście,
# w przeciwnym wypadku wyprintuj "Nie szukałam tej liczby"
# """
# g = {1: "xd", 2: "3", 3: [5, 6, 7]}
#
# gg = g[1].capitalize()
# print(gg)
#
# klucz_2 = g[2]
# print(klucz_2)
#
# zmienna_int = int(klucz_2)
# print(type(zmienna_int))
#
# klucz_3 = g[3]
# print(klucz_3)
# for element in klucz_3:
#     if element == 6:
#         print(f"Liczba sześć: {element} jest w liście")
#     else:
#         print(f"Nie szukałam tej liczby: {element}")
#
#
# """
# Stwórz 3 listy ["pomidor", "grejfrut", "ziemniak"], ["kalafior", "fasola", "kalarepa"], ["ogorek", "ananas", "jablka"]
# Przeiteruj po pierwszej liście jak znajdzie grejfruta ma wyprintować znalazłem owoc podstaw zmienną,
# w przeciwnym wypadku ma wyprintować znalazłem warzywo i zmienną,
# Pomyśl co można zrobić żeby nie powtarzać kodu przy kolejnych listach
# """
# pierwsza = ["pomidor", "grejfrut", "ziemniak"]
# druga = ["kalafior", "fasola", "kiwi"]
# trzecia = ["ogorek", "ananas", "kapusta"]
#
# def element_in_list(lista):
#     for element in lista:
#         if element == "grejfrut":
#             print(f"znalazlem owoc: {element} ")
#         elif element == "kiwi":
#             print(f"znalazlem owoc: {element} ")
#         elif element == "ananas":
#             print(f"znalazlem owoc: {element} ")
#         else:
#             print(f"znalazlem warzywo: {element}")
#
# element_in_list(lista=pierwsza)


"""
Stworz funkcje dodawanie która będzie przyjmowała dwa parametry liczba_jeden i liczba_dwa
następnie stwórz zmienną gdzie te dwie liczby będą się dodawały
wyprintuj f stringiem "wynik dodawania to: ...."
"""

#
# def dodawanie(liczba_jeden, liczba_dwa):
#     wynik = liczba_jeden+liczba_dwa
#     print(f"wynik dodawania to: {wynik}")
#
#
# dodawanie(liczba_jeden=1, liczba_dwa=2)



"""
Stworz funkcje odejmowanie która
- będzie przyjmowała dwa parametry liczba_jeden i liczba_dwa
- następnie stwórz zmienną gdzie te dwie liczby będą się odejmowały
- jeśli wynik będzie większy lub równy 0 wyprintuj f stringiem "wynik odejmowania to: ...."
- jeśli wynik będzie mniejszy od 0 wyprintuj f stringiem "wynik odejmowania mniejszy niż zero: ...."
"""


# def odejmowanie(liczba_jeden, liczba_dwa):
#     wynik = liczba_jeden-liczba_dwa
#     if wynik >= 0:
#         print(f"wynik odejmowania to: {wynik}")
#     else:
#         print(f"wynik odejmowania mniejszy niż zero: {wynik}")
#
#
#
# odejmowanie(liczba_jeden=1, liczba_dwa=2)

"""
Stworz funkcje kalkulator która
- będzie przyjmowała trzy parametry liczba_jeden i liczba_dwa oraz dzialanie
- jeśli dzialanie będzie równe dodawanie, odejmowanie, dzielenie, mnożenie
- wyprintuj f stringiem "wynik działania:... to: ...."
- w przeciwnym wypadku wyprintuj "nie znam takiego dzialania: ....."
"""

#
# def kalkulator(liczba_jeden, liczba_dwa, dzialanie):
#     if dzialanie == "dodawanie":
#         wynik = liczba_jeden+liczba_dwa
#         print(f"wynik działania:{dzialanie} to: {wynik}")
#
#     elif dzialanie == "odejmowanie":
#         wynik = liczba_jeden - liczba_dwa
#         print(f"wynik działania:{dzialanie} to: {wynik}")
#
#     elif dzialanie == "mnożenie":
#         wynik = liczba_jeden * liczba_dwa
#         print(f"wynik działania:{dzialanie} to: {wynik}")
#
#     elif dzialanie == "dzielenie":
#         wynik = liczba_jeden / liczba_dwa
#         print(f"wynik działania:{dzialanie} to: {wynik}")
#
#     else:
#         print(f"nie znam takiego dzialania:{dzialanie}")
#
#
# kalkulator(liczba_jeden=1, liczba_dwa=2, dzialanie="dzielenie")

"""
Stwórz dwie listy jedną pustą do drugiej dodaj inty, 
- następnie dla każdej pozycji w liście z intami
- przemnóż wartość * 2 i dodaj 1,
- wartość dodaj do pustej listy
- wyprintuj nową listę
"""

lista_1 = []
lista_2 = [3, 4, 6]

for element in lista_2:
    wynik = element*2+1
    lista_1.append(wynik)

print(lista_1)


"""
Stwórz listę [1,1,3,2,2,2,3,4,44,4,5,5,6,66,6,66,6,6,6,6,77777,777,77,77,77],
stwórz pustą listę,
dla każdej pozycji w liście,
sprawdz czy pozcja jest już w liście ,
wrzuc wartości z listy bez powtórek,

Wynik:
[1, 3, 2, 4, 44, 5, 6, 66, 77777, 777, 77]
"""

lista = [1, 1, 3, 2, 2, 2, 3, 4, 44, 4, 5, 5, 6, 66, 6, 66, 6, 6, 6, 6, 77777, 777, 77, 77, 77]
pusta_lista = []

for pozycja in lista:
    if pozycja not in pusta_lista:
        pusta_lista.append(pozycja)
print(pusta_lista)


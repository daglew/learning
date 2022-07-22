# """"
# zrob assercie wykorzystaj try except blok do przechwycenia wyjatku AssertionError
#
# """
#
# zmienna = 3
# druga_zmienna = "dwa"
#
# # printowanie wyjatku
# try:
#     assert zmienna == druga_zmienna, f"Wartosc zmiennej: {zmienna} nie jest wartosci drugiej zmiennej: {druga_zmienna}"
# except AssertionError as ex:
#     print(ex)

# wyrzucanie wyjatku
lista1 = [6]
string1 = "oko"

try:
    assert lista1 == string1, f"Wartosc lista1: {lista1}, nie jest wartosci string1: {string1}"
except AssertionError as hgfgnfnfnnfnfnfn:
    raise Exception(f"Przechwycilam wyjatek hgfgnfnfnnfnfnfn: {hgfgnfnfnnfnfnfn}, przy sprawdaniu asserci wartosci "
                    f"lista1: {lista1}, oraz wartosci string1: {string1}")
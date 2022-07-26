
#
# # funkcja_przyjmuje_list(lista=lista_zmienna)
# lista_z_nowymi_wartosciami, list_comprehension = funkcja_przyjmuje_list(lista=lista_ze_zmiennymi)
# print(lista_z_nowymi_wartosciami)
# print(list_comprehension)
#
# """
# 1. Obórć string aby otrzymać wynik poniżej
# string_1 = "who are you"
# wynik = "you are who"
#
# 2. drugim kroku zrób z tego funkcję która będzie wykorzystywała powyższy kod
#
# 3. Zrób test swojej funkcji
#
# """
#
# string_1 = "who are you"
#
# lista_ze_str = string_1.split()
# obrocona_lista = lista_ze_str[::-1]
#
# # lista_ze_str.reverse()
# print(obrocona_lista)
#
#
# string_1 = "who are you"
#
#
# def obracam_str(zmienna: str):
#     lista_ze_str = zmienna.split()
#     obrocona_lista = lista_ze_str[::-1]
#     lista_na_str = ' '.join([str(elem) for elem in obrocona_lista])
#     return lista_na_str
#
# t = obracam_str(zmienna=string_1)
# t1 = obracam_str(zmienna="kota ma Ala")
#
# print(t)
# print(t1)
#
# def test_obracam_str():
#     str = "Psa ma Zosia"
#     expected_result = "Zosia ma Psa"
#     current_result = obracam_str(zmienna=str)
#     assert expected_result == current_result, f"Expected result: {expected_result} is not equal to current result: {current_result}."
#
# test_obracam_str()
#
# reverse= "ddfed eedcced efefve"
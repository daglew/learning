"""
stwórz zmienną "1"
- wyprintuj typ zmiennej
- przekonweruj zmienną na inta
- wyprintuj
"""
print("zadanie_1")

zmienna_1 = "1"
print(type(zmienna_1))

zmienna_1_intiger = int(zmienna_1)

print(zmienna_1_intiger)
print(type(zmienna_1_intiger))


"""
stwórz zmienną 1
stwórz f stringa który bedzie przyjmował zmienną rezultat: "1 podejście"
wyprintuj tego f stringa
"""
print("zadanie_2")

fortuna = 1
print(f"{fortuna} podejście")

"""
stwórz zmeinna [1, 2, 3, 4]
prziteruj po liście
wyprintuj każdy element z listy
rezultat:
1
2
3
4
"""
print("zadanie_3")

lot = [1, 2, 3, 4]
for element in lot:
    print(f"{element}")

"""
stwórz [1, 2, 3, 4]
przeknowertuj ją na tuple
i wyprintuj
"""
print("zadanie_4")

hop = [1, 2, 3, 4]
hop_tuple = tuple(hop)
print(type(hop_tuple))



""" 
Stwórz dicta = {"tupla" :(1, "3", "5", 2)}
stworz pusta liste 
wyciągnij z dicta tuple po kluczu
przeknowertuj ją na liste
przeitruj po liście
jeśli element jest stringiem
przekonwertuj go na inta
 dodaj do listy pusta lista
 jeśli element jest intem
przekonwertuj go na stringa
 dodaj do listy pusta lista
przekowertuj pusta liste do tulpi
# tuple podstaw pod klucz dicta "tupla"
wyprintuj dicta
rezultat:
dicta = {"tupla" :("1", 3, 5, "2")}
"""
print("zadanie_5")

dik = {"tupla" :(1, "3", "5", 2)}
pusta_lista_1 = []
tupla_z_dicta = dik["tupla"]
print(tupla_z_dicta)

lista_z_dicta = list(tupla_z_dicta)
print(type(lista_z_dicta))

for element in lista_z_dicta:
    if isinstance(element, str):
        element_przekonwertowany_int = int(element)
        # print(type(element_przekonwertowany_int))
        pusta_lista_1.append(element_przekonwertowany_int)
        print(pusta_lista_1)
    elif isinstance(element, int):
        pusta_lista_1_str = str(element)
        # print(type(pusta_lista_1_str))
        pusta_lista_1.append(pusta_lista_1_str)
pusta_lista_1_tuple = tuple(pusta_lista_1)
print(pusta_lista_1_tuple)
dik["tupla"] = pusta_lista_1_tuple
print(dik)
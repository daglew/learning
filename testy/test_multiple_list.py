"""
Create a list = [1, 3, 4, 5, 6]
Create empty_list = []

please add to empty_list every element from first list x2
result empty_list = [2, 6, 8, 10, 12]
"""
list_ = [1, 3, 4, 5, 6]
empty_list = []

for element in list_:
    nowy_element = element * 2
    empty_list.append(nowy_element)

print(empty_list)




"""

Create a function which will take parameter list an multiple element x2 (use code from first task) 
and return list

"""


def multiple_list(lista):
    empty_list = []
    for element in lista:
        nowy_element = element * 2
        empty_list.append(nowy_element)
    return empty_list


lista_2 = multiple_list(lista=[12, 45, 98])
print(lista_2)

lista = [22, 44, 55, 66, 77]
## LIST COMPREHHENSSION ##
nowa_lista = [element*2 for element in lista]
print(nowa_lista)

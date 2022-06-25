 # Lists
 ## metoda len()

```python
this_list = ["sil", 56, 89.5, True, "uuu"]
second_list = [189, 8, (), "por", 56.7]

 ## metoda len()
# powoduje sprawdzenie dlugosci listy
print(len(this_list), len(second_list))
```

```python
# podmiana wartosci w liscie
this_list = ["sil", 56, 89.5, True, "uuu"]
print(this_list[0])
this_list[0] = "try"
print(this_list)

second_list = [189, 8, (), "por", 56.7]
second_list[1] = "lol"
print(second_list[1])

```

```python
# metoda clear() czysci liste
this_list = ["sil", 56, 89.5, True, "uuu"]
this_list.clear()
print(this_list)

```

```python
# metoda remove() usuwa wartosc pozycji z listy odejmowanie
this_list = ["sil", 56, 89.5, True, "uuu"]
this_list.remove("uuu")
print(this_list)

```

```python
# metoda pop() usuwa element o indeksie np.3
this_list = ["sil", 56, 89.5, True, "uuu"]
this_list.pop(3)
print(this_list)

```
```python
# iteracja=powtorzenie
this_list = ["sil", 56, 89.5, True, "uuu"]

# petla for przejdzie po kazdym elemencie w this_list nastepnie wyprintuje go
for element in this_list:
    print(element)

```
```python
# petla if
this_list = ["sil", 56, 89.5, True, "uuu"]

if this_list == ["sil", 56, 89.5, True, "uuu"]:
    print(f"Prawda ta lista się równa weż zmienną i ją wyprintuj: {this_list}")
else:
    print(f"Ta lista: {this_list} nie jest prawdą ")

print(type(this_list))


a = 12
b = 9
if b > a:
    print(f"wartosc b: {b} jest wieksze od wartosci a: {a} ")
else:
    print(f"wartosc b: {b} nie jest wieksza od wartosci a: {a}")


if b < a and b < 8:
    print(f"wartosc b: {b} jest wieksze od wartosci a: {a} ")
elif b == 9:
    print(f"wartosc b: {b} jest rowna 9 ")
else:
    print(f"wartosc b: {b} nie jest wieksza od wartosci a: {a}")


try:
    assert b>a, f"B:{b} nie jest wieksze od {a}"
except AssertionError:
    raise Exception(f"wartosc b:{b}, nie jest wieksze od {a}")

lista_do_iteracji = [1, 2, 3, 45, 6, 6, 7, 77, (), "strig", True, None, False]

nowa_lista = []

for element in lista_do_iteracji:
    nowa_lista.append(element)

print(nowa_lista)



```
```python
# metoda apppend() dodaje do listy element
lista_do_iteracji_2 = [1, 2, 3, 45, 6, 6, 7, 77]
nowa_lista_2 = []

for element in lista_do_iteracji_2:
    nowy_element = element * 2
    nowa_lista_2.append(nowy_element)

print(nowa_lista_2)
```

```python
prawda = False
falsz = False

if prawda == True:
    print(f"prawda: {prawda}")
else:
    print(f"falsz: {prawda}")

if prawda != True:
    print(f"zmienna prawda: {prawda} != True")
else:
    print(f"zmienna prawda: {prawda} == True")


```
```python
# list comprehenssion
dom = {
    "rodzina": ["hubert", "dagmara", "zosia", "jan"],
    "zwierzeta": ["puszek", "mordzia"]
}
dom_rodzina = dom["rodzina"]
lista_1 = [1, 2, 3, 4, 4, 5]

lista_3 = [element*2 for element in lista_1]
lista_4 = [element.capitalize() for element in dom_rodzina]
lista_5 = [f"element: {element}" for element in dom_rodzina]

```


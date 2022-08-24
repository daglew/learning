# https://www.w3schools.com/python/python_json.asp
import json

# to jest json
import os

x = '{"name": "John", "age": 30, "city": "New York"}'

# zaczytanie jsona
zaczytanie_x = json.loads(x)

imie = zaczytanie_x['name']
wiek = zaczytanie_x['age']
miasto = zaczytanie_x['city']
print(f"wyciagnelam z jsona imie: {imie}, wiek: {wiek} oraz miasto: {miasto}.")

# konwertowanie do jsona
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# tworzenie jsona
json_1 = json.dumps(x)
print()
x.update({"country": "USA"})
json_2 = json.dumps(x)
print()
json_3 = json.loads(json_2)
print()


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

g = json.dumps(x)
f = json.loads(g)
print()
billy= f['children'][1]
mpg = f['cars'][0]['mpg']

"""
otwarcie pliku, zaczytanie danych i wyciagniecie numeru telefonu
"""
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

plik = f"{ROOT_DIR}/jsons/sample2.json"
with open(f"{ROOT_DIR}/jsons/sample2.json", "r") as aaa:
  zaczytanie_aa = json.load(aaa)
  number_phone = zaczytanie_aa['phoneNumbers'][0]['number']
  print()





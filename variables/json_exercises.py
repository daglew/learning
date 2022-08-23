# https://www.w3schools.com/python/python_json.asp
import json

# to jest json
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
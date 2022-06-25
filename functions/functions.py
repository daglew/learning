x = 2
y = "3"
z = []

'''
Funkcja ktora przyjmuje zmienne i sprawdza czy zmienne sa str? Czy int?
Jesli zmienna jest stringiem wyprintuj wartosc zmiennej, jesli int wyprintuj wartosc zmiennej. Jesli nie jest str ani 
int, wyprintuj "Błędna zmienna. {zmienna} nie jest to str ani int"
isinstance
'''
def sprawdzam_zmienna(zmienna):
   if isinstance(zmienna, int):
       return f"Zmianna {zmienna} jest int."
   elif isinstance(zmienna, str):
       return  f"Zmienna {zmienna} jest str."
   else:
       return f"Błędna zmienna. Zmienna {zmienna} nie jest str ani int."

spr_x = sprawdzam_zmienna(zmienna=x)
spr_y = sprawdzam_zmienna(zmienna=y)
spr_z = sprawdzam_zmienna(zmienna=z)

print(spr_x)
print(spr_y)
print(spr_z)

"""
zrob liste = [1,"2",(3), [4,6], {"key":1}]
zrob funkcje ktora bedzie przyjmowala liste
nastepnie przeiteruj po tej liscie 
sprawdź typ ziennej
wyprintuj typ każdej zmiennej
"""
lista_1 = [1, "2", (), [4, 6], {"key": 1}]

def sprawdz_typ(lista):
    for element in lista:
        typ_elementu = type(element)
        print(typ_elementu)

sprawdz_typ(lista=lista_1)

s = sprawdz_typ(lista=lista_1)
print(s)
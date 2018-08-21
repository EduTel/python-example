#https://docs.python.org/3/tutorial/datastructures.html
#gtx-body
for target_list in "hola":
    print(target_list)

class C_humano:
    edad=0
    def __init__(self,_edad):
        self.edad = _edad
    def imprimir(self):
        print(self.edad)
humano =C_humano(1)
humano.imprimir()

print ("jeje","123")
x = "jeje","123"
print (x)

lista= ["a","b","c","c"]
buscar = "c";
if buscar in  lista:
    print(lista.index(buscar))

lista = [1,2,3,4,5]
lista.insert(1,3)
print(lista)


listone = [1,2,3]
listtwo = [4,5,6]
mergedlist = []
mergedlist.extend(listone)
mergedlist.extend(listtwo)
mergedlist.pop()
mergedlist.remove(1)
print(mergedlist)

#zip
"""
    mix to list
"""
a = "ABCD"
b = "12345"

p_1 = list(a)
p_2 = list(b)
print(str(p_2[0]))

concat = "";
contador = 0;
if len(p_1)>len(p_2) :
    for f in p_1:
        if len(p_2)>contador:
            concat +=str(p_2[contador])
        concat += str(f)
        contador= contador+1
else:
    for f in p_2:
        if len(p_1)>contador:
            concat +=str(p_1[contador])
        concat += str(f)
        contador= contador+1

print(concat)


for target_list in "hola":
    print(target_list)

class C_humano:
    edad=0
    def __init__(self,_edad):
        self.edad = _edad
    def imprimir(self):
        print(self.edad)
humano =C_humano(1)
humano.imprimir()

print ("jeje","123")
x = "jeje","123"
print (x)

lista= ["a","b","c","c"]
buscar = "c";
if buscar in  lista:
    print(lista.index(buscar))

lista = [1,2,3,4,5]
lista.insert(1,3)
print(lista)


listone = [1,2,3]
listtwo = [4,5,6]
mergedlist = []
mergedlist.extend(listone)
mergedlist.extend(listtwo)
mergedlist.pop()
mergedlist.remove(1)
mergedlist.reverse()
print(mergedlist)


# diccionarios
diccionario = {
    "hola1": [1,2,3],
    "hola2": "two item",
    "hola3": (4,5,6)                              
}
diccionario2 = diccionario.copy()
print("hola1" in diccionario.keys() )
print(diccionario.items())
print(diccionario.keys())
print(diccionario.values())
print(diccionario.pop("hola2",-1))
print(diccionario)
del diccionario["hola3"]
print(diccionario)
diccionario.clear()
print(diccionario2)



#filter
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for x in adults:
  print(x)


#operador ternario
if (1 > 50):
    r =1
else:
    r =0
print(r)

#reduce
cadena = ("h","o","l","a")
def concat(data,cadena):

reducido = functools.reduce(concat, cadena)
print(reducido)


#import 
import itertools

#sort
#!/usr/bin/python3
# vowels list
vowels = [1,6,3,4,5,2]
letter = ["a","d","b","c"]
# sort the vowels
answer = sorted(vowels, reverse=True)
letter = sorted(letter, reverse=True)
print(answer)
print(letter)




#******************************test

#zip
"""
    mix to list
"""



def mergeStrings(a, b):
    p_1 = list(a)
    p_2 = list(b)
    concat = "";
    contador = 0;
    if len(p_1)>len(p_2) :
        for f in p_1:
            if len(p_1) > contador:
                concat += str(p_1[contador])
            if len(p_2)>contador:
                concat +=str(p_2[contador])
            contador= contador+1
    else:
        for f in p_2:
            if len(p_1)>contador:
                concat +=str(p_1[contador])
            concat += str(f)
            contador= contador+1
    return concat
a = "abc"
b = "def"


#a = "zbxnsjdns"
#b = "idowdk"


print(mergeStrings(a,b))

"""
    find difference max
"""


_params = [1,2,6,4]

_params = [5,10,8,7,6,5]

_diference = [2]
_temporal = []
_contador = 0
for item_p in _params:
    _temporal.insert(len(_temporal), item_p)
    if _contador==0:
        _contador += 1
        continue
    _contador +=1
    for item_t in _temporal:
        if item_p > item_t:
            #print("====",item_p,">",item_t,"=====")
            _diference.insert(len(_diference), (item_p-item_t))
        #else:
            #print("error")
if len(_diference)==0:
    return -1
else:
    return max(_diference)













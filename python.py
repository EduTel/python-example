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
print(mergedlist)






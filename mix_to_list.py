#zip
"""
    mix to list
"""


def mergeStrings(a, b):
    p_1 = list(a)
    p_2 = list(b)
    concat = ""
    contador = 0
    if len(p_1) > len(p_2):
        for f in p_1:
            if len(p_1) > contador:
                concat += str(p_1[contador])
            if len(p_2) > contador:
                concat += str(p_2[contador])
            contador = contador+1
    else:
        for f in p_2:
            if len(p_1) > contador:
                concat += str(p_1[contador])
            concat += str(f)
            contador = contador+1
    return concat


a = "abc"
b = "def"


#a = "zbxnsjdns"
#b = "idowdk"


print(mergeStrings(a, b))

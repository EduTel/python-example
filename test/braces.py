"""
    braces
"""
##all braces must be close (),[],{}
braces_close = ("}", ")", "]")
braces_close = braces_close[:-1]
print(braces_close)


def f_braces(values):
    #return str([len(values), type(values), values])
    _yes_no = []
    braces_opens = ("{", "(", "[")
    braces_close = ("}", ")", "]")
    _true = "YES"
    _false = "NO"
    for string_item in values:
        print("interacion cadena==========================================", string_item)
        _braces_opened = []
        _contador = 0
        if string_item[-1] in braces_opens:
            _yes_no.insert(len(_yes_no), (_false))
            break
        for item_b in string_item:
            _contador+=1
            print("interacion letras-----------", item_b)
            if item_b in braces_opens:
                _braces_opened.insert(len(_braces_opened), (item_b))
            elif item_b in braces_close:
                if(len(_braces_opened) == 0):
                    _yes_no.insert(len(_yes_no), (_false))
                    break
                else:
                    print("=======ultimo open=====", _braces_opened[-1])
                    print("_braces_opened", _braces_opened)
                    if(_braces_opened[-1] == "{"):
                        _braces_opened = _braces_opened[:-1]
                        if(item_b != "}"):
                            _yes_no.insert(len(_yes_no), (_false))
                            break
                    elif(_braces_opened[-1] == "["):
                        _braces_opened = _braces_opened[:-1]
                        if(item_b != "]"):
                            _yes_no.insert(len(_yes_no), (_false))
                            break
                    elif(_braces_opened[-1] == "("):
                        _braces_opened = _braces_opened[:-1]
                        if(item_b != ")"):
                            _yes_no.insert(len(_yes_no), (_false))
                            break
            else:
                print("Error")
            if _contador == len(string_item):
                _yes_no.insert(len(_yes_no), (_true))
            #print("*********_braces_opened", _braces_opened)
            #print("termino==========================================")
    return _yes_no
s_braces = ["()"]
#s_braces = ["()", "[]"]
#s_braces = ["{}[]()", "{[}]"]
s_braces = [
    "}][}}(}][))]",
    "[](){()}",
    "()",
    "({}([][]))[]()",
    "{)[](}]}]}))}(())(",
    "([[)"
]
print(f_braces(s_braces))


[2,<class  'list'>, ['{}[]()', '{[}]']]
[2, <class 'list'>, ['{}[]()', '{[}]']]

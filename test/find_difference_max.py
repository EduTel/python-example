
"""
    find difference max
"""


_params = [1, 2, 6, 4]

_params = [5, 10, 8, 7, 6, 5]

_diference = [2]
_temporal = []
_contador = 0
for item_p in _params:
    _temporal.insert(len(_temporal), item_p)
    if _contador == 0:
        _contador += 1
        continue
    _contador += 1
    for item_t in _temporal:
        if item_p > item_t:
            #print("====",item_p,">",item_t,"=====")
            _diference.insert(len(_diference), (item_p-item_t))
        #else:
            #print("error")
if len(_diference) == 0:
    return -1
else:
    return max(_diference)

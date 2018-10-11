"""
    sample query
"""
#menores o igual  a el elemento


def counts(nums, maxes):
    #print("nums:", nums)
    #print("maxes:", maxes)
    _nums = []
    for maxes_item in maxes:
        #print("maxes_item==========================================", maxes_item)
        _contador = 0
        _cuantos = 0
        for item_nums in nums:
            #print("item_nums====================", item_nums)
            if(maxes_item >= item_nums):
                #print("==", maxes_item, ">", item_nums)
                _cuantos += 1
                #print("_cuantos: ", _cuantos)
            _contador += 1
            if(_contador == len(nums)):
                #print("===================terminado")
                _nums.insert(len(_nums), (_cuantos))
    #print("==========================================terminado")
    return _nums
nums = [2, 10, 5, 4, 8]
maxes = [3, 1, 7, 8]


print(counts(nums, maxes))

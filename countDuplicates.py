#countDuplicates
def countDuplicates(numbers):
    print("numbers:", numbers)
    numbers_c = numbers;
    number=0
    for item_number in numbers_c:
        print("================item_number================")
        print(numbers_c.count(item_number))
        val = numbers_c.count(item_number)
        if(val>1):
            print(val,">",1)
            number+=1
            while item_number in numbers_c: numbers_c.remove(item_number)
    #print("number", number)
    return number


numbers = [1, 3, 1, 4, 5, 6, 3, 2]

print(countDuplicates(numbers))


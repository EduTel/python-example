#countDuplicates
def countDuplicates(numbers):
    numbers_c = numbers
    number=0
    for item_number in numbers_c:
        val = numbers_c.count(item_number)
        if(val>1):
            number+=1
            while item_number in numbers_c: numbers_c.remove(item_number)
    return number


numbers = [1, 3, 1, 4, 5, 6, 3, 2]

print(countDuplicates(numbers))


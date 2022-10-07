# How can you make this more scalable and reusable later?
import math

def find_armstrong_numbers(numbers):
    results =[]
    # string_num = str(numbers)
    # total = 0
    for item in numbers:
        holder = str(item)
        if len(holder) == 1:
            results.append(item)
            pass
        elif len(holder) == 2:
            temp1 = int(holder[0])
            temp2 = int(holder[1])
            summ = math.pow(temp1, 2) + math.pow(temp2, 2)
            if summ == item:
                results.append(item)
            #instructions
            pass
        elif len(holder) == 3:
            tem1 = int(holder[0])
            tem2 = int(holder[1])
            tem3 = int(holder[2])
            sum3 = math.pow(tem1, 3) + math.pow(tem2, 3) + math.pow(tem3, 3)
            if sum3 == item:
                results.append(item)
    return results
    # results = []
    # comparison = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
    # for num in numbers:
    #     print(num)
    #     if num in comparison:
    #         results.append(num)
    # return results

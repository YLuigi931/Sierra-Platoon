# How can you make this more scalable and reusable later?
import math

def find_armstrong_numbers(numbers):
    results = []
    
    for item in numbers:
        holder = str(item)
        if len(holder) == 1:
            results.append(item)
            
        elif len(holder) == 2:
            temp1 = int(holder[0])
            temp2 = int(holder[1])
            summ = math.pow(temp1, 2) + math.pow(temp2, 2)
            if summ == item:
                results.append(item)
            
        elif len(holder) == 3:
            tem1 = int(holder[0])
            tem2 = int(holder[1])
            tem3 = int(holder[2])
            sum3 = math.pow(tem1, 3) + math.pow(tem2, 3) + math.pow(tem3, 3)
            if sum3 == item:
                results.append(item)
    return results

# use list comprehension to shorten
# lambda
# functools.reduce

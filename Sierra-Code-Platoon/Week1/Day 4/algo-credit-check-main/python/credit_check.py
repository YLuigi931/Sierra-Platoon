import math

def to_string(mynum):
    return str(mynum)

def credit_check(str):
    result = []
    for item in str:
        result.append(int(item))
    # print(f"starting array{result}")    
    result.reverse()
    # print(f"after reversing array {result}")
    for index in range(len(result)):
        # multiply the 2nd index by 2
        if index % 2 != 0:
            result[index] *= 2
            current = result[index]
            word1 = to_string(current)
            # if it has 2 digit numbers, get the sum of left and right digit
            if(len(word1) == 2):
                summ = int(word1[0]) + int(word1[1])
                result[index] = summ
    total = sum(result)
    return(("The number is valid!", "The number is invalid!") [total % 10 != 0])
    # print(result)
    
    # array1 = []
    # array2 = []
    # array3 = []
    
    # for c in str:
    #     array1.append(int(c))
    # array1.reverse()
    
    # for index, num in enumerate(array1):
    #     if(index % 2) == 0:
    #         array2.append(num)
    #     else:
    #         array2.append(num * 2)
    
    # for n in array2:
    #     if n > 9:
    #         mystr = to_string(n)
    #         the_num = int(mystr[0]) + int(mystr[1])
    #         array3.append(the_num)
    #     else:
    #         array3.append(n)
    
    # summ = lambda x, y: x + y, array3
    # if summ % 10 == 0:
    #     return "The number is valid!"
    # else:
    #     return "The number is invalid!"

# credit_check('5541808923795240')

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"


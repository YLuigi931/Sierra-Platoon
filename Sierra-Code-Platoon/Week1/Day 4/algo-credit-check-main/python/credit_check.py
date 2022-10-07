def credit_check(str):
    
    array1 = []
    
    for c in str:
        array1.append(int(c))
        
    array1.reverse()
    print(f"Before {array1}")
    for num in array1:
        if(array1.index(num) % 2) != 0:
            array1[array1.index(num)] *= 2
    
    
    print(array1) 

credit_check('5541808923795240')

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"


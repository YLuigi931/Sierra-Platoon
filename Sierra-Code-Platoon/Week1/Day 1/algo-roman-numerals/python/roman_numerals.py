def to_roman(num):
    # write your code here!
    result = ''
    sample = num
    while(sample != 0):  
        # 1 digit number
        if(len(str(sample)) == 1):
            if(sample >= 9):
                sample -= 9
                result += 'IX'
            elif(sample >= 5):
                sample -= 5
                result += 'V'
            elif(sample >= 4):
                sample -= 4
                result += 'IV'
            else:
                sample -= 1
                result += 'I'
        elif(len(str(sample)) == 2):
            if(sample >= 90):
                sample -= 90
                result += 'XC'
            elif(sample >= 50 ):
                sample -= 50
                result += 'L'
            elif(sample >= 40):
                sample -= 40
                result += 'XL'
            else:
                sample -= 10
                result += 'X'
        elif(len(str(sample)) == 3):
            if(sample >= 900):
                sample -= 900
                result += 'CM'
            elif(sample >= 500):
                sample -= 500
                result += 'D'
            elif(sample >= 400):
                sample -= 400
                result += 'CD'
            else:
                sample -= 100
                result += 'c'
        elif(len(str(sample)) == 4):
            if(sample >= 9000):
                sample -= 9000
                result += 'I̅X̅'
            elif(sample >= 5000):
                sample -= 5000
                result += 'V̅'
            elif(sample >= 4000):
                sample -= 4000
                result += 'I̅V̅'
            else:
                sample -= 1000
                result += 'M'
                
    return result   

print(to_roman(4444))        
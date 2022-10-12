def caesar_cipher(string, shift_amount):
    
    result = ""
    
    for item in string:
        
        number = ord(item)
        print(f'{number}')
        summ = number + shift_amount
        print(f'sum of number and shift = {summ}')
        if(summ > 122): # lowercase z
            print('first got trigger')
            diff = summ - 122
            diff += 97
            print(diff)
            result += chr(diff)
        elif(summ < 97): # lowercase a
            print('second got trigger')
            diff = 97 - summ
            diff = 122 - diff
            print(diff)
            result += chr(diff)
        elif(summ > 90): # uppercase Z
            print('third got trigger')
            diff = summ - 90
            diff += 65
            print(diff)
            result += chr(diff)
        elif(summ < 65): # uppercase A
            print('fourth got trigger') 
            diff = 65 - summ
            diff = 90 - diff
            print(diff)
            result += chr(diff)
        else:
            print('last got trigger')
            if item == " ":
                result += " "
            else:
                result += chr(summ)
            
    return result
# "Boy! What a string!", -5) == "Wjt! Rcvo v nomdib!"
print(caesar_cipher("B", -5))
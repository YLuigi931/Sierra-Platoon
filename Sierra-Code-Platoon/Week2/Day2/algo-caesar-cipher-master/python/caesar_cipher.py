def caesar_cipher(string, shift_amount):
    # result = ""
    
    # for item in string:
        
    #     number = ord(item)
    #     print(f'{number}')
    #     summ = number + shift_amount
    #     print(f'sum of number and shift = {summ}')
    #     if(summ > 122): # lowercase z
    #         print('first got trigger')
    #         diff = summ - 122
    #         diff += 97
    #         print(diff)
    #         result += chr(diff)
    #     elif(summ < 97): # lowercase a
    #         print('second got trigger')
    #         diff = 97 - summ
    #         diff = 122 - diff
    #         print(diff)
    #         result += chr(diff)
    #     elif(summ > 90): # uppercase Z
    #         print('third got trigger')
    #         diff = summ - 90
    #         diff += 65
    #         print(diff)
    #         result += chr(diff)
    #     elif(summ < 65): # uppercase A
    #         print('fourth got trigger') 
    #         diff = 65 - summ
    #         diff = 90 - diff
    #         print(diff)
    #         result += chr(diff)
    #     else:
    #         print('last got trigger')
    #         if item == " ":
    #             result += " "
    #         else:
    #             result += chr(summ)
            
    # return result
    # https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
    exception = [' ', '!', '.', '0','1','2','3','4','5','6','7','8','9']
    result = ""
    # transverse the plain text
    for i in range(len(string)):
        char = string[i]
        # space
        if char in exception:
            result += char
        # Encrypt uppercase characters in plain text
        
        elif(char.isupper()):
            summ = ord(char) + shift_amount-65
            # print(f'\nAfter adding {char} convert to ascii ({ord(char)}) {ord(char)} + {shift_amount-65} = {summ}')
            # print(f'current mod (sum % 26): {summ % 26}')
            # print(f'final number after the shift {summ % 26 + 65} {chr(summ % 26 + 65)}')
            result += chr((ord(char) + shift_amount-65) % 26 + 65)
            
        # Encrypt lowercase characters in plain text
        else:
            summ = ord(char) + shift_amount-97
            # print(f'\nAfter adding {char} convert to ascii ({ord(char)}) {ord(char)} + {shift_amount-97} = {summ}')
            # print(f'current mod (sum % 26): {summ % 26}')
            # print(f'final number after the shift {summ % 26 + 97} {chr(summ % 26 + 97)}\n')
            result += chr((ord(char) + shift_amount - 97) % 26 + 97)
    return result
# "Boy! What a string!", -5) == "Wjt! Rcvo v nomdib!"
# print(caesar_cipher("Boy! What a string!", -5))
# "Hello zach168! Yes here.", 5) == "Mjqqt efhm168! Djx mjwj."
# print(caesar_cipher("Hello zach168! Yes here.", 5))
roman_numerals = {
    1000 : 'M',
    900 : 'CM',
    500 :  'D',
    400 : 'CD',
    100 : 'C',
    90 : 'XC',
    50 : 'L',
    40 : 'XL',
    10 : 'X',
    9 : 'IX',
    5 : 'V',
    4 : 'IV',
    1 : 'I'
}

def roman_int(user_choice):
    number = str(user_choice)
    index = 0
    result = ''
    
    while(index < len(number)):
        
        for k , v in roman_numerals:
            if number.startswith(str(k), index, len(number)):
                result += v
                index += 1
                break
            
    return result




print(roman_int(10))
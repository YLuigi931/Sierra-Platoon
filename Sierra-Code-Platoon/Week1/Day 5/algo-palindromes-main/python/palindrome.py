from pkg_resources import empty_provider
import re

def palindrome(word):
   
    temp_word1 = str(word).lower().replace(" ", "")
    out = re.sub("[,-.]","", temp_word1)
    
    return out == out[::-1]
    
    
    
# print(palindrome("NOva is here"))
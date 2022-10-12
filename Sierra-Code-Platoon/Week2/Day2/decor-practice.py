def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)
    
greet(shout)
greet(whisper)
'''
==================
output:
HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
hi, i am created by a function passed as an argument.
==================

In the above example, the greet function takes another 
function as a parameter(shout and whisper in this case). 
The function passed as an argument is then called inside the function greet.
'''
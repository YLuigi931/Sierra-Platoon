def factorial(x):
    if x == 1:
        return x
    else:
        return x + factorial(x-1)

def palindrome(string):
	pass

def bottles(num):
    if num == 0:
        print('no more bottles')
        return
    else:
        print(f'{num} bottles of beer on the wall')
        return bottles(num-1)

def roman_num(num):
	pass

bottles(10)
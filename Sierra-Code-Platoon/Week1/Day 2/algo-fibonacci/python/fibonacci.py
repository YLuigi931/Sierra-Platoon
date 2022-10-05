def fibonacci(n):
  current = 0
  holder = 0 
  previous = 1
  
  while(n != 0):
    holder = current
    current += previous
    previous = holder
    n -= 1
  
  return current
  
#print(fibonacci(7))
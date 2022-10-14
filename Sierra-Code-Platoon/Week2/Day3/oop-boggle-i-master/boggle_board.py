import random
import string

class BoggleBoard:
  
  def __init__(self):
    self.blank = BoggleBoard.blank(self)
  
  def shake(self):
    # print(''.join(random.choices(string.ascii_uppercase, k=4)))
    lst = []
    for item in range(4):
      random_letters = ''.join(random.choices(string.ascii_uppercase, k=4))
      lst.append(random_letters)
    
    print(lst)
    
    
    # for index in range(4):
      
  def blank(self):
    blank = '```python\n   ____\n   ____\n   ____\n   ____\n```'
    print(blank)
    
    
test1 = BoggleBoard()
test1.shake()

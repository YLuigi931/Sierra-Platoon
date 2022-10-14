import random
import string



class BoggleBoard:
  
  def __init__(self):
    blank = self.blank()
    self.map = blank
    print(self.map)
  
  def shake(self):
    # print(''.join(random.choices(string.ascii_uppercase, k=4)))
    erase = self.blank()
    self.map = erase
    
    lst = []
    for item in range(4):
      random_letters = ''.join(random.choices(string.ascii_uppercase, k=4))
      lst.append(random_letters)
    
    # print(lst)
    # print(self.map)
    
    temp_map = self.map
    # print(temp_map)
    for index in range(4):
      # print(f'{lst[index]}')
      # print(temp_map)
      x = temp_map.replace("____", f'{lst[index]}', 1)
      temp_map = x
    
    self.map = temp_map
    print(temp_map)
      
  def blank(self):
    blank = '```python\n   ____\n   ____\n   ____\n   ____\n```'
    # print(blank)
    return blank


# ============== MAIN Method =====================

test1 = BoggleBoard()
test1.shake()
test1.shake()
test1.shake()


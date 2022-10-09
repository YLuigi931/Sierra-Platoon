import numpy as np
from operator import itemgetter

def char_count(str):
  # Your code here
  temp = str.replace(" ", "")
  container = {}
  for letter in temp:
    if letter not in container:
      container[letter] = 1
    else:
      container[letter] += 1  
  
  lst1 = container.items()
  res = [[i for i, j in lst1],[j for i, j in lst1]]
  temp1 = np.array(list(zip(res[0], res[1])))
  temp2 = sorted(temp1.tolist(), key=itemgetter(0), reverse=False)
  mr = np.array(temp2)
  temp3 = sorted(mr.tolist(), key=itemgetter(1), reverse=True)
  
  for bag in temp3:
    holder = bag[1]
    bag[1] = int(holder)
    
  return temp3
  # print(temp3)
  
# char_count("an apple a day will keep the doctor away")
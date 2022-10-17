class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self) -> None:
    self.lst = []
    self.size = 0
  
  
  def push(self, data): # add to end
    # write your code to add data following LIFO and return the Stack
    self.lst.append(data)
    self.size += 1
    return

  def pop(self): # remove from begin
    # write your code to removes the data following LIFO and return the Stack
    self.lst.pop(0)
    self.size -= 1
    return

  def size(self): # return the length of stack
    # write your code that returns the size of the Stack
    return self.size

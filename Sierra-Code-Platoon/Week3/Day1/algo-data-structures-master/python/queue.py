class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self):
    self.lst = []
    self.length = 0
    
  
  def enqueue(self, data):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.lst.insert(0, data)
    self.length +=1
    return

  def dequeue(self):
    # write your code to removes the data to the Queue following FIFO and return the Queue
    self.length -= 1
    return self.lst.pop(0)

  def size(self):
    # write your code that returns the size of the Queue
    return self.length

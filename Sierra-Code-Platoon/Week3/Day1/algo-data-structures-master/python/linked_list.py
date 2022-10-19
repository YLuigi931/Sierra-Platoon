
# ----- Node ------



class Node:
  # store your DATA and NEXT values here
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkList:
    # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, data):
    self.singly = Node(data)
    self.size = 0
    
  def add(self, data):# add to the right of linkedlist
    # write your code to ADD an element to the Linked List
    pointer = self.singly
    more = Node(data)
    while(pointer.data != 0):
      if pointer.next == None:
        pointer.next = more
        return
      pointer = pointer.next

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    pointer = self.singly
    # if self.size == 0: return # handles empty
    if pointer.data == data:  # current node is the data
      pointer = pointer.next
      self.size -= 1
      self.singly = pointer
      return
    else:
      while(pointer.data != 0):
        # print(pointer.data)
        if pointer.next == None: return
        elif(pointer.next.data == data):
          
          pointer.next = pointer.next.next
          self.size -= 1
          
          return
        else:
          pointer = pointer.next

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    copy = self.singly
    if copy.data == element_to_get: return copy.data
    while(copy != None):
        if copy.next == None: return
        elif(copy.next.data == element_to_get):
          return copy.next.data
        else:
          copy = copy.next
    return
    
  def print_lst(self):
    pointer = self.head
    result = 'Head==> '
    
    while(pointer != 0):
      result += f'[{pointer.data}]==> '
      if pointer.next == None:
        result += 'None'
        print(result)
        return
      pointer = pointer.next
    return


test1 = LinkList(10)
test1.print_lst()
print('add 20')
test1.add(20)
test1.print_lst()
print('add 21, 22, 23')
test1.add(21)
test1.add(22)
test1.add(23)
test1.print_lst()
print(f'get function have been envoke {test1.get(10)}')
print('remove 21')
test1.remove(21)
test1.print_lst()
print('remove 20')
test1.remove(20)
test1.print_lst()
print('remove 23')
test1.remove(23)
test1.print_lst()
test1.remove(10)
test1.print_lst()


class Node:
  # store your DATA and LEFT and RIGHT values here
  def __init__(self):
    self.data = None
    self.left = None
    self.right = None

class Bst:
  def __init__(self):
    self.head = Node()
    self.parent = self.head

  def insert(self, value):
    #This is where you will insert a value into the Binary Search Tree
    pointer = self.head
    if pointer.data == None: # case were head has no value
      pointer.data = value
    else:
      more_node = Node()
      more_node.data = value 
      while(pointer.data != None):
        
        if value > pointer.data and pointer.right == None:
            pointer.right = more_node
            return
        elif value < pointer.data and pointer.left == None:
            pointer.left = more_node
            return
        elif(value > pointer.data):
          pointer = pointer.right
        elif(value < pointer.data):
          pointer = pointer.left
                 
    return
  
  def contains(self,value):
        tree = self.parent
        bool = self.helper(tree, value)
        return bool
    
  def helper(self, tree, value):
      pointer = tree
      found = False
      if pointer is None:
          return found
      if pointer.data == value:
          found = True
          return found
      if(value < pointer.data):
          bool_left = self.helper(pointer.left, value)
          if bool_left == True:
            found = bool_left
            return found
      if(value > pointer.data):
          bool_right = self.helper(pointer.right, value)
          if bool_right == True:
            found = bool_right
            return found
      return found
      

  def remove(self, value):
    # this is where you will remove a value from the BST
    if self.contains(value) == False: return
    
    
    pass
        
  
# def print_tree(tree):
#   pass



test1 = Bst()
test1.insert(10)
test1.insert(7)
print(test1.head.left.data)
test1.insert(12) 
print(f'{test1.head.right.data}')
test1.insert(11)
print(f'{test1.head.right.left.data}')
print(test1.contains(11)) 

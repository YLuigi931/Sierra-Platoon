class HashTable:
  def __init__(self, number_of_buckets):
    self.number_of_buckets = number_of_buckets
    self.table = [None] * self.number_of_buckets
    

  def hash(self, value):
    # here is where you'll turn your 'value' into a hash value that will return the index of your table to insert value
    # IMPORTANT: Think about how you'd store values into the same index
    result = 0
    for letter in value:
      result += ord(letter)
    result = result // self.number_of_buckets
    return result

  def set(self, value):
    # here is where you'll perform your logic to insert the value into your table
    # you'll also call your hash method here to get the index where you'll store the value
    index = self.hash(value)
    if index > self.number_of_buckets:
      index = index % self.number_of_buckets

    if self.table[index] == None:
      self.table[index] = [value]
    else:
      self.table[index].append(value)

  def get(self, value):
    # here is where you'll retreive your value from the hash table
    # IMPORTANT: Think about how you'd retreive a value that from an index that has multiple values
    if self.has_key(value):
      print('value found')
      return value
    else:
      print('value not found')
      return
    

  def has_key(self, value):
    # here is where you'll return a True or False value if there is a value stored at a specific index in your HashTable
    index = self.hash(value)
    if index > self.number_of_buckets:
      index = index % self.number_of_buckets

    if self.table[index] == None:
      return False
    if value in self.table[index]:
      return True
    return False

my_hash_table = HashTable(35)
# print(my_hash_table.number_of_buckets)
# print(my_hash_table.table)
my_hash_table.set('tom')
my_hash_table.set('mot')
my_hash_table.set('moaiusydfhasdlfashdfljaskldhfljasdfhasjdfhasdlfjklast')
print(my_hash_table.table)
my_hash_table.get('mort')
my_hash_table.get('tom')
# print(my_hash_table.has_key('tom'))
# print(my_hash_table.has_key('otm'))
# print(my_hash_table.has_key('Tom'))
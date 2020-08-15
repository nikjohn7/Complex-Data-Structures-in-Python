from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [LinkedList() for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for i in list_at_array:
      if i[0]==key:
        i[0]=value
        return
    list_at_array.insert(payload)
    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    list_at_index = self.array[array_index]

    if not list_at_index:
      return None
    for i in list_at_index:
      if i[0] == key:
        return i[1]
    return None

    

blossom = HashMap(len(flower_definitions))
for ele in flower_definitions:
  blossom.assign(ele[0],ele[1])

print(blossom.retrieve('daisy'))

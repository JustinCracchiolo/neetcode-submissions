class MyHashSet:

    def __init__(self):
        self.arr = [] #keeps order 
        self.value_index_map = {} #constant lookup time 
        

    def add(self, key: int) -> None:
        self.arr.append(key)
        self.value_index_map[key] = len(self.arr) - 1 
        

    def remove(self, key: int) -> None:
        if key in self.value_index_map:
            #take the last value in arr give it's index to key 
            self.value_index_map[self.arr[-1]] = self.value_index_map[key]
            #remove element
            self.arr.pop(self.value_index_map[key])
            del self.value_index_map[key]

    def contains(self, key: int) -> bool:
        return key in self.value_index_map


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
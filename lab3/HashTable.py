class HashTable:
    # size should be a prime number
    def __init__(self, size):
        self.items = [list() for _ in range(size)]
        self.size = size

    def hash(self, element):
        sum_ascii = 0
        for char in element:
            sum_ascii += ord(char) - ord('0')
        return sum_ascii % self.size

    def add(self, element):
        if self.contains(element):
            return self.getPosition(element)
        self.items[self.hash(element)].append(element)
        return self.getPosition(element)

    def contains(self, elemnet):
        return elemnet in self.items[self.hash(elemnet)]

    def __str__(self) -> str:
        result = "Symbol Table - hash table with separate chaining\n"
        for i in range(self.size):
            result = result + str(i) + "->" + str(self.items[i]) + "\n"
        return result

    def getPosition(self, element):
        pos_in_list = self.hash(element)
        if element not in self.items[pos_in_list]:
            return None
        else:
            listIndex = 0
            for item in self.items[pos_in_list]:
                if item != element:
                    listIndex += 1
                else:
                    break
            return pos_in_list, listIndex

from HashTable import HashTable


class SymbolTable:

    def __init__(self, size):
        self.hashTable = HashTable(size)

    def add(self, element):
        return self.hashTable.add(element)

    def contains(self, elemnet):
        return elemnet in self.hashTable.items[self.hashTable.hash(elemnet)]

    def __str__(self) -> str:
        return self.hashTable.__str__()

    def getPosition(self, element):
        return self.hashTable.getPosition(element)

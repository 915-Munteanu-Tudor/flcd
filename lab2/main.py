from SymbolTable import SymbolTable

if __name__ == '__main__':
    ST = SymbolTable(23)
    print(ST.add("ad"))
    # print(ST.add("bc"))
    print(ST.getPosition("bc"))
    print(ST.add("bc"))
    print(ST.__str__())

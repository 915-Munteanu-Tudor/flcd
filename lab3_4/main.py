from Console import Console
from Scanner import Scanner
from SymbolTable import SymbolTable

if __name__ == '__main__':
    # ST = SymbolTable(23)
    # print(ST.add("ad"))
    # # print(ST.add("bc"))
    # print(ST.getPosition("bc"))
    # print(ST.add("bc"))
    # print(ST.__str__())

    # console = Console('in_files/FA.in')
    # console.run()

    scanner = Scanner('in_files/program3.txt')
    try:
        scanner.scan()
        scanner.write_pif_and_st_files()
    except ValueError as e:
        print(e)

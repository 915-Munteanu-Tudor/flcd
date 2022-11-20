import re
from tabulate import tabulate
from FiniteAutomata import FiniteAutomata
from SymbolTable import SymbolTable


class Scanner:
    def __init__(self, program_file):
        self.programFile = program_file
        self.constantsST = SymbolTable(47)
        self.identifiersST = SymbolTable(47)
        self.fa_identifiers = FiniteAutomata()
        self.fa_constants = FiniteAutomata()
        self.tokens = []
        self.pif = []
        self.read_token_file()

    def read_token_file(self):
        f = open('in_files/token.in', "r")
        self.tokens = f.read().split()
        f.close()

        self.fa_identifiers.readFromFile('in_files/fa_identifiers.in')
        self.fa_constants.readFromFile('in_files/fa_constants.in')

    def write_pif_and_st_files(self):
        f = open('out_files/PIF.out', 'w')
        f.write(tabulate(self.pif))
        f.close()

        f = open('out_files/ST_constants.out', 'w')
        f.write(self.constantsST.__str__())
        f.close()

        f = open('out_files/ST_identifiers.out', 'w')
        f.write(self.identifiersST.__str__())
        f.close()

    def is_identifier(self, token):
        return re.match('^[a-zA-Z]+[a-zA-Z0-9_]*$', token) is not None \
               and re.match(r'^(?!.*True|False).*$', token) is not None

    def is_constant(self, token):
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$|^(True|False)$', token) is not None

    def tokenize(self, string):
        line_data = re.split('("[^a-zA-Z0-9\"\']")|([^a-zA-Z0-9\"\'])', string)
        elements = [el for el in line_data if el is not None and el != '' and el != ' ']
        for i in range(len(elements) - 1):
            if elements[i] == "=" and elements[i + 1] == "=":
                elements[i] += elements[i + 1]
                elements.remove(elements[i + 1])
            elif elements[i] == "<" and elements[i + 1] == "=":
                elements[i] += elements[i + 1]
                elements.remove(elements[i + 1])
            elif elements[i] == ">" and elements[i + 1] == "=":
                elements[i] += elements[i + 1]
                elements.remove(elements[i + 1])
            elif elements[i] == "!" and elements[i + 1] == "=":
                elements[i] += elements[i + 1]
                elements.remove(elements[i + 1])
        return elements

    def scan(self):
        i = 0
        f = open(self.programFile, "r")
        for line in f:
            line = line.split()
            i += 1
            for part in line:
                elements = self.tokenize(part)
                for elem in elements:
                    if elem in self.tokens:
                        self.pif.append((elem, -1))
                    # elif self.is_identifier(elem):
                    elif self.fa_identifiers.isAccepted(elem):
                        self.identifiersST.add(elem)
                        self.pif.append(('identifier', self.identifiersST.getPosition(elem)))
                    # elif self.is_constant(elem):
                    elif self.fa_constants.isAccepted(elem):
                        self.constantsST.add(elem)
                        self.pif.append(('constant', self.constantsST.getPosition(elem)))
                    else:
                        raise ValueError('Lexical Error at line: ' + str(i) + ', at token: ' + elem)
        f.close()

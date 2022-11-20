class FiniteAutomata:

    def __init__(self):
        self.Q = []
        self.E = []
        self.q0 = []
        self.F = []
        self.S = {}

    def readFromFile(self, file_in):
        with open(file_in) as file:
            self.Q = file.readline().strip().split(' ')[2:]
            self.E = file.readline().strip().split(' ')[2:]
            self.q0 = file.readline().strip().split(' ')[2:][0]
            self.F = file.readline().strip().split(' ')[2:]
            file.readline()

            for line in file:
                src = line.strip().split('=')[0].strip().split(',')[0]
                route = line.strip().split('=')[0].strip().split(',')[1]
                dst = line.strip().split('=')[1].strip()

                if (src, route) in self.S.keys():
                    self.S[(src, route)].append(dst)
                else:
                    self.S[(src, route)] = [dst]

    def isDfa(self):
        for k in self.S.keys():
            if len(self.S[k]) > 1:
                return False
        return True

    def isAccepted(self, seq):
        if self.isDfa():
            current = self.q0
            for symbol in seq:
                if (current, symbol) in self.S.keys():
                    current = self.S[(current, symbol)][0]
                else:
                    return False
            return current in self.F
        return "Not a DFA"

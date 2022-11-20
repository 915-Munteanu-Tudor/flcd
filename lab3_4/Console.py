from FiniteAutomata import FiniteAutomata


class Console:

    def __init__(self, file_in):
        self.fa = FiniteAutomata()
        self.fa.readFromFile(file_in)
        self.cmds = {'1': self.showStates, '2': self.showAlphabet, '3': self.showTransitions,
                     '4': self.showInitialState,
                     '5': self.showFinalStates, '6': self.checkDFA}

    def showStates(self):
        print(self.fa.Q)

    def showAlphabet(self):
        print(self.fa.E)

    def showTransitions(self):
        print(self.fa.S)

    def showInitialState(self):
        print(self.fa.q0)

    def showFinalStates(self):
        print(self.fa.F)

    def checkDFA(self):
        seq = input()
        print(self.fa.isAccepted(seq))

    @staticmethod
    def displayMenu():
        print("1.Display states")
        print("2.Display alphabet")
        print("3.Display transitions")
        print("4.Display initial states")
        print("5.Display final state")
        print("6.Check accepted sequence for DFA")
        print("7.Exit")

    def run(self):
        condition = False
        while not condition:
            self.displayMenu()
            print(">>")
            cmd = input()
            if cmd in self.cmds.keys():
                self.cmds[cmd]()
                print("\n")
            elif cmd == "7":
                condition = True
            else:
                print("This command doesn't exist\n")

from ops import *

class VM:
    def loadProgram(self, program):
        for i,ins in enumerate(program):
            self.pMem[i]=ins

    def push(self, x):
        self.sp+=1
        self.stack[self.sp] = x

    def pop(self):
        x = self.stack[self.sp]
        self.sp-=1
        return x

    def run(self):

        while not self.halt:
            if self.pMem[self.pc] == opcodes['IPUSH']:
                self.pc+=1
                self.push(self.pMem[self.pc])

            elif self.pMem[self.pc] == opcodes['IPOP']:
                self.pop()

            elif self.pMem[self.pc] == opcodes['IADD']:
                a = self.pop()
                b = self.pop()
                self.push(a+b)

            elif self.pMem[self.pc] == opcodes['IPRINT']:
                print self.pop()

            elif self.pMem[self.pc] == opcodes['HALT']:
                self.halt = 1

            self.pc+=1

    def __init__(self):
        self.stack = [None]*(1024*4)
        self.pMem = [None]*(1024*4)
        self.rwMem = [None]*(1024*4)

        self.halt = 0

        self.pc = 0
        self.sp = 0

program = [0x01, 0x02, 0x01, 0x03, 0x11, 0xe1, 0xff]

vm = VM()

vm.loadProgram(program)
vm.run()
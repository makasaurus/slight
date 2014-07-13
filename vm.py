from ops import *
from lex import *


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

    def peek(self):
        x = self.stack[self.sp]
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

            elif self.pMem[self.pc] == opcodes['ISUB']:
                a = self.pop()
                b = self.pop()
                print b,a
                self.push(b-a)

            elif self.pMem[self.pc] == opcodes['IPRINT']:
                print self.peek()

            elif self.pMem[self.pc] == opcodes['HALT']:
                self.halt = 1

            else:
                print 'Unrecognized instruction, halting.'
                self.halt = 1

            self.pc+=1
            # print self.pc, '@', self.sp, self.stack


    def __init__(self):
        self.stack = [None]*(1024*4)
        self.pMem = [None]*(1024*4)
        self.rwMem = [None]*(1024*4)

        self.halt = 0

        self.pc = 0
        self.sp = 0

lex = Lex()


source = "ipush 2\n" \
         "ipush 4\n" \
         "iadd\n" \
         "iprint\n" \
         "halt"

program =  lex.encode(source)

vm = VM()

vm.loadProgram(program)
vm.run()
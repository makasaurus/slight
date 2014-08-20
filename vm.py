from ops import *
from lex import *


class VM:
    def loadProgram(self, program):
        for i,ins in enumerate(program):
            self.pMem[i]=ins

    def start(self):
        source = open("program.sl", 'r').read()
        program = self.lex.encode(source)
        self.loadProgram(program)
        self.run()

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
        if self.debug:
            for item in self.pMem[0:20]:
                if item in codes:
                    print "(%s | %d)"%(codes[item], item),
                else:
                    print item,

        while not self.halt:

            if self.debug:
                print self.stack[0:20]
                if self.pMem[self.pc] in codes:
                    print "PC %d: %s"%(self.pc, codes[self.pMem[self.pc]])
                else:
                    print "PC %d:"(self.pc)

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

            elif self.pMem[self.pc] == opcodes['IMUL']:
                a = self.pop()
                b = self.pop()
                self.push(a*b)

            elif self.pMem[self.pc] == opcodes['IDIV']:
                a = self.pop()
                b = self.pop()
                self.push(int(b/a))

            elif self.pMem[self.pc] == opcodes['AND']:
                a = self.pop()
                b = self.pop()
                self.push(1 if a and b else 0)

            elif self.pMem[self.pc] == opcodes['OR']:
                a = self.pop()
                b = self.pop()
                self.push(1 if a or b else 0)

            elif self.pMem[self.pc] == opcodes['NOT']:
                a = self.pop()
                self.push(0 if a else 1)

            elif self.pMem[self.pc] == opcodes['CMP']:
                a = self.pop()
                b = self.pop()
                if b < a: self.push(-1)
                elif b  == a: self.push(0)
                else: self.push(1)

            elif self.pMem[self.pc] == opcodes['IPRINT']:
                if self.debug:
                    print ">>>",
                print self.peek()

            elif self.pMem[self.pc] == opcodes['JMP']:
                labelName = self.pMem[self.pc+1]
                targetAddress = self.lex.label[labelName] -1

                self.pc = targetAddress

            elif self.pMem[self.pc] == opcodes['CALL']:
                self.pc+=1
                functionNameEncoded = self.pMem[self.pc]
                self.pc+=1
                argCount = int(self.pMem[self.pc])

                #TODO don't use this array, but allocate space in system memory
                swap = []

                for i in xrange(0, argCount):
                    swap += [self.pop()]

                self.push(self.pc)

                for item in reversed(swap):
                    self.push(item)

                self.pc = self.lex.function[functionNameEncoded]-1

            elif self.pMem[self.pc] == opcodes['RET']:
                self.pc+=1
                argCount = int(self.pMem[self.pc])

                swap = []

                for i in xrange(0, argCount):
                    swap += [self.pop()]

                returnAddress = self.pop()

                for item in reversed(swap):
                    self.push(item)

                self.pc = returnAddress

            elif self.pMem[self.pc] == opcodes['VAR']:
                self.pc += 1
                varName = self.pMem[self.pc]

                self.pc += 1
                value = int(self.pMem[self.pc])

                # find an empty address to store var to
                # hopefully we find a quicker way of doing this, O(n) isn't very cool
                # TODO make this quicker

                varAddress = 0
                addressFound = False
                hit = False

                while not addressFound:
                    for varDict in self.vars:
                        if varAddress in varDict.values():
                          varAddress += 1
                          hit = True
                          break;
                    if not hit:
                        addressFound = True

                # store var address in last dict
                self.vars[len(self.vars)-1][varName] = varAddress

                self.rwMem[varAddress] = value

                print self.rwMem[0:10]

            elif self.pMem[self.pc] == opcodes['NOP']:
                #do nothing, but need to make python think we are doing something
                nothing = True

            elif self.pMem[self.pc] == opcodes['HALT']:
                self.halt = 1

            else:
                print 'Unrecognized instruction, halting.'
                self.halt = 1

            self.pc+=1
            #print self.pc, '@', self.sp, self.stack


    def __init__(self):
        self.stack = [None]*(1024*4)
        self.pMem = [None]*(1024*4)
        self.rwMem = [None]*(1024*4)

        self.halt = 0

        self.pc = 0
        self.sp = 0

        self.lex = Lex()

        # vars will be stored in a set of dicts, one per scope level
        self.vars = []

        self.debug = False

vm = VM()
vm.start()
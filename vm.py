from ops import *
from lex import *
import random
import console


"""

VM is the virtual machine that runs the code.

There are many 'cheat' points, i.e. memory stores any size string in a single memory space. Also, there is a good
amount of 'magic' points as well, i.e. where an int is converted to a string using python methods. The goal is to remove
all of the 'cheating magic'.

"""
class VM:
    def loadProgram(self, program):
        for i,ins in enumerate(program):
            self.pMem[i]=ins

    def start(self):
        source = open("program.sl", 'r').read()
        program = self.lex.encode(source)
        self.loadProgram(program)
        print
        self.run()

    def push(self, x):
        self.sp += 1
        self.stack[self.sp] = x

    def pop(self):
        x = self.stack[self.sp]
        self.stack[self.sp] = None
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
                for cell in self.stack[0:10]: print "%s\t"%(str(cell)),
                print
                if self.pMem[self.pc] in codes:
                    print "PC %d: %s"%(self.pc, codes[self.pMem[self.pc]])
                else:
                    print "PC %d"%(self.pc)
                print "SP %d"%(self.sp)


            # TODO find some more elegant way of switching self.pMem[self.pc], too much going on here

            if self.pMem[self.pc] == opcodes['IPUSH']:
                self._ipush()

            elif self.pMem[self.pc] == opcodes['IPOP']:
                self._ipop()

            elif self.pMem[self.pc] == opcodes['ICPY']:
                self._icpy()

            elif self.pMem[self.pc] == opcodes['IADD']:
                self._iadd()

            elif self.pMem[self.pc] == opcodes['ISUB']:
                self._isub()

            elif self.pMem[self.pc] == opcodes['IMUL']:
                self._imul()

            elif self.pMem[self.pc] == opcodes['IDIV']:
                self._idiv()

            elif self.pMem[self.pc] == opcodes['AND']:
                self._and()

            elif self.pMem[self.pc] == opcodes['OR']:
                self._or()

            elif self.pMem[self.pc] == opcodes['NOT']:
                self._not()

            elif self.pMem[self.pc] == opcodes['CMP']:
                self._cmp()

            elif self.pMem[self.pc] == opcodes['JE']:
                self._je()

            elif self.pMem[self.pc] == opcodes['JNE']:
                self._jne()

            elif self.pMem[self.pc] == opcodes['IPRINT']:
                self._iprint()

            elif self.pMem[self.pc] == opcodes['CPRINT']:
                self._cprint()

            elif self.pMem[self.pc] == opcodes['CDELETE']:
                self._cdelete()

            elif self.pMem[self.pc] == opcodes['IIN']:
                self._iin()

            elif self.pMem[self.pc] == opcodes['CIN']:
                self._cin()

            elif self.pMem[self.pc] == opcodes['JMP']:
                self._jmp()

            elif self.pMem[self.pc] == opcodes['CALL']:
                self._call()

            elif self.pMem[self.pc] == opcodes['RET']:
                self._ret()

            elif self.pMem[self.pc] == opcodes['IVAR']:
                self._ivar()

            elif self.pMem[self.pc] == opcodes['IVARST']:
                self._ivarst()

            elif self.pMem[self.pc] == opcodes['IGET']:
                self._iget()

            elif self.pMem[self.pc] == opcodes['ISET']:
                self._iset()

            elif self.pMem[self.pc] == opcodes['SPGET']:
                self._spget()

            elif self.pMem[self.pc] == opcodes['SPSET']:
                self._spset()

            elif self.pMem[self.pc] == opcodes['NOP']:
                self._nop()

            elif self.pMem[self.pc] == opcodes['HALT']:
                self._halt()

            else:
                print 'Unrecognized instruction, halting.'
                print '\tins: %s' % self.pMem[self.pc]
                self.halt = 1

            self.pc+=1
            #print self.pc, '@', self.sp, self.stack
            #print self.vars

    def _ipush(self):
        self.pc += 1
        self.push(self.pMem[self.pc])

    def _ipop(self):
        self.pop()

    def _icpy(self):
        self.push(self.peek())

    def _iadd(self):
        a = self.pop()
        b = self.pop()
        self.push(a + b)

    def _isub(self):
        a = self.pop()
        b = self.pop()
        print b, a
        self.push(b - a)

    def _imul(self):
        a = self.pop()
        b = self.pop()
        self.push(a * b)

    def _idiv(self):
        a = self.pop()
        b = self.pop()
        self.push(int(b / a))

    def _and(self):
        a = self.pop()
        b = self.pop()
        self.push(1 if a and b else 0)

    def _or(self):
        a = self.pop()
        b = self.pop()
        self.push(1 if a or b else 0)

    def _not(self):
        a = self.pop()
        self.push(0 if a else 1)

        # TODO change to ICMP as it should only compare ints

    def _cmp(self):
        a = self.pop()
        b = self.pop()
        if b < a:
            self.push(-1)
        elif b == a:
            self.push(0)
        else:
            self.push(1)

    def _je(self):
        a = self.pop()
        b = self.pop()
        if a == b:
            labelName = self.pMem[self.pc + 1]
            targetAddress = self.lex.label[labelName] - 1

            self.pc = targetAddress
        else:
            self.pc += 1

    def _jne(self):
        a = self.pop()
        b = self.pop()
        if a != b:
            labelName = self.pMem[self.pc + 1]
            targetAddress = self.lex.label[labelName] - 1

            self.pc = targetAddress
        else:
            self.pc += 1

    def _iprint(self):
        if self.debug:
            print ">>>",
        print self.peek()

    def _cprint(self):
        if self.debug:
            print ">>>",
        self.console.update_display(chr(self.peek()))

    def _cdelete(self):
        self.console.delete_char()

    def _iin(self):
        inputInt = input()
        self.push(inputInt)

    def _cin(self):
        inputOrd = ord(self.console.getchar())
        self.push(inputOrd)

    def _jmp(self):
        labelName = self.pMem[self.pc + 1]
        targetAddress = self.lex.label[labelName] - 1
        self.pc = targetAddress

    def _call(self):
        self.pc += 1
        functionNameEncoded = self.pMem[self.pc]
        self.pc += 1
        argCount = int(self.pMem[self.pc])

        # TODO don't use this array, but allocate space in system memory
        swap = []

        for i in xrange(0, argCount):
            swap += [self.pop()]

        self.push(self.pc)

        for item in reversed(swap):
            self.push(item)

        # set up a new scope for variables
        self.vars += [{}]

        self.pc = self.lex.function[functionNameEncoded] - 1

    def _ret(self):
        self.pc += 1
        argCount = int(self.pMem[self.pc])

        swap = []

        for i in xrange(0, argCount):
            swap += [self.pop()]

        returnAddress = self.pop()

        for item in reversed(swap):
            self.push(item)

        # remove local variable scope
        self.vars.pop()

        self.pc = returnAddress

    def _ivar(self):

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
            hit = False
            for varDict in self.vars:
                if varAddress in varDict.values():
                    varAddress += 1
                    hit = True
                    break;
            if not hit:
                addressFound = True

        # store var address in last dict
        self.vars[len(self.vars) - 1][varName] = varAddress

        self.rwMem[varAddress] = value

    def _ivarst(self):
        # Create var from a stack pop

        self.pc += 1
        varName = self.pMem[self.pc]

        value = int(self.pop())

        # find an empty address to store var to
        # hopefully we find a quicker way of doing this, O(n) isn't very cool
        # TODO make this quicker

        varAddress = 0
        addressFound = False
        hit = False

        while not addressFound:
            hit = False
            for varDict in self.vars:
                if varAddress in varDict.values():
                    varAddress += 1
                    hit = True
                    break;
            if not hit:
                addressFound = True

        # store var address in last dict
        self.vars[len(self.vars) - 1][varName] = varAddress

        self.rwMem[varAddress] = value

    def _iget(self):
        # Get var and push to stack

        self.pc += 1
        varName = self.pMem[self.pc]

        for varDict in self.vars:
            if varName in varDict.keys():
                self.push(self.rwMem[varDict[varName]])
                break;

    def _iset(self):
        # Change the value of an initialized variable

        self.pc += 1

        varName = self.pMem[self.pc]

        for varDict in self.vars:
            if varName in varDict.keys():
                self.rwMem[varDict[varName]] = self.pop()
                break;

    def _spget(self):
        # Get var and push to stack
        self.push(self.sp)

    def _spset(self):
        # Change the value of an initialized variable
        self.sp = self.pop()

    def _nop(self):
        # do nothing, but need to make python think we are doing something
        nothing = True

    def _halt(self):
        self.halt = 1

    def __init__(self):
        self.stack = [None]*(1024*4)
        self.pMem = [None]*(1024*4)
        self.rwMem = [None]*(1024*4)

        self.halt = 0

        self.pc = 0
        self.sp = -1

        self.lex = Lex()

        # vars will be stored in a set of dicts, one per scope level
        self.vars = [{}]

        self.console = console.tinyconsole()

        self.debug = False

vm = VM()
#vm.debug = True
#vm.debug = False
vm.start()
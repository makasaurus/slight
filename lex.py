from ops import *

class Lex:

    def __init__(self):
        self.label = {}
        

    """
        source as a string
    """
    def encode(self, source):
        byteCode = []
        lines = source.split("\n")

        for i in xrange(0, len(lines)):
            line = lines[i]
            tokens = line.split(" ")
            for i, token in enumerate(tokens):
                if token.upper() in compilerCodes:

                    if token.upper() == 'LABEL':
                        #need to convert next item, which will be label name, to a number to store to bytecode
                        #could hash, but we will just convert the name
                        tokenInt = int(tokens[i+1].encode("hex"), 16)
                        tokens[i+1] = str(tokenInt)

                        #add label location to label dict based on tokenInt
                        self.label[tokenInt] = len(byteCode)

                        break;

                    if token.upper() == 'JMP':
                        tokenInt = int(tokens[i+1].encode("hex"), 16)
                        tokens[i+1] = str(tokenInt)
                        byteCode += [opcodes[token.upper()]]


                elif token.upper() in opcodes:
                    byteCode += [opcodes[token.upper()]]
                else:
                    byteCode += [int(token)]
        print byteCode
        return byteCode

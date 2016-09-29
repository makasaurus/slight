from ops import *

"""

Lex converts the input file to be ran into executable bytecode. If a token indicates that it has a non-reserved word
following it, such as a variable name or a string, the lexer will also convert this into usable bytecode. This is
clearly not the best route to do this, as we could offload strings into memory.

Lex should eventually be expanded to enable it to run in an interactive mode, where you can type code into an
interactive console.

"""

class Lex:

    def __init__(self):
        self.label = {}
        self.function = {}

    """
        source as a string
    """
    def encode(self, source):
        # TODO create interactive mode of encode
        byteCode = []
        lines = source.split("\n")

        for i in xrange(0, len(lines)):
            line = lines[i]
            if line[0:2] == "//":
                comment = True
                continue

            tokens = line.split()

            for i, token in enumerate(tokens):
                if token[0:2] == "//":
                    comment = True
                    break
                if token.upper() in compilerCodes:

                    if token.upper() == 'LABEL':
                        #need to convert next item, which will be label name, to a number to store to bytecode
                        #could hash, but we will just convert the name
                        tokenInt = int(tokens[i+1].encode("hex"), 16)
                        tokens[i+1] = str(tokenInt)

                        #add label location to label dict based on tokenInt
                        self.label[tokenInt] = len(byteCode)

                        break;

                    if token.upper() == 'DEF':
                        defInt = int(tokens[i+1].encode("hex"), 16)
                        tokens[i+1] = str(defInt)

                        self.function[defInt] = len(byteCode)
                        break;
                    if token.upper() == 'CALL':
                        defInt = int(tokens[i+1].encode("hex"), 16)
                        tokens[i+1] = str(defInt)
                        byteCode += [opcodes[token.upper()]]

                    if token.upper() == 'JE':
                        defInt = int(tokens[i+1].encode("hex"), 16)
                        tokens[i+1] = str(defInt)
                        byteCode += [opcodes[token.upper()]]

                    if token.upper() == 'JNE':
                        defInt = int(tokens[i+1].encode("hex"), 16)
                        tokens[i+1] = str(defInt)
                        byteCode += [opcodes[token.upper()]]

                    if token.upper() == 'JMP':
                        tokenInt = int(tokens[i+1].encode("hex"), 16)
                        tokens[i+1] = str(tokenInt)
                        byteCode += [opcodes[token.upper()]]

                    if token.upper() == 'RET':
                        byteCode += [opcodes[token.upper()]]

                    if token.upper() == 'IVAR':
                        byteCode += [opcodes[token.upper()]]
                        tokens[i+1] = str(int(tokens[i+1].encode("hex"), 16))

                    if token.upper() == 'IVARN':
                        byteCode += [opcodes[token.upper()]]
                        tokens[i + 1] = str(int(tokens[i + 1].encode("hex"), 16))

                    if token.upper() == 'IVARST':
                        byteCode += [opcodes[token.upper()]]
                        tokens[i+1] = str(int(tokens[i+1].encode("hex"), 16))

                    if token.upper() == 'IGET':
                        byteCode += [opcodes[token.upper()]]
                        tokens[i+1] = str(int(tokens[i+1].encode("hex"), 16))

                    if token.upper() == 'ISET':
                        byteCode += [opcodes[token.upper()]]
                        tokens[i+1] = str(int(tokens[i+1].encode("hex"), 16))

                elif token.upper() in opcodes:
                    byteCode += [opcodes[token.upper()]]
                else:
                    byteCode += [int(token)]
        return byteCode

    def encodeToken(self, token):
        return int(token.encode("hex"), 16)

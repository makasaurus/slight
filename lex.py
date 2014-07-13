from ops import *

class Lex:

    """
        source as a string
    """
    def encode(self, source):
        byteCode = []
        lines = source.split("\n")
        for line in lines:
            tokens = line.split(" ")
            for token in tokens:
                if token.upper() in opcodes:
                    byteCode += [opcodes[token.upper()]]
                else:
                    byteCode += [int(token)]
        return byteCode

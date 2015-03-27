"""

Ops is the dict object that allows for the lookup of and reverse-lookup of each op code.

"""

#TODO redo codes to follow groups - i.e. these use variables, these compare variables, etc. more cohesive.
opcodes = {
    'IPUSH': 0x01,
    'IPOP': 0x02,
	'IADD' : 0x11,
	'ISUB' : 0x12,
    'IMUL' : 0x13,
	'IDIV' : 0x14,
    'CPUSH' : 0x15,
    'CPOP' : 0x15,
    'AND' : 0x21,
    'OR' : 0x22,
    'NOT' : 0x23,
    'CMP' : 0x31,
    'SCMP' : 0x32,
    'JE' : 0x33,
    'JNE' : 0x34,
    'JMP': 0x40,
    'CALL' : 0x50,
    'RET' : 0x51,
    'IVAR' : 0x60,
    'IVARST' : 0x61,
    'IGET' : 0x62,
    'ISET' : 0x63,
    'CVARST' : 0x64,
    'CGET' : 0x65,
    'CSET' : 0x66,
    'RAND' : 0x70,
    'IPRINT': 0xe1,
    'CPRINT' : 0xe2,
    'IIN': 0xe2,
    'NOP' : 0xfe,
    'HALT' : 0xff
}

compilerCodes = [
    'LABEL',
    'JE',
    'JNE',
    'JMP',
    'DEF',
    'CALL',
    'RET',
    'IVAR',
    'IVARST',
    'IGET',
    'ISET'
]

codes = {}

#generate codes, which will be our reverse lookup dict for speed purposes.  small size, should be okay.
for k in opcodes:
    codes[opcodes[k]]=k

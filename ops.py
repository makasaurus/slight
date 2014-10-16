
opcodes = {
    'IPUSH': 0x01,
    'IPOP': 0x02,
	'IADD' : 0x11,
	'ISUB' : 0x12,
    'IMUL' : 0x13,
	'IDIV' : 0x14,
    'AND' : 0x21,
    'OR' : 0x22,
    'NOT' : 0x23,
    'CMP' : 0x31,
    'JE' : 0x32,
    'JNE' : 0x33,
    'JMP': 0x40,
    'CALL' : 0x50,
    'RET' : 0x51,
    'VAR' : 0x60,
    'VARST' : 0x61,
    'GET' : 0x62,
    'SET' : 0x63,
    'RAND' : 0x70,
    'IPRINT': 0xe1,
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
    'VAR',
    'VARST',
    'GET',
    'SET'
]

codes = {}

#generate codes, which will be our reverse lookup dict for speed purposes.  small size, should be okay.
for k in opcodes:
    codes[opcodes[k]]=k

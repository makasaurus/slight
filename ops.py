
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
    'JMP': 0x40,
    'CALL' : 0x50,
    'RET' : 0x51,
    'VAR' : 0x60,
    'VARST' : 0x61,
    'GET' : 0x62,
    'IPRINT': 0xe1,
    'NOP' : 0xfe,
    'HALT' : 0xff
}

compilerCodes = [
    'LABEL',
    'JMP',
    'DEF',
    'CALL',
    'RET',
    'VAR',
    'VARST',
    'GET'
]

codes = {}

for k in opcodes:
    codes[opcodes[k]]=k

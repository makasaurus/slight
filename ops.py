
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
    'IPRINT': 0xe1,
    'HALT' : 0xff
}

codes = {}

for k in opcodes:
    codes[opcodes[k]]=k
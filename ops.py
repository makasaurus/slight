
opcodes = {
    'IPUSH': 0x01,
    'IPOP': 0x02,
	'IADD' : 0x11,
	'ISUB' : 0x1a2,
    'IPRINT': 0xe1,
    'HALT' : 0xff
}

codes = {}

for k in opcodes:
    codes[opcodes[k]]=k
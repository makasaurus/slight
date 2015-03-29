slight
======

slight is a very small system with aims of project oberon.


Ops 
-----

Ops are used as follows:
`push A
push B
push C
<op name> <named arg>`

For example, to output the result of ( 1 || 0 ) to the top of the stack:
`
ipush 1
ipush 0
or
iprint
`



|     Op     | Op code | Pushed Args  | Named Args | Description |                                                                                                                                                              
| -----------|---------|--------------|------------|--------------------------------------------|
|  **IPUSH** |  `0x01` |              | num        | Pushes integer num on to the top of the stack.
|  **IPOP**  |  `0x02` |              |            | Removes the top-most entry from the stack. 
|  **IADD**  |  `0x11` | int A, B     |            | Stores A + B to the top of the stack.
|  **ISUB**  |  `0x12` | int A, B     |            | Stores A-B to the top of the stack.
|  **IMUL**  |  `0x13` | int A, B     |            | Stores A*B to the top of the stack.
|  **IDIV**  |  `0x14` | int A, B     |            | Stores A/B to the top of the stack.
|  **CPUSH** |  `0x15` | char A, B    |            | Pushes char A to the top of the stack. *Currently unimplemented.*
|  **CPOP**  |  `0x16` |              |            | Removes the top most entry from the stack. *Currently unimplemented and possibly unneeded.*
|  **AND**   |  `0x21` | bool A, B    |            | Stores (A && B) to the top of the stack as 1 for true, 0 for false..
|  **OR**    |  `0x22` | bool A, B    |            | Stores (A || B) to the top of the stack as 1 for true, 0 for false.
|  **NOT**   |  `0x23` | bool A       |            | Stores (!A)  to the top of the stack as 1 for true, 0 for false.
|  **CMP**   |  `0x31` | int A, B     |            | Stores 1 on the stack if A > B, 0 if equal, else -1
|  **SCMP**  |  `0x32` | str A, B     |            | Stores 1 on the stack if A == B, else 0. *Currently unimplemented.*
|  **JE**    |  `0x34` | int A, B     | LBL        | If (A == B), then the program jumps to LBL
|  **JNE**   |  `0x34` | int A, B     | LBL        | If (A == B), then the program jumps to LBL
|  **JNE**   |  `0x34` | int A, B     | LBL        | If (A == B), then the program jumps to LBL

slight
======

slight is a very small system, starting with the creation of a bytecode and aiming to end with the implementation of
the CPU on an FPGA. This project is inspired by project oberon.

slight:
* is stack based
* has non-dynamic program memory
* has an n-bit emulator
* allows for functions, function overloading, and variable scopes at byte-code level
* is very simple

goals:
* complete emulator
* create cli terminal to code in real time
* run terminal graphics and I/O from machine
* run 'complex' graphics
* write a high-level OOP language, named donut, that compiles down to bytecode.
* write donut compiler in donut 
* implement in Verilog on FPGA


Ops 
-----

Ops are used as follows:
```
push A
push B
push C
<op name> <named arg>
```

For example, to output the result of ( 1 || 0 ) to the top of the stack:
```
ipush 1
ipush 0
or
iprint
```



|     Op      | Op code | Pushed Args  | Named Args   | Description                                |                                                                                                                                                              
| ------------|---------|--------------|--------------|--------------------------------------------|
|  **IPUSH**  |  `0x01` |              | num          | Pushes integer `num` on to the top of the stack.
|  **IPOP**   |  `0x02` |              |              | Removes the top-most entry from the stack. 
|  **IADD**   |  `0x11` | int A, B     |              | Stores A + B to the top of the stack.
|  **ISUB**   |  `0x12` | int A, B     |              | Stores A-B to the top of the stack.
|  **IMUL**   |  `0x13` | int A, B     |              | Stores A*B to the top of the stack.
|  **IDIV**   |  `0x14` | int A, B     |              | Stores A/B to the top of the stack.
|  **CPUSH**  |  `0x15` | char A, B    |              | Pushes char A to the top of the stack. *Currently unimplemented.*
|  **CPOP**   |  `0x16` |              |              | Removes the top most entry from the stack. *Currently unimplemented and possibly unneeded.*
|  **AND**    |  `0x21` | bool A, B    |              | Stores (A && B) to the top of the stack as 1 for true, 0 for false..
|  **OR**     |  `0x22` | bool A, B    |              | Stores (A || B) to the top of the stack as 1 for true, 0 for false.
|  **NOT**    |  `0x23` | bool A       |              | Stores (!A)  to the top of the stack as 1 for true, 0 for false.
|  **CMP**    |  `0x31` | int A, B     |              | Stores 1 on the stack if A > B, 0 if equal, else -1
|  **SCMP**   |  `0x32` | str A, B     |              | Stores 1 on the stack if A == B, else 0. *Currently unimplemented.*
|  **JE**     |  `0x34` | int A, B     | lbl          | If (A == B), then the program jumps to `lbl`
|  **JNE**    |  `0x34` | int A, B     | lbl          | If (A == B), then the program jumps to `lbl`
|  **CALL**   |  `0x50` | A, B, ...    | func, arglen | Calls function `func` with `arglen` amount of arguments and args A, B, ...
|  **RET**    |  `0x51` | A, B,  ...   | arglen       | Returns function with `arglen` amount of arguments and args A, B, ...
|  **IVAR**   |  `0x60` |              | varname, val | Creates variable `varname` set to integer `val`
|  **IVARST** |  `0x61` | A            | varname      | Creates variable `varname` set to arg A
|  **IGET**   |  `0x62` |              | varname      | Pushes value of `varname` to the top of the stack.
|  **ISET**   |  `0x62` | A            | varname      | Updates value of `varname` to arg A.
|  **RAND**   |  `0x70` | A, B         |              | Pushes random integer x to the top of the stack, with A <= x < B.
|  **IPRINT** |  `0xe1` | A            |              | Prints integer A to the terminal
|  **IIN**    |  `0xe2` |              |              | Pushes integer terminal user input to the top of the stack
|  **NOP**    |  `0xfe` |              |              | Do nothing for one cycle.
|  **HALT**   |  `0xff` |              |              | End execution of program









slight
======

slight is a very small system with aims of project oberon.


Ops 
-----

|     Op     | Op code | Arguments | Description |                                                                                                                                                              
| -----------|---------|-----------|--------------------------------------------------------|
|  *IPUSH**  |  `0x01` |     A     | Pushes integer A on to the top of the stack
|  **IPOP**  |  `0x02` |   *none*  | Removes the top-most entry from the stack. 
|  **IADD**  |  `0x11` |    A, B   | Adds A and B together and pushes the sum to the stack
|  **ISUB**  |  `0x12` |    A, B   | Subtracts B *from* A amd pushes the result to the stack

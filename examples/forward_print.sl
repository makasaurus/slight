ivar enter_ord 13
ivar backspace_ord 8
ivar chr 0
ivar line_len 0
// main loop for keyboard input
// might want to make this a function and pass in pointers for enter/backspace event function overrides.
// that would be fancy.
// overwrite enter_press to
label   getkey
cin                         // get  keypress
iset    chr             // save keypress

iget    enter_ord
iget    chr
je      enter_press

iget    backspace_ord
iget    chr
je      backspace_press

iget    chr
cprint
ipop

iget    chr     //push onto stack to print later

iget line_len   //lots of code just for line_len += 1
ipush 1
iadd
iset line_len

jmp     getkey

//keyboard input is an enter
label   enter_press
//print enter line
ipush   10
cprint
//pop enter key off stack, not useful
ipop
jmp     forward_print

// keyboard input is a backspace - remove char
label   backspace_press
iget    backspace_ord
cprint
ipop

ipop    // pop the bkspc char

iget    line_len   //lots of code just for line_len -= 1
ipush   -1
iadd
iset    line_len

jmp     getkey

// print stack contents in forward order on new line
label   forward_print
//set sp to first letter, which is (-1)*line_len away
iget line_len
ipush -1
imul
spget
iadd
spset

label forward_print_loop
        // leave loop is line_len = 0, recursive end
ipush   0
iget    line_len
je      end_forward_print

cprint  //print char at top of stack
ipop    //pop char at top of stack so we don't have to do another loop to clean
ipush   -1
iget    line_len
iadd
iset    line_len
//move the stack one position back
spget
ipush   -1
iadd
spset
jmp     forward_print_loop   //recursive is cool, does it count if it's a goto?

label end_forward_print
ipush   10  //push a return and print it, return to loop
cprint
ipop
jmp getkey
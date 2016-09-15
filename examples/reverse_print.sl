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
ipush   10
cprint
ipop
jmp     reverse_print

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

        // print stack contents in reverse order on new line
label   reverse_print

        // leave loop is line_len = 0, recursive end
ipush   0
iget    line_len
je      end_reverse_print

cprint  //print char at top of stack
ipop
ipush   -1
iget    line_len
iadd
iset    line_len
jmp     reverse_print   //recursive is cool

label end_reverse_print
ipush 10    //push a return and print it, return to loop
cprint
ipop
jmp getkey
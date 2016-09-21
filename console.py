import msvcrt
import sys
import os


class tinyconsole:

    def __init__(self):
        self.buff = ''
        self.escape_key = '\x1b'
        self.enter_key = '\r'

        self.clear_console()

        self.init_print()

    def update_display(self, ch):
        ch = '\b \b' if ch == '\x08' else ch
        sys.stdout.write(ch)
        sys.stdout.flush()

    def update_buffer(self, ch):
        if ch == '\x08': self.buff = self.buff[:-1]
        else: self.buff += ch

    def print_buffer(self):
        sys.stdout.write("\n" + self.buff + "\n")

    def empty_buffer(self):
        self.buff = ''

    def dumb_console(self):
        ch = ''
        while ch != self.escape_key:
            ch = msvcrt.getch()
            if ch == self.enter_key:
                self.print_buffer()
                self.empty_buffer()
            else:
                self.update_buffer(ch)
                self.update_display(ch)

    def getchar(self):
        ch = msvcrt.getch()
        if ch == self.escape_key: quit()
        return ch

    def putchar(self, ch):
        sys.stdout.write(ch)
        self.update_buffer()


    def delete_char(self):
        self.putchar('\b \b')

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def init_print(self):
        message = """\n    tiny term\n___________________"""
        print message

##figure out how to name things right pls / dynamic mem management

#tc = tinyconsole()
#tc.dumb_console()
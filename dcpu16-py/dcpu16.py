from lexer import *
import os

pc = sp = o = 0
a = b = c = x = y = z = i = j = 0

ram = [] # todo wrap this for 0x10000 limit

def stmnt_callback(scanner, token):
    """ This is just an example of providing a function to run the
        token through.
    """
    print 'end_stmnt: ' + token
    return ""
 
rules = [
    ("WORD", r"[a-zA-Z_][\w,]*"),
    ("SEPARATOR", r"[\w,]+"),
    ("ADDRESS", r"\[0x[\dA-Fa-f]\]"),
    ("HEX", r"0x[\dA-Fa-f]"),
    ("ADDRESS", r"\[0x[\dA-Fa-f]\]*"),
    ("COMMENT", r";.*"),
    ("OPERATOR",   r"\+|\-|\\|\*|\="),
    ("DIGIT",      r"[0-9]+(\.[0-9]+)?"),
    ("END_STMNT",  ("\r", stmnt_callback)), 
    ]
 
lex = Lexer(rules, case_sensitive=True)
f = open('test.in')
try:
    for token in lex.scan(f.read()):
        print(token)
except UnknownTokenError as ex:
    print(ex)

#print(len(ram))

def hex2dec(s):
    """return the integer value of a hexadecimal string s"""
    return int(s, 16)

def nexttoken():
    
    pass

def parse():
    return 0

#os.system('pause')

os.system('pause')

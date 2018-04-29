
import codegen
from astPy import ast, Unsorted, Alphabetical

expr = """

def bfoo():
    return 1

import zfoo, afoo,dfoo 

class ba():

    def foo():
       print("hello world")

import afoo

def afoo():
    return 2

class a1():

    def bfoo():
       print("hello world 2")

    def afoo():
       print("hello world 2")

a = 1
c = b = 2
b = a              

"""

p = ast.parse(expr)
u = Unsorted(p, Alphabetical())
u.sort()
print(codegen.to_source(u.context))

# codegen.to_source(p.body[1])

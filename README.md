# Intro
astPy organizes unruly python code. You can sort classes, functions, and assignments alphabetically.  It uses [ast](https://docs.python.org/3/library/ast.html) and [codegen](https://github.com/andreif/codegen).
### Usage
```python
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
# printing results
print(codegen.to_source(u.context))
```
``` 
import afoo
import afooimport dfooimport zfoo


class a1:

    def afoo():
        print 'hello world 2'

    def bfoo():
        print 'hello world 2'


class ba:

    def foo():
        print 'hello world'

def afoo():
    return 2

def bfoo():
    return 1
a = 1
b = a
b, c = 2
```

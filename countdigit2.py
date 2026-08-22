from math import *

def countDigits (num):
     return int (log10(num)+1)

n=5438
print(countDigits(n))
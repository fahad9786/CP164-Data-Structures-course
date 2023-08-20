"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-02-03"
-------------------------------------------------------
"""


from Stack_array import Stack
from functions import stack_split_alt

s = Stack()
source = [8,14,12,9,8,7,5]
for i in source:
    s.push(i)
    

print(stack_split_alt(s))



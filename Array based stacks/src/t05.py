"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""

from functions import is_mirror_stack


m = "m" or "M"
valid_chars = 'a', 'b','c'

string = "aabbbmbbbaaa"

print(is_mirror_stack(string, valid_chars, m))

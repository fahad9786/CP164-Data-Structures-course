"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
Section: CP164 B
__updated__ = "2023-01-13"
-------------------------------------------------------
"""

from functions import file_analyze
filename = "movies.txt"
fv = open(filename,"r",encoding = "utf-8")
print(file_analyze(fv))


fv.close()

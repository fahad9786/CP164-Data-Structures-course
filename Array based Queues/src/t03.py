"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-02-08"
-------------------------------------------------------
"""

from Queue_array import Queue
from functions import queue_combine

first1 = Queue()
first2 = Queue()


first = [5, 8, 12, 8]
seconds = [7, 9, 14]


for every in first:
    first1.insert(every)
    
for each in seconds:
    first2.insert(every)
  
    
x = queue_combine(first1, first2)


for each in x:
    print(each)
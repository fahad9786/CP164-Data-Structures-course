"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-02-10"
-------------------------------------------------------
"""



from Priority_Queue_array  import Priority_Queue
from functions import pq_split_key
source = Priority_Queue()

sources = [1,2,3,4,5,  6  ,7,8,9,10,11]

key = 6



for each in sources:
    source.insert(each)

    
target1, target2 = pq_split_key(source, key)

while not target1.is_empty():
    print(target1.remove())
    
print("++++++++++++++++++++++++++++")


while not target2.is_empty():
    print(target2.remove())
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



from Queue_array import Queue

lol = Queue()
lols  = Queue()
target = Queue()
x = [1,2,4,4,5,6]
y = [6,5,4,3,2,1]


for i in x:
    lol.insert(i)



for i in y:
    lols.insert(i)
    
xyz = target.combine(lol,lols)


for each in target:
    print(each)

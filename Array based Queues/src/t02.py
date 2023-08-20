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

queue1 = Queue()
queue2 = Queue()

x = [1,2,4,4,5,6]
y = [6,5,4,3,2,1]


for i in x:
    queue2.insert(i)



for i in y:
    queue1.insert(i)
    


equals = queue1 == queue2
print(equals) 
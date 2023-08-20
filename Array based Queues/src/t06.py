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


from Priority_Queue_array import Priority_Queue



# Create a priority queue and insert some elements
source = Priority_Queue()
sources = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for each in sources:
    source.insert(each)

# Split the priority queue using the key
key = 6
target1, target2 = source.split_key(key)


# Print the elements of the two split priority queues
for i in target1:
    print(i)
    

print("________________________________________")

for i in target2:
    print(i)
    
    
    
if (source.is_empty()):
    print("TREUEE")

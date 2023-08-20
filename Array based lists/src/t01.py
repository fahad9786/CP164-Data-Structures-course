"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-02-14"
-------------------------------------------------------
"""



""
from List_array import List

source = List()
sources = List()


source1 = [1,2,3,3,54,52,2]
source2 = [1,2,3,34,54,52,2]

for each in source1:
    source.append(each)
    
for each in source2:
    sources.append(each)
    
key = 3
equals = source == sources
print(equals)

""




""
from List_array import List

source = List()
source1 = [1,2,3,3,54,52,2]


for each in source1:
    source.append(each)
key = 0
x = source[key]

print(x)

""

""

from List_array import List

source = List()
source1 = [1,2,3,3,54,52,2]


for each in source1:
    source.append(each)
    
key = 3
source.append(key)

for each in source:
    print(each)
""



""
from List_array import List

source = List()
source1 = [1,2,3,3,54,52,2]


for each in source1:
    source.append(each)
    
key = 3
source.clean()

for each in source:
    print(each)
""







""
from List_array import List

source = List()
source1 = [1,2,3,3,54,52,2]


for each in source1:
    source.append(each)
    
key = 3
source.prepend(key)

for each in source:
    print(each)

""





""
source = List()
source1 = [1,2,3,3,54,52,2]


for each in source1:
    source.append(each)
    
key = 3
source.prepend(key)

for each in source:
    print(each)


""













""
from List_array import List


source = List()
source1 = [1,2,3,3,54,52,2]


for each in source1:
    source.append(each)
    
key = 3
source.remove_front()
source.remove(key)

for each in source:
    print(each)

""


""
source = [1,2,3,4,5]
target = List()


for each in source:
    target.append(each)
target1, target2 = target.split()

print(target1)
print(target2)
""



""
from List_array import List

source = List()
source1 = [1,2,3,3,54,52,2]


for each in source1:
    source.append(each)
    
    
target1, target2 = source.split_alt()

for each in target1:
    print(each)
    
print("XXXXXXXXXXXXXXXX")
for each in target2:
    print(each)
""


""
source11 = [44, 33, 55, 22, 55]

source22 = [22, 55, 11, 12]
target = [55, 22]


from List_array import List

source1 = List()
source2 = List()
target = List()


for each in source11:
    source1.append(each)

for each in source22:
    source2.append(each)

    
x = target.intersection(source1, source2)


for each in target:
    print(each)
""


""
source11 = [22, 33, 44, 55, 55]
source22 = [11, 12, 22, 55]

target = [55, 22]


from List_array import List

source1 = List()
source2 = List()
target = List()


for each in source11:
    source1.append(each)

for each in source22:
    source2.append(each)

    
target.union(source1, source2)

for each in target:
    print(each)
""

""
from List_array import List
source1 = List()

source22 = []





for each in source22:
    source1.append(each)
    
    
x = source1.clean()


for each in source1:
    print(each)
""


""
source11 = [555,1]
source22 = [11, 12, 22, 55]



from List_array import List

source1 = List()
source2 = List()
target = List()


for each in source11:
    source1.append(each)

for each in source22:
    source2.append(each)

    
target.combine(source1, source2)

for each in target:
    print(each)

""



""
source11 = []
source22 = [11, 12, 22, 55]



from List_array import List

source1 = List()

source1.append(9)

value = 1
source1.prepend(value)

for each in source1:
    print(each)
    
x = source1.remove_front()


""

""

from List_array import List

source1 = List()


source1.append(11)
source1.append(9)
source1.append(9)
source1.append(9)

source1.append(9)
source1.append(9)
source1.append(9)
key = 9

source1.remove_many(key)


"====="

for each in source1:
    print(each)
""







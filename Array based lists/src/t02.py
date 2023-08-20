
"""new function below or above"
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-02-15"
-------------------------------------------------------
"new function below or above"
"""
from Sorted_List_array import Sorted_List


from Movie import Movie

# Create a Bag object with several Movie objects

movie1 = Movie("The Shawshank Redemption", 1994, "Frank Darabont", 9.3, [2, 7])

# create another movie object
movie2 = Movie("The Godfather", 1972, "Francis Ford Coppola", 9.0, [2, 5, 7])


bag = Sorted_List()
bag.insert(movie1)
bag.insert(movie2)


# Call the remove_many function to remove all movies with a rating of 9.0
bag.remove_many(Movie("", 1972, "", 9.0, []))

# Print the contents of the Bag to ensure that the correct movies were removed
for movie in bag:
    print(movie)





"new function below or above"

from Sorted_List_array import Sorted_List
source = Sorted_List()

source.insert(5)

source.insert(2)

source.insert(4)


    
    
i = 2

value = source[i]
print(value)


"new function below or above"


"new function below or above"
source = Sorted_List()

source.insert(2)

source.insert(5)

source.insert(2)

source.insert(4)

source.insert(2)

source.clean()

for each in source:
    print(each)
"new function below or above"
"new function below or above"

from Sorted_List_array import Sorted_List
source = Sorted_List()

source.insert(2)

source.insert(5)

source.insert(2)

source.insert(4)

source.insert(2)

key = 4
n = source.count(key)
n = source.index(key)
print(n)

"new function below or above"


"new function below or above"

from Sorted_List_array import Sorted_List
source = Sorted_List()

source.insert(2)

source.insert(5)

source.insert(2)

source.insert(4)

source.insert(2)
key = 2
value = source.find(key)
print(value)
"new function below or above"

"new function below or above"
from Sorted_List_array import Sorted_List
source = Sorted_List()

source.insert(2)

source.insert(5)

source.insert(2)

source.insert(4)

source.insert(2)
key = 1
n = source.index(key)
print(n)

"new function below or above"

"new function below or above"
from Sorted_List_array import Sorted_List
source1 = Sorted_List()
source2 = Sorted_List()
target = Sorted_List()
source11 = [22, 33, 44, 55, 55]
source22 = [11, 12, 22, 55]

for each in source11:
    source1.insert(each)

for each in source22:
    source2.insert(each)

    
x = target.intersection(source1, source2)

for each in target:
    print(each)
"new function below or above"


"new function below or above"
from Sorted_List_array import Sorted_List
source = Sorted_List()

source.insert(2)

source.insert(5)

source.insert(2)

source.insert(4)

source.insert(2)

value = source.max()

print(value)

"new function below or above"


"new function below or above"
from Sorted_List_array import Sorted_List
source = Sorted_List()

source.insert(2)

source.insert(5)

source.insert(2)

source.insert(4)

source.insert(2)

value = source.min()

print(value)

"new function below or above"

"new function below or above"

from Sorted_List_array import Sorted_List
source = Sorted_List()

source.insert(0)

source.insert(5)

source.insert(2)

source.insert(4)

source.insert(2)

value = source.peek()
print(value)
"new function below or above"



"new function below or above"
from Sorted_List_array import Sorted_List
source = Sorted_List()


source.insert(0)

source.insert(5)

source.insert(2)

source.insert(4)

source.insert(2)
key = 2

value = source.remove(key)
for each in source:
    print(each)
"new function below or above"



"new function below or above"
from Sorted_List_array import Sorted_List
source = Sorted_List()


source.insert(0)

source.insert(5)

source.insert(2)

source.insert(4)

source.insert(2)

value = source.remove_front()
for each in source:
    print(each)
"new function below or above"

"new function below or above"
from Sorted_List_array import Sorted_List
source = Sorted_List()


source.insert(0)

source.insert(5)

source.insert(2)

source.insert(4)

source.insert(2)
key = 2
source.remove_many(key)
for each in source:
    print(each)

"new function below or above"

"new function below or above"


from Sorted_List_array import Sorted_List
source1 = Sorted_List()
source2 = Sorted_List()
target = Sorted_List()
targets = [22, 33, 44, 55, 55]
for each in targets:
    target.insert(each)

source1, source2 = target.split()

for each in source1:
    print(each)

print("   x           x")


for each in source2:
    print(each)
"new function below or above"


"new function below or above"

from Sorted_List_array import Sorted_List

target = Sorted_List()
targets = [22, 33, 44, 55, 55]
for each in targets:
    target.insert(each)

target1, target2 = target.split_alt()

for each in target1:
    print(each)
print("XXXXXXXXX")
for each in target2:
    print(each)
    
    
    
"new function below or above"

"new function below or above"
from Sorted_List_array import Sorted_List

target = Sorted_List()
target1 = Sorted_List()
target2 = Sorted_List()

target1 = [22, 33, 44, 55, 55]
target2 = [12,11, 22, 55]
x = target.union(target1, target2)


for each in target:
    print(each)

"new function below or above"


"new function below or above"
from Sorted_List_array import Sorted_List
source = Sorted_List()

target11 = [1,2,3,4,5,6,7,8,9]

for each in target11:
    source.insert(each)

key = 5


target1, target2 = source.split_key(key)

for each in target1:
    print(each)

print("__________________________________")

for each in target2:
    print(each)
"new function below or above"


# Creating array steps
# -> Assign it to a variable
# -> Define the type of elements that it will store
# -> Define the size the maximum number of elements

from array import *

arr1 = array("i",[1,2,3,4,5,6])
print(arr1)

arr2 = array("d",[1.2,3.2,3.5])
print(arr2)
print(type(arr1))
print(type(arr2))

#TC for creation of array is 1

#inserting in the last of the array

# arr1.insert(index,value)
# arr1.insert(6,7)
# print(arr1)

# whenever you insert in the array or middle of the array the element move one step right here
# for eg
print(arr1)
arr1.insert(2,9)
print(arr1)

# if inserting beginning time complexity - O(n)
# if inserting at the back then time complexity - O(1)
# if inserting at the middle still time complexity - O(n)
# if inserting in full array the time complexity - O(n)

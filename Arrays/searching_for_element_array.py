from array import *

arr1 = array("i",[1,2,3,4,5,6,7,8])
print(arr1)

def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exists in the array"

print(searchInArray(arr1,6))

# TC - O(n)
# SC - O(1)




























































from array import *

arr1 = array("i",[15,22,3,14,65,64])

print(arr1)

def accessElement(array,index):
    if index >= len(arr1):
        print("No such index exists to access an array")
    else:
        print(array[index])


accessing = accessElement(arr1,6)

print(accessing)

#TC - O(1)
#SC - O(1)





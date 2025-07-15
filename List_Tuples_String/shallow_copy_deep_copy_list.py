list1 = [1,2,2,3,4,5,6,7,8,9]
list2 = list1 #deep copy
list2.append([1,2,3])

print(list2, id(list2))
print(list1 ,id(list1))

#id matlab address type hee idar okk
# toh dono mein changes dikhega because of vooh naa ek hee address ko point krr rahe hee

# sirf values copy hote variable nhi hote thats called as shallow copy bro
# .copy() method use karna hote hee for this

list_1 = [1,2,2,3,4,5,6,7,8,9]
list_2 = list_1.copy() #meine shallow copy pass kii hee

list_2.append(4)
print(list_1 , id(list_1))
print(list_2, id(list_2))

list11 = [3, 4, 456, 24, 312, 234, 456, 42, 23]

print(list11[2:6])       # From index 2 to 5
print(list11[2:8:3])     # From index 2 to 7, step of 3
print(list11[8:1:-2])    # From index 8 to 2 (not inclusive), step -2

print(list11[:5])        # From start to index 4
print(list11[6:])        # From index 6 to end
print(list11[:])        # Print full list



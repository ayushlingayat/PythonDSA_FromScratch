# Yes, in Python, a list can contain different data type
# The elements stay in the same order in which they were added in list okk.
#they are mutable and allow duplicate values okk

my_list = [1, "hello", 3.14, True, [5, 6], {'a': 1}]
print(my_list)


my_list_fruits = ['apple', 'banana', 'cherry']
print(my_list_fruits)       # ['apple', 'banana', 'cherry']
print(my_list_fruits[0])    # 'apple'
print(my_list_fruits[1])

#methods in list


number_list = [4,2,1,7,8,7]

number_list.append([1,2,3])

print(number_list)

number_list.extend([1,2,3])

print(number_list)
print(number_list[6])


# khuch specific cheez prr insert krr dega

# number_list.insert(index,element)
number_list.insert(3,100)
#abb pata hee number bss insert hoga toh baki kee number shift krr lenge okk

print(number_list)

#remove and pop both used for removing
#remove is used to remove specific element
# aur pop remove karta hee specific index koo

number_list.pop()
#so last element remove hoga

number_list.pop(1)
#index 1 kaa value remove hoga

# number_list.remove(element dena)
number_list.remove(100)

print(number_list)

#puri list clear karni hoo toh
# .clear use karna

number_list.clear()
print(number_list)


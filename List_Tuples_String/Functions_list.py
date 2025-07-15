list_numbers = [2,4,3,6,7,8,9]

#to get min and max element of list
#Min and Max Element
print(min(list_numbers)) #O(n)
print(max(list_numbers)) #O(n)


list1 = [2,4,5,4,8,7,5,4,9]

#jitne baar joo element occur hora in list uska count de dega in simple thik hee

count_of_four = list1.count(4)
print(count_of_four)

#sort function list koo sorting karne mein use hota hee
list1.sort() #O(n log n)
print(list1)

list1.reverse() #O(n)
print(list1)

#.index function use kiya toh element kaa index bata deta

print(list1.index(5))
print(list1.index(4))


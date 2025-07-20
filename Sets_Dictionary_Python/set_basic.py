# Set is in sequence , mutable, hetrogenous, unordered
#in set no indexing possible because of unorderness
#in set unique element store
#set represented by curly brackets

#bhale multiple element add kardo set mein single time hee element print hota hee

set1 = {"hello","ayush","hello","lingayat","ayush",26,26}

print(set1)
print(type(set1))
print(len(set1))
#len mein naa bss unique value aayenge

list1 = [2,4,5,6,7,8,9,8,9,7,5,3,2,4,6]

set2 = set(list1)
print(set2)
print(len(set2))

#methods in set

# add
set1.add(100)
set1.add("hello") #hello phele seeh hee toh naa add nhi hoga in set unique elem rehte isliye

print(set1)

#discard and Remove
# dono hee function set mein remove karne kee kaam atte hee

set1.discard("hello")
set1.discard("hii") # yeeh present nhi hee still error throw nhi karega
set1.remove(26)
# set1.remove("hii") # yeeh toh present nhi yeeh so yeeh naa error show kardega

set3 = {12,24,36,48,60,72,84}

#in kee through check karr sakhte hoo kya yeeh in set hee yaa nhi okk
if 60 in set3:
    print(True)
else:
    print(False)

set3.clear()
print(set3)

#indexing not possible
# set3[0] #indexing nhi rehti

#copy() method in set
#shallow copy
set4 = {1,2,3}
set5 = set4.copy()

set5.add(4)
print(set5)

#deep copy
set6 = {1,2,3}
set7 = set6

set6.add(4)
print(set7)

#Operations in set

set8 = {1,8,5,2,4}
set9 = {8,2,9,6}

#Union
# | pipe symbol represents union
print(set8|set9)
#and inbuilt method is also there
print(set8.union(set9))

#Intersection
# & and symbol represents union
print(set8&set9) #intersection dega
#and inbuilt method is also there
print(set8.intersection(set9))

#Difference
# bss common elements remove hote hee okk baki as it is answer aayega
print(set8-set9)
print(set8.difference(set9))

#Symmetric Difference
#vooh number joo common nhi hee matlab union - intersection bhi bol sakhte hee 
print(set9^set8)
print(set9.symmetric_difference(set8))


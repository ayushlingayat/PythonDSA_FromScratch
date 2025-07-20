# In dictionary key can be unique
#value duplicate hoo sakhte hee
# and key can be non- mutable anything like tuple also
#dictionary elements are ordered now phele nhi the order abb ordered hogayi dictionary


#blank set
set_blank = set({})
print(type(set_blank))

#blank dictionary
x ={}
print(type(x))

#simple dictionary

simp_dict = {1:"ayush", 26:"Birthday",(23,45,67): "Marks"}

print(simp_dict)
print(type(simp_dict))
print(len(simp_dict))

#key seeh value operate krr sakhte like this
print(simp_dict[1])
print(simp_dict[(23,45,67)])

#Operations in Dictionary

dict1 ={1:"Ayush",2:"Rushab",3:"Piyush",4:"Rohan",5:"Bunty"}
print(dict1)
dict1[5] = "Abhi"
dict1[2] = "Ruu"
print(dict1)

# aur ek tarika hee jisse hum dictionary koo update krr sakhte hee
dict1.update({1:"Ayu",2:"Ritik",6:"Bablu"})
print(dict1)

#aur ek tarika hote hee dictionary create karne kaa
dict2 = dict(abhinav =1,aman =2)
print(dict2)

#pop operation also used in dictionary
dict1.pop(2)
print(dict1)
#aur ek tarika hee
del dict1[1]
print(dict1)

#aur ek tarika hee jisse value access kar sakhte hee hum log
print(dict1.get(4))

#clear
#copy same like other data structure

# .items
# .items basically provide karta hee list humko to iterate in dictionary okk

#ek list provide karta dictionary .items likha toh see here
print(dict1.items())


#iterating the dictionary okk
dict3 = {12:"Ayu",34:"Piyu",48:"Riyu"}

for key,value in dict3.items():
    print(key,value)

#.keys() seeh naa hum full keys print kar sakhte hee okk

print(dict3.keys())

#iterating the dictionary and just printing the keys
for key in dict3.keys():
    print(key)

#abb sarre values koo print karna hoo toh .values use kar sakhte hee hum

for values in dict3.values():
    print(values)

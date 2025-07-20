#calculate frequency jyada trr use hota okk in dictionary

list_names = ["Ayush","Piyush","Rushab","Ayush","Piyush"]
freq = {}

for name in list_names:
    if name not in freq:
        freq[name] = 1
    else:
        freq[name] +=1

print(freq)

s = "ayush shyam lingayat"
freq = {}

for name in s:
    if name not in freq:
        freq[name] = 1
    else:
        freq[name] +=1

print(freq)


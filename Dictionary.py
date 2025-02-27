d={'a':123,1:"abc"}
print(d[1])

'''
get
update
values
keys
items
'''

#values
d={'a':123,1:"abc",2:"sweety"}
print(d.values())

#keys
d={'a':123,1:"abc"}
print(d.keys())

#get
d={'a':123,1:"abc"}
print(d.get(1))

#items
d={'a':123,1:"abc"}
print(d.items())

#update
d={'a':123,1:"abc"}
d.update({1111:2222})
print(d)

#for loop

for i in {'a':123,1:"abc"}.items():
    print(i)


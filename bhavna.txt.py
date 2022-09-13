# f=open("bhavna.txt","r")
# data=f.read()
# print(data)
# f.close()


# f=open("bhavna.txt","r")
# d=f.readlines()
# print(d)
# f.close()




f=open("bhavna.txt","r")
data=f.read()
# data=a.split("\n")
vowels=["a","i","e","o","u"]
v_count=0
c_count=0
lower_count=0
uper_count=0
for i in data:
    if i in vowels:
        v_count=v_count+1
    if i.islower():
        lower_count=lower_count+1
    if i.isupper():
        uper_count=uper_count+1
    elif i not in vowels:
        c_count=c_count+1


print("v_count",v_count)
print("lower_count",lower_count)
print("c_count",c_count)
print("uper_count",uper_count)




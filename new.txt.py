# f=open("new.txt","r")
# d=f.readlines()
# print(d)

f=open("new.txt","r+")
d=f.read()
f.write(" I am bhavna")
print(d)
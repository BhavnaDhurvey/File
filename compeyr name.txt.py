# f=open("compeyr name.txt","r")
# d=f.read()
# s=d.split()
# i=0
# j=i+1
# while i<len(s) and j<len(s):
#     if len(s[i])>len(s[j]):
#         print(s[i])
#     i=i+1
#     j+=1



f=open("compeyr name.txt","r")
d=f.read()
s=d.split()
i=0
l=s[0]
c=0
while i<len(s):
    if s[i]<l:
        l=s[i]
    c=len(l)
    i=i+1
print(l,c)


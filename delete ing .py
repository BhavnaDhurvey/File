



f=open("delete ing.txt","r")
a=f.read()
b=a.split(",")
c=""
i=0
while i<len(b):
    if "ing" in b[i]:
        print(b[i][:-3],end=",")
    else:
        print(b[i],end=",") 
    i=i+1

f=open("name.txt","r")
count=0
for line in f:
    if line!="":
        count+=1
print(count)
f.close()
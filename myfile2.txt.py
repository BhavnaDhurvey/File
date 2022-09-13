n=int(input("enter n lines:-  "))
f=open("myfile2.txt","r")
for line in (f.readlines()[n:]):
    print(line,end=" ")
f.close()
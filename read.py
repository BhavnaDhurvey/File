# f=open("my name.txt","r")
# data=f.read()
# print(data)




# f = open("student.txt","w+")
# f.write("youtube")
# print(f.read())

# name=["Bhavna","Narani","pinki"]
# l=open("my name.txt","w")
# i=0
# while i<len(name):
#     l.write(""+name+"\n")
#     i=i+1
# n=input("enter the number\n  ")
# i=0
# while i<len(n):
# f.write(n)
    # i=i+1


# f=open("my name.txt","r")

# print(f.read())
# f.close()


banks_list = ["Ameesha", "Doly", "Bhavna", "Archana", "pinki"]
names=open("file-question3.txt","w")
i=0
while i<len(banks_list):
    names.write(""+banks_list[i]+"\n")
    i+=1
names=open("file-question3.txt","r")
print(names.read())
a=input("enter files names  ")
f=open(a,"r")
d=f.read()
print(d)



# a=input("enter files names ")
# f=open(a,"r")
# d=f.read()
# c=d.split("\n")
# print(c)
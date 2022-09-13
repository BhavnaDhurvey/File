

a=input("enter files names ")
f=open(a,"r")
d=f.read()
c=d.split("\n")
print(c)
count_words=0
count_character=0
i=0
while i<len(c):
    count_character=count_character+len(c[i])
    count_words=count_words+i
    i=i+1
print("count_words",count_words)
print("count_character",count_character)
print("count_line",i)

x = len(f.readlines())
print('Total lines:', x)
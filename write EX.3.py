# f = open("student.txt","w")
# f.write("🥰Hello🥰 \n")
# f.write("🥰I am Bavna🥰 \n")
# f.write("🥰How are you🥰 \n")
# f.close()


# f = open("student.txt","w")
# f.write("Hii")
# f.close()

f = open("student.txt",mode='a')
f.write("bye")
print(f.readline)
f.close()
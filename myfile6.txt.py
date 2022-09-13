# with open("myfile5.txt")as f:
#     content=f.readline()
#     li=[x.strip()for x in content]
# print(li)

# with open("myfile5.txt")as f:
#     lines =[]
#     for line in f:
#         lines.append(line.strip("\n"))
#     print(lines)

from pathlib import path            
p= path ("myfile5.txt")
lines=p.read_text().splitlines()
print(lines)
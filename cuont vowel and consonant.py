

f=open("cuont vowel and consonant.txt","r")
x=f.read()
vowels=["a","e","i","o","u"]
vowel=0
consonants=0
for i in x:
    if i in vowels:
        vowel=vowel+1
    else:
        consonants=consonants+1
print(vowel)
print(consonants)

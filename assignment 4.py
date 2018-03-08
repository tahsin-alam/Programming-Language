#Tahsin Alam
#Assignment 4
#CS 113 Morning.

#Part 1
#A.
str1 = input("Please enter the First String: ")
str2 = input("Please enter the Second String: ")


writeFile = open("my_file.txt","w")
print(str1,file=writeFile)
writeFile.close()

my_file= open("my_file.txt","r")
print(my_file.read())


#B
with open("my_file.txt","a") as f:
 data1=f.read
 f.seek(0)
 f.write(str2+data1)
f.close()
print(my_file.read())


#C
str3 = my_file.readline()
str4 = my_file.readline()
for i in range (0,len(str3)):
    if (str4.rfind(str3[i], 0, len(str4))) == -1:
        print(str3[i],end="")


#D
str3 = my_file.readline()
str4 = my_file.readline()

for i in range (0,len(str4)):
    if (str3.rfind(str4[i], 0, len(str3))) == -1:
        print(str4[i],end="")



#PART-2
#Word Puzzle.

def Vowel_check(s):
    for i in range (0,len(s)):
        if (s.rfind('a',0,len(s))) != -1:
            if (s.rfind('e', 0, len(s))) != -1:
                if (s.rfind('i', 0, len(s))) != -1:
                    if (s.rfind('o', 0, len(s))) != -1:
                        if (s.rfind('u', 0, len(s))) != -1:
                            return True;

#The writing part and closing then.
str5 = input("\nEnter designated string:")
puzzle_filewrite= open("my_file2.txt","a")
print(str5,file=puzzle_filewrite)
puzzle_filewrite.close()

#The Reading file part with saving data inside another string.
puzzle_fileread = open("my_file2.txt","r")
saving_file = puzzle_fileread.read()

print("\nWords with the vowels in order are listed below: ")
for word in saving_file.split():
    if Vowel_check(word)==True:
        print("\t\t")
        print(word)



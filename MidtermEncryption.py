#CSC11300 Morning Session
#Mohammednaeem Meman, Tahsin Alam
#Encryption File
import random #imported random to generate the random values for the key

OriginalAlphabet = "abcdefghijklmnopqrstuvwxyz"

OriginalStr = "" #String that is going to be encrypted
NewAlphabet = "" #Alphabet that has been encrypted
NewStr = "" #String that has been encrypted

#Function to copy text from the Input file to OriginalStr
with open("Input.txt", "a+") as file:
	file.seek(0)
	OriginalStr = file.read()
n = 0
while n==0:
	n = random.randint(-1,25) #Number of shifts randomly chosen between [-1,25]

c = OriginalAlphabet[random.randint(0,25)] #Special character that is randomly and will stay the same when encrypted

#Function to create the key file
with open("Key.txt", "w") as file:
	file.seek(0)
	file.write(str(n)+"\n")
	file.write(c)
	
#Function to make create the NewAlphabet which takes the shifts and special character into account
for i in range(0,26,1):
	if OriginalAlphabet[i] == c:
		NewAlphabet = NewAlphabet + c.upper()
	else:
		NewAlphabet=NewAlphabet + OriginalAlphabet[(i+n)%26]

#Function to encrypt the string
OriginalStr = OriginalStr.lower()
OriginalList = OriginalStr.splitlines(True)
for i in range(0,len(OriginalList),1):
	for j in OriginalList[i]:
		for k in  range(0,26,1):
			if j == OriginalAlphabet[k]:
				NewStr = NewStr + NewAlphabet[k]
				break
		else:
			NewStr = NewStr + j

with open("EncryptedOutput.txt", "w") as file:
	file.seek(0)
	file.write(NewStr)


#CSC11300 Morning Session
#Mohammednaeem Meman, Tahsin Alam
#Decryption File
OriginalAlphabet = "abcdefghijklmnopqrstuvwxyz"
NewAlphabet = "" #Encrypted Alphabet which will be used to Decrypt the string

OriginalStr = "" #Encrypted String
NewStr = "" #Decrypted String

n = 0
c = ""

with open("Key.txt", "r") as file:
	file.seek(0)
	TempStr = file.read()
	TempList = TempStr.split()
	n = int(TempList[0])
	c = TempList[1]

with open("EncryptedOutput.txt", "r") as file:
	file.seek(0)	
	OriginalStr = file.read()
	
#Function to make create the NewAlphabet which takes the shifts and special character into account
for i in range(0,26,1):
	if OriginalAlphabet[i] == c:
		NewAlphabet = NewAlphabet + c.upper()
	else:
		NewAlphabet=NewAlphabet + OriginalAlphabet[(i+n)%26]

#Function to encrypt the string
OriginalList = OriginalStr.splitlines(True)
for i in range(0,len(OriginalList),1):
	for j in OriginalList[i]:
		for k in  range(0,26,1):
			if j == NewAlphabet[k]:
				NewStr = NewStr + OriginalAlphabet[k]
				break
		else:
			NewStr = NewStr + j
	
with open("DecryptedOutput.txt", "w") as file:
	file.seek(0)
	file.write(NewStr)
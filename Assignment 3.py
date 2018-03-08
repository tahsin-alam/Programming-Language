
#Tahsin Alam
#CS 113-Morning session.

#1.
def primenum(n):
    for i in range (2,n):
        if (n%i==0):
            return False
    return True

def primenumbers(n):
    for i in range(1, n + 1 ):
             if(primenum(i)==True):
                print(i,end=" ")

print("Listing prime numbers for given n numbers...")
primenumbers(21)

#2.
def primefactors(n):
    for i in range (2,n):
        if (n%i==0):
            return False
    return True
def listPrimeFactors(n):

            if (primefactors(n) == True):
                print(n, "=", n, "* 1")

            else:
                print(n, "=", end=" ")
                prime = 2
                while (n != 1):

                    if n % prime == 0:
                        n = n / prime
                        if (n == 1):
                            print(prime)
                            break
                        print(prime, "*", end=" ")

                    else:
                        while True:
                            prime += 1
                            if (primefactors(prime) == True):
                                break

print("\nListing prime factors for number n.....")
listPrimeFactors(675)

 #3.
def main():

    score = int(input("Please enter your score:"))
    if score > 100 or score < 0:
        print("Invalid score")
    elif score >= 90:
            print("Your grade is A")
    elif score >= 80:
                print("Your grade is B")
    elif score >= 70:
                    print("Your grade is C")
    elif score >= 60:
                        print("Your score is D")
    else:
                        print("You failed")

main()
#4.
def collatz(n):
        print(n, end=" ")
        while (n != 1):
            if (n%2==0):
                n = n / 2
            else:
                n = 3 * n + 1
            print(int(n), end=" ")
print("Listing the Collatz Conjecture starting from the given number n.....")
collatz(56)



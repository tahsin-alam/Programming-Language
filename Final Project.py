#Tahsin  Alam
#CS 11300
#Final Project
#Morning Session
#1.
class soldiers:
    def survivors(self,start,max):
        self.list=[]
        for i in range(0,max):
            self.list.append(i+1)
        while len(self.list)!=1:
            tmp=self.list[start]
            self.list.remove(tmp)
            start=start+1
            start=start%len(self.list)
        return self.list[0]

todo=soldiers()
init_survived=1
num=8
tmp=todo.survivors(init_survived,num)
print("Total survived soldiers:",tmp)


#2.
import random
def flips():
    return random.randint(0,1)
def HeadorTail():
    return random.randint(0,1)
def consecutive(s, list):
    temp = 0; result =0
    for i in range (0,len(list)):
        if list[i]==s:
            temp = temp+ 1
            result = max(result, temp)
        else:
            temp =0
    return result

n=10000
list=[]
for i in range (0,n):
    Choice = HeadorTail()
    if Choice==flips():
        list.append(1)
    else:
        list.append(0)

print("Number of Consecutive wins :", consecutive(1, list))
print("Number of Consecutive losses :", consecutive(0, list))

#3.
#Output of function 3a
#[[2, 3, 5], [5, 2, 3]]
#looks like the function will append 5 means the ending of the list begin  with 5 and beginning
# next list start with 5 returning a list of list.

#Function 3b returns permutation of numbers in terms of list and also returns a list of list.

#4.
def powerset(set):
    if len(set)<=1:
        return [[set[0]]] #if the size of set id <=1 return the set then.
    else:
        src=powerset(set[1:]) # compute power set of list excluding first element.
        src=[[set[0]]] + [[set[0]]+item for item in src] + src
        return src

#test powerset
set=['w','x','y','z']
print("Subset of given set:",powerset(set))

#5.
#Four OOP features
#a. Plolymorphism: Polymorphism is an important feature of class that is utilized when we have commonly
#named methods across classes or subclasses.A function wil be able to evaluate these ploymorphic
#methods without knowing which classes are invoked.
#Example: class player1():
#             def playsoccer(self):
#                   print("The player is playing soccer")
#           def playcricket(self):
#                   print("The player is playing crickt")
#         class player2():
#                def playsoccer(self):
#                   print("The player is playing soccer")
#               def playcricket(self):
#                   print(The player can not play cricket")
#           src=player1()
#           print(src.playcricket())
#
#           res=player2()
#           print(res.playcricket)
# #output
# The player is playing cricket
# The player can not play cricket

#b.
#Encapsulation: Hiding the design details to make the program more clearer and easily modified
#to the reader.The implementation means to stay the same just we are reorganizing the program
#hiding the details.
#Example: Class Person
#           def init(self, first_name):
#               self.first_name=first_name

#c.
#Inheritence:creating neting objects by inheriting the object characteristics while creating
#or over riding for this object.
#Example: class python
#            def init(self, no slides):
#                self.n=no_of_slides
#                 self.sides=[0 for i in range(no_of_slides)]
#               def inputSides(self):
#                self.sides = [float(input("Enter side ")
#This class has data attributes to store the number of sides, n and magnitude of each side as a list, sides.
#Method inputSides() takes in magnitude of each side and display properly.
#
#d. Classes: The collection of the objects can be said as a class. However class is something thats is always
#user defined. This is where from everything is declared and created.
#Example:  Class Animal
#               def herbivore(self)
#           #codes#
# Class animal can contain all the animal types inside it which are user defined data types.

#6.
#The "inspect" and "reflection" are the modules are usd to view the names of variables and functions.
#Yes, we can use these modules to view for all built in function.
#Reflection module example:PyObject*PyEval_getbuiltins()
#Inspection modules example: inspect.getmodulesname(path)
#An alternate way would be to use sys.builtin module names which returns a tuple of  strings.
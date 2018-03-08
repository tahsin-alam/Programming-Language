#Tahsin Alam
#Cs 113
#Morning session

#Part 1
#A. 42=n is not acceptable because a varibale name can not start with an integer. The left part is always
#variable name and the right part is the value being assigned.
#B. x=y=1 is acceptable since it assigning values and setting them equally.
#C. the program will still execute without any error but it gives you a warning.
#D.It gives you a syntax error.
#E. Since we didn't use any multiplication sign between them compiler gives us a name error.
#F. High level languages.
#G.it gives a syntax error.
#H. if we leave out the quatation marks it will gives us the message that the string is not defined.
#I. A python script is a written python codes wich you can save as a python file by adding .py  extension.
#J. High level programming languages.


#Part 2
#A
seconds=(42*60)+42;
print( seconds);
#B
import math
rad_str=4
volueme=4/3*math.pi*math.pow(rad_str,3)
print("The volueme of sphere with radius 4 is:" ,volueme)

rad_str=6
volueme=4/3*math.pi*math.pow(rad_str,3)
print("The volueme of sphere with radius 6 is:" ,volueme)

#C
print("Converted to Celsius we get:", (-40 -32)*5/9)
print("Converetd to Fahrenheit we get:",(-40*9/5)+32)

#D

V=3
volueme_prism= V*(2*V)*(3*V)
volueme_cube=math.pow(V,3)

print("Number of C that fits into R:",(volueme_prism/volueme_cube))
#calculated with different numbers. get 6 everytime.

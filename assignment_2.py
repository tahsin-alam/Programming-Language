#Tahsin Alam
#Morning session
#CS 113

#A
def minutes_to_miliseconds(mint_key):
 return mint_key*60000
mint_key=int(input("Enter amount of minute:"))
mile_key=minutes_to_miliseconds(mint_key)
print(mint_key,"minutes is equal to",mile_key,"mileseconds")

#B
def average_scores(first,second):
    return ( first+second)/2
first=int(input("Enter the first exam score: "))
second=int(input("Enter the second exam score: "))
average=average_scores(first,second)
print("avearge score is",average)

#C
import math
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))

roots= math.pow(b,2)-4*a*c
if roots>0:
 num_roots=2
 x1=(((-b)+math.sqrt(roots))/(2*a))
 x2 = (((-b) - math.sqrt(roots)) /(2*a))
 print("There are 2 roots",(x1,x2))

 if roots==0:
  num_roots=1
  z=(-b)/2*a
  print("There is only one root",z)

  if roots==0:
    print("No roots exists")
 if roots <0:
    print("No roots exists")
#D
 def distance_traveled(speed_kmh, time_h):
     return(speed_kmh*time_h)
 def average_speed(totaldis_km,totaltime_h):
     """find the average speed and retuens as meter/second."""
     return(totaldis_km/totaltime_h)*(1000/360)
#E
def kelvin_to_reaumur(kelvin_float):
 return (kelvin_float-273.15)*4/5
print("Convert kelvin to reaumur")
kelvin_float=float(input("Enter temp in kelvin:"))
rae_float=kelvin_to_reaumur(kelvin_float)
print(kelvin_float,"Kelvin converted to ",rae_float,"reaumur")

def reaumur_to_celcius(rae_float):
    return rae_float*5/4
print("Convert reaumur to celcius")
rae_float=float(input("Enter temp in raeumur:"))
cel_float=reaumur_to_celcius(rae_float)
print(rae_float,"Reaumur converted to",cel_float,"Celcius")

#F
n=3
cube_vol=math.pow(n,3)
marble_vol=4/3*math.pi*math.pow(n/4,3)
def marble_in_cube(cube_vol,marble_vol):
    return cube_vol/marble_vol
fits_in=marble_in_cube(cube_vol,marble_vol)
print(fits_in,"Marble can fit inside the cube")
print(round(fits_in)) ##rounding to the nearest full number.

#G
def first_type():
    print("^ - ^ - ^^ - ^ - ^^ - ^ - ^^ - ^ - ^^")

    def second_type():
        print("i     i     i     i     i")
        print("i     i     i     i     i")
        print("i     i     i     i     i")
        print("i     i     i     i     i")

    def all_together():
        for i in range(0,4):
            print (first_type())
            print(second_type())
    print(first_type())

    print(all_together())













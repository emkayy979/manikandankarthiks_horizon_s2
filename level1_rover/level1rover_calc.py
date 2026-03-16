import math

print("\n"*2)

print (" Rover motion calculator")
print("\n"*2)



#accepting the intial and final cordinates of the rover from the user

#use  try and except block to check if the input in numerical values or not.
try:
    x1= float(input("Enter the initial x position of the rover: "))
    y1= float(input("Enter the initial y position of the rover: "))
    x2= float(input("Enter the final x position of the rover: "))
    y2= float(input("Enter the final y position of the rover: "))

    #calculating the distance between the initial and final position of the rover using the distance formula
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx**2 + dy**2)


    #inputting motion parametres

    u=float(input("enter the intial velocity of the rover: "))
    a=float(input("enter the acceleration of the rover: "))
    if a <= 0:
        print("acceleration must be positive so that the rover can reach the target location")
        exit()

    v=float(input("enter the final velocity(max allowed speed) of the rover: "))
    if v < 0:
        print("Top speed cannot be negative, try again")
        exit()


#checking for value error 
except ValueError:
    print(" ERROR: Please enter numerical values, letters and symbols are not valid inputs.")
    exit()




#use motion paramteres given and motion in one dimension equations to find different values.
# use v^2-u^2=2as to find the s (distance) covered till max V is reached.

s= (v**2 - u**2)/(2*a)


if s < distance:
    #1. Time taken till it reaches v speed.
    t1 = (v - u) / a
    
    # 2. Time taken cruising in v speed till it reaches final destination.
    constant_speed_distance = distance - s
    t2 = constant_speed_distance / v

    total_time = t1 + t2

else:
 #rover doesnt achieve max speed before it hits its final destination. 
#use v^2-u^2=2as to find the velocity at the final destination.

 v_final_destination = math.sqrt(u**2+ 2*a*distance)
 total_time = (v_final_destination - u)/a


#print the results


print("\n"*2)
print("Distance to cover:", round(distance,2), "metres")

print("\n")
print("Total time taken to cover the distance :", round(total_time, 2), "seconds")

print("\n"*2)


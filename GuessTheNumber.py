#Mustafa Emir Utku 
#Guess the number


import random
#random number 0-9
x=random.randint(0,9)

#user input
print("please pick number (0-9)")
user=int(input())

#first choice is true 
if user==x:
 print ("you win")

#first choice is not true 
else:

#another choices are not true 
 while user<x or user>x:
  print("Wrong choose")
  print("please pick number (0-9)")
  x=random.randint(0,9) # every choices reset random number if you want delete it 
  user=int(input())
  
  #another choices are true 
  if user==x:
   print ("you win")
   break
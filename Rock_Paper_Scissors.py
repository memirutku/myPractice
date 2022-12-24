# NOTES
# random number(0,3){0,1,2} 
# choosing 1-Rock 2-Paper 3-Scissors
# 3**2= 9 different results
# win and lose in fuctions 

import random


randomNumber=random.randint(0,3)

print("Choose your move!(Rock,Paper,Scissors)")

# player input 
Player=input()

#dictionary
dictionariesMove={
"Rock":0,
"Paper":1,
"Scissors":2
}


#Random Number change to String in dictionary
for x in dictionariesMove:
    if randomNumber==dictionariesMove[x]:
       randomNumberString=x

#Player input change to number usin dictionary
for x in dictionariesMove:
    if Player==x:
       Player=dictionariesMove[x]



# function of all results

#equal
def equal():
    print("Equal!!!\nYou good but not enough\nTry again!\nI choose {} ".format(randomNumberString))
#win
def win():
    print("Congratulations!!!\nYou won\nI choose {} ".format(randomNumberString))
#lose
def lose():
    print("I'm sorry you don't enough good \nTry Again!\nI choose {} ".format(randomNumberString))



# rock-rock
if randomNumber==0 and  Player==0:
    equal()
# rock-paper
elif randomNumber==0 and  Player==1:
    win()
# rock-scissors
elif randomNumber==0 and Player==2:
    lose()
# paper-rock
elif randomNumber==1 and  Player==0:
    lose()
# paper-paper
elif randomNumber==1 and  Player==1:
    equal()
# paper-scissors
elif randomNumber==1 and  Player==2:
    win()
# scissors-rock
elif randomNumber==2 and  Player==0:
    win()
# scissors-paper
elif randomNumber==2 and  Player==1:
    lose()
# scissors-scissors
elif randomNumber==2 and Player==2:
    equal()
#
else: print("Try again")

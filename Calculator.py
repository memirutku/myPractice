# İclal Kurt and Mustafa Emir Utku 
# Basic calculator 

print("Please enter number:")

number1 = float(input()) 
number2 = float(input())

print("Please Choose operation")
print("1-addition"+"\n2-subtraction"+"\n3-multiplication"+"\n4-division")
choose=float(input())

#addition
if choose == 1:
 print(number1+number2)

#subtraction
elif choose == 2:
 print(number1-number2)

#multiplication
elif choose == 3:
 print(number1*number2)

#division
elif choose == 4:
 print(number1/number2)

else :
 print("invalid value")




 



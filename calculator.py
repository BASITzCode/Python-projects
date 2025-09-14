#Simple calculator 
#Displays a sort of menu for the user to choose the operation he wants to perform
print('1)Addition')                 #
print('2)Subtraction')
print('3)Multiplication')
print('4)Division')
calc = int(input( 'Enter the number of operation you want to perform : '))
if calc==1:
    num = float(input('Enter your 1st number : '))
    num1 = float(input('Enter your 2nd number : '))
    print('The sum of the numbers is :' , num+num1)
elif calc==2:
    num = float(input('Enter your 1st number : '))
    num1 = float(input('Enter your 2nd number : '))
    print('The subtraction of the numbers is :' , num-num1)
elif calc==3:
    num = float(input('Enter your 1st number : '))
    num1 = float(input('Enter your 2nd number : '))
    print('The product of the numbers is :' , num*num1)
elif calc==4:
    num = float(input('Enter your 1st number : '))
    num1 = float(input('Enter your 2nd number : '))
    if num1 ==0:
        print('Division by zero is not possible')
    else:
        print('The division of the numbers is :' , num/num1)
else:
        print('Invalid operation')

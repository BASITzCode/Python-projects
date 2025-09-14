#ToDoList in python
List=[]
print('Welcome to the ToDoList')
while True:
    print('-------------------------------Menu--------------------------------')
    print('1)Add a task')
    print('2)Remove a task')
    print('3)View the tasks')
    print('4)Exit')
    choice = int(input('Enter the number of operation you want to perform : '))
    if choice==1:
        List.append(input('Enter the task to add into the list : '))
        print('-------------------------------Task Added --------------------------------')
        print(f"Your List is : {List}")
    elif choice==2:
        List.remove(input('Enter the task to remove from the list : '))
        print('-------------------------------Task removed --------------------------------')
        print(f"Your List is : {List}")
    elif choice==3:
        print('----------------------',List,'----------------------')
    elif choice==4:
        break
    else:
        print('Invalid operation')
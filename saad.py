from random import randint 
List = randint(1, 1000)
Running = True
while Running :
    user = int(input('enter a number '))
    if List == user :
        print('victory')
        Running = False
    elif List < user :
        print('lower')
    elif List > user : 
        print('higher')

print('game over')
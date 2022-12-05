from random import randrange
computer_number = randrange(0,10)
chance = 5
has_won = False

print("--------------------------------------------------------Welcome------------------------------------------------------")
print("In this game , the computer will choose a number between 0 and 10  and your goal is to guess the number that it has chosen. \n You have only 5 chances ")
print("Let's Go!")
choose_number = int(input("Choose a number please "))
while (chance > 1) :
    if choose_number > computer_number:
        print('Choose a smaller number') 
        choose_number = int(input('Enter the number : '))
        chance -= 1
    
    if choose_number < computer_number:
        print('Choose a larger number') 
        choose_number = int(input('Enter the number :'))
        chance -= 1

    if choose_number == computer_number:
        print('You have Won') 
        has_won = True
        break
    
if has_won == False:
    print('Sorry Time out ,the number that the computer had chosen was: ', computer_number)     

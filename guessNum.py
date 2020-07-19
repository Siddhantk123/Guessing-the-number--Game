print("Hey!!! can you guess the number?")
print("You will be given 7 chance to win this game.")
print("Don't worry, we will give you a hint after every chance.")
print("For your convenience, I am keeping the range of number between 0 to 50. ")
print("Lets play....\n\n")

import random
num = random.randint(0,50)
#print(num) to check the number

chance=1
while 1:

    while(chance <= 7):
        userInput=int(input("\nEnter the number\n\n"))

        chanceleft=7-chance
        chance=chance+1 
        

        if(userInput>num):
            print("\nvalue is too high!!!, please enter smaller number")
            print(f"\nchance left={chanceleft}")
        elif(userInput<num):
            print(f"\nvalue is too low!!!, please enter greater number                  Chance left={chanceleft}")
            
        else:
            print("\nYou Won!!!")
            print("\nWant to play again? Press y else Press n")
            again=input()
            if again=='y':
                chance = 1
            else:
                break
           
    if(chanceleft==0):
        print("\nGame Over")
        print("\nWant to play again? Press y else Press n\n")
        again= input()
        if again=='y':
            chance = 1
        else:
            break



            
        









    

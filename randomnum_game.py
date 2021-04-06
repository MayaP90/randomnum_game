import random
computer=random.randint(1, 10) 
play_again = 'y'
while play_again == 'y':
    guess=int(input("Try to guess the number that is the same as the computer from 1 to 10:"))
    if guess > 10:
        print("Your number is too high for the range ")
    elif guess < 1: 
        print("Your number is low for the range") 
    elif guess==computer: 
        print("Good job your number is the same as the computer!") 
    else: 
        print("Sorry this is not the number, please guess again")
    play_again = input("Want to play again(y/n): ")
print("\n\nWELCOME TO GUESS THE NUMBER GAME!")
print("---------------------------------\n")
print("INSTRUCTIONS")
print("------------")
print("I will think of a number in the range of 1 to 50 inclusive. You need to guess that number. You will get 5 chances.\n")
print("Let's play!")
print("-----------")


#generate random number with random function
import random
random_no = random.randint(1,50)


#compare the user input with random number
#if input is greater than random number show 'high' and if less show 'low'
#if input equals random number show 'correct'
#run the whole thing in a loop and limit the guesses to 5
#show 'game over' after 5 incorrect guesses

Guess = False
i=1
a=5
while i < 6:

    user_input = int(input("Can you guess the number? "))
    if user_input == random_no:
        Guess = True
        break
    elif user_input > random_no:
        print("\nYour number is high!")
        print("---------------")
        print("Chances left:", a-i)
        print("---------------\n")
    else:
        print("\nYour number is low!")
        print("---------------")
        print("Chances left:", a-i)
        print("---------------\n")
    i+=1

if Guess == True:
    print("\nCORRECT\n")
    print("YOU WON!\n")
    print("CONGRATS! :D\n\n")
else:
    print("YOU LOST!\n")
    print("THE NUMBER WAS:", random_no )
    print("\nGAME OVER!\n\n")

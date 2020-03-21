#!/usr/bin/python3

'''
Problem-2 :
we take 3 inputs from user
 1. first number (int or float)
 2. second number (int or float)
 3. operator (string)
Output the result
(Must check invalid input)
'''



def main(): #defines the function, main(), as the collection of codes below

    print("\nAs-salamu-alaikum")
    print("\nWhat calculation do you want to perform?")
    print("\n1: Addition 2: Subtraction 3: Multiplication 4: Division") #Shows options
    calc_method = int(input("\nPlease select the method of calculation: ")) #Asks user input for the type of calculation to be performed

    #Operation = Addition, Subtraction, Multiplication, Division
    if calc_method == 1: #evaluates which operation to perform
        print(float(input("Please input 1st number")) + float(input("Please input 2st number"))) #Asks user input for 1st no. & 2nd no. and performs addition
    elif calc_method == 2:
        print(float(input("Please input 1st number")) - float(input("Please input 2st number"))) #Asks user input for 1st no. & 2nd no. and performs subtraction
    elif calc_method == 3:
        print(float(input("Please input 1st number")) * float(input("Please input 2st number"))) #Asks user input for 1st no. & 2nd no. and performs multiplication
    elif calc_method == 4:
        print(float(input("Please input 1st number")) / float(input("Please input 2st number"))) #Asks user input for 1st no. & 2nd no. and performs division
    else:
        print("Invalid input") #displays 'invalid input' if input is not any int between 1 and 4

    restart = input('Do you want to perform another calculation? y/n\n') #Asks user input to restart the program or exit
    if restart == 'y': #evaluates whether to restart or exit the program
        main() #calls the function, main(), and restarts the program
    else:
        print("\nJazakAllah Khair\n\n")
        exit() #exits the program

main() #calls the function, main(), and runs the program

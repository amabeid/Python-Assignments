print("\nHANGMAN\n")
print("o I will think of a word. I will name the category the word belongs to.")
print("o You need to guess what the word in the category is.")
print("o Only the vowels of the word will be shown. You need to guess the rest of the letters.")
print("o 5 incorrect guesses mean the game is over.\n")

#STEP-1 - MAKE A DICTIONARY OF WORDS

word_dict = {
"summer fruit" : ["jackfruit", "mango", "papaya", "lichi", "pineapple", "guava", "star fruit", "watermelon", "pomegranate", "lemon"],
"car brand" : ["toyota", "honda", "nissan", "mitsubishi", "ford", "kia", "mazda", "hyundai", "suzuki", "mercedes" ],
"flower" : ["water lily", "sunflower ", "jasmine", "night queen", "marigold", "hibiscus", "orchid", "rose", "gladiolus", "dahlia", "krishnachura" ],
"occupation" : ["dentist", "biotechnologist", "pilot", "carpenter", "archaeologist", "economist", "fire fighter", "programmer", "historian", "zoologist"]
}


#STEP-2 - GENERATE A RANDOM KEY-VALUE PAIR

import random

#genrate a random key
keys = list(word_dict)
random_key = random.choice(keys)

#generate a random value of the random key
random_value = random.choice(word_dict[random_key])

#print random_key
print(random_key + ":")


#STEP-3 - TAKE THE RANDOM VALUE AND PRINT ONLY THE VOWELS-AEIOU, AND PRINT UNDERSCORE IN PLACE OF OTHER LETTERS
#check if each ch in str equals aeiou
#if ch does not equal vowel, then append '_' to str_list1, otherwise append vowel to str_list1
#join the list of ch into a string and print the string (str1)

str = random_value
str_list = list(str)
vow = "aeiou"
vow_list = list(vow)

str_list1=[]
for i in str_list:
    check_vowel = False
    for j in vow_list:
        if (i == j):
            check_vowel = True
            break
    if (i == " "):
        str_list1.append(" ")
    elif check_vowel == False:
        str_list1.append("_")
    else:
        str_list1.append(i)

str1 = "".join(str_list1)
print(str1,"\n")


#STEP-4 - TAKE USER INPUT AND PRINT MODIFIED str1 (new_str)

#new_str is the random_value showing only the vowels
#take user user input
#create emtpy string list (new_strlist)
#iterate throught the index of str1; check if user input matches the chars in str (random_value)
#if matches replace "_" in str1 with user input, else keep the the chars unchanged
#print modified str1 (new_str)


#STEP-5 - RUN STEP-4 ITERATING N TIMES (n = infinite) and REPLACE str1 WITH new_str AT EACH ITERATION AFTER THE FIRST

#set counter to 0
#run step-4
#set str1=new_str
#the new_str prints the random_value with user_input if guess is correct
#increment counter by 1 to keep count of the number of times new_str is printed

count = 0
a=5
while True:
    user_input=input("Enter a letter:")
    #str
    #str1
    new_strlist = []
    for i in range(len(str1)):
        if user_input==str[i]:
            replace = str1[i].replace("_", user_input)
            new_strlist.append(replace)
            # print(replace)
        else:
            new_strlist.append(str1[i])
            # print(str1[i])

    new_str = "".join(new_strlist)
    print(new_str,"\n")

    str1=new_str
    count = count + 1
    # print(count)


#STEP-6 - LIMIT THE NUMBER OF GUESSES TO 5
#if user input is in str(random_value) and if new_str equals str, then break the infinite loop
#takeaway 1 from count to set counter to 0 each time user guesses the correct letter
#this allows to count the number of incorrect guesses only
#if user input is not found in str and if the number of incorrect gusses is 5 (count==5), then break the infinite loop

    Guess=True
    if user_input in str:
        if new_str==str:
            break
        count = count-1
    else:
        if user_input not in str:
            print("Wrong guess.")
            print("---------------")
            print("Guesses left:", a-count)
            print("---------------\n")
            if count==5:
                Guess=False
                break

if Guess==False:
    print("GAME OVER.\n")
    print("The word is:", random_value, "\n")
else:
    print("SOLVED!\n")

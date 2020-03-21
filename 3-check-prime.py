import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('abeid-d4-t1.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


#Returning True if a number taken from user input is prime
p = int(input('Enter number: '))
logger.info('user input:' + str(p))

def check_prime(p):
    res = True
    for i in range(2, p):
        if (p%i == 0):
            res = False
            break
    if res == False:
        logger.info('check_prime result:' + 'False')
        return False
    else:
        logger.info('check_prime result:' + 'True')
        return True

cal_value = check_prime(p)
print(cal_value)


# find_prime(num_list): #if input is [3,4,5,6,7,8,9], please return (3, 5, 7)
# print (find_prime([2,5,6,7,29,11]))


#Printing a list of prime numbers from list_num1
list_num1 = [3,4,5,6,7,8,9]
logger.info('input list-1:' + str(list_num1))

list_prime1 = []
for i in list_num1:
    check_prime = True
    for j in range(2, i):
        if (i%j == 0):
            check_prime = False
            break
    if check_prime == True:
        list_prime1.append(i)

print(list_prime1)
logger.info('list-1 prime numbers:' + str(list_prime1))


#Returning a list of prime numbers from list_num2
list_num2 = [2,5,6,7,29,11]
logger.info('input list-2:' + str(list_num2))

def find_prime(list_num2):
    list_prime2 = []
    for i in list_num2:
        check_prime = True
        for j in range(2, i):
            if (i%j == 0):
                check_prime = False
                break
        if check_prime == True:
            list_prime2.append(i)
    logger.info('list-2 prime numbers:' + str(list_prime2))
    return list_prime2

cal_value = find_prime(list_num2)
print(cal_value)

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0 and number <=10000:
    result= number % 10
    if result > 5:
       print("Last digit of {} is {} and is greater than 5".format(number ,result))
    elif result == 0:
        print("Last digit of {} is {} and is 0".format(number, result))
    elif result < 6 and result !=0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number,result))
if number < 0:
    result = -((abs(number))%10)
    if result < 6 and result !=0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number,result))    
    elif result == 0:
        print("Last digit of {} is {} and is 0".format(number, result))

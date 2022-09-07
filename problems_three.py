

# Problem 1 - Happy Numbers

"""
https://en.wikipedia.org/wiki/Happy_number 

A happy number is a number defined by the following process: 
Start with any positive integer
Replace the number by the sum of the squares of its digits
Repeat the process until the number equals 1. 


Write a method that determines if a number is happy or sad 

Example Input: 13
Example Output: "13 is a Happy Number!"

Example Input: 22
Example Output: "22 is a Sad Number :("
"""


def happy_number_checker(number_to_check):
    original_number = number_to_check
    while number_to_check != "1":
        new_integer = 0
        for each in number_to_check:
            square = int(each) * int(each)
            new_integer += square
        number_to_check = str(new_integer)
        if number_to_check == "1":
            print(f"{original_number} is a happy number! :)")
            break
        elif number_to_check == original_number or "4":
            print(f"{original_number} is a sad number :(")
            break




# Problem 2 - Prime Numbers

"""
A prime number is a number that is only divisible by one and itself. 
Write a method that prints out all prime numbers between 1 and 100  
"""


def print_prime_numbers():
    prime_numbers = [2, 3, 5, 7]
    for num in range(8, 100):
        for prime in prime_numbers:
            if num % prime == 0:
                break
            elif num % prime != 0 and prime == prime_numbers[-1]:
                prime_numbers.append(num)
            elif num % prime != 0:
                continue
    prime_numbers.insert(0, 1)
    print(prime_numbers)


# Problem 3 - Fibonacci

"""
A Fibonacci is a series of numbers in which each number is the sum of the two preceding numbers. 
The simplest is the series 1, 1, 2, 3, 5, 8, etc. 
Write a method that does the Fibonacci sequence starting at 1 

HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs 
"""


def fibonacci():
    pass

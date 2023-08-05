# Problem 1:
#
# factorial: a Python function that takes a positive integer
# as a parameter and calculates its factorial. The factorial of a number
# is the product of all positive integers less than or equal to that number.
# For example, the factorial of 5 is 5*4*3*2*1 = 120.
#
def factorial(Integer):

    if Integer ==0 or Integer==1:
        return (1)
    else:
        return (Integer * factorial(Integer-1))


# Problem 2:
#
# fizz_buzz: a Python function  that takes an integer n and for each integer
# from 1 to n it prints "Fizz" if the number is divisible by 3,
# "Buzz" if the number is divisible by 5,
# and "FizzBuzz" if the number is divisible by both 3 and 5.
# If the number is not divisible by 3 or 5, it should just print the number.
#
def fizz_buzz(n):

    if n%3==0 and n%5==0:
        for i in range(n):
            print(i,": FizzBuzz")
    elif n%3==0:
        for i in range(n):
            print(i,": Fizz")
    elif n%5==0:
        for i in range(n):
            print(i,": Buzz")

    else:
        print(n)

# Problem 3:
#
# char_frequency: a Python function that takes a string as input and
# returns a dictionary where the keys are characters and the values are the
# frequency of each character in the string.

def char_frequency (str):

    dict={}

    for i in str:
        if dict.get(i)==None:
            dict.setdefault(i,1)
        else:
            dict[i]+=1
    return dict
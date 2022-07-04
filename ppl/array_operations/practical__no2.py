i = 0


def whileLoop(i: int) -> int:

    while (i <= 10):
        print(i)

        i += 1

    else:

        print('Done While Loop')


def forLoop():

    for n in range(5, 10, 3):
        print(n)
    else:

        print('Done for Loop')


def find7InList():

    for n in range(0, 10, 1):

        if (n == 7):

            print("Found  7!")

            break
        print(n)
    else:

        print('Done for Loop')


''' A function for skiping the printing of even number and only print odd numbers in range give below '''


def skipEvenInList():

    for n in range(0, 10, 1):

        if (n % 2 == 0):

            continue
        print(n)
    else:

        print('Done for Loop')


# whileLoop(i=i)

# forLoop()

# find7InList()

# skipEvenInList()


# Program to print numbers from 25 to 50 using while and for loop

# Write a program to display numbers from 100 to 75 using while and for loop


def whileLoop2(i: int, n: int, increment: bool = False) -> int:

    if (increment == True):

        while (i <= n):
            print(i)

            i += 1
    else:

        while (i >= n):
            print(i)

            i -= 1


def forLoop2(i: int, n: int, increment: bool = False):
    if (increment == True):
        for n in range(i, n, 1):
            print(n)
    else :
        for n in range(i, n, -1):
            print(n)

# whileLoop2(i=75, n=100)
# whileLoop2(i=100, n=75, increment=False)

# forLoop2(i=75, n=100)
# forLoop2(i=100, n=75, increment=False)

''' 
'''

# user_val = int(input("Enter any integer value:"))

# def printUpToUserVal(val:int):
#     temp_num_inc = 0
#     temp_num_dec = val
#     while (temp_num_inc <= val):
#         print(temp_num_inc)
#         temp_num_inc += 1
#     print("---------------")
#     while (temp_num_dec >= 0):
#         print(temp_num_dec)
#         temp_num_dec -= 1

# printUpToUserVal(user_val)

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

even = []
odd = []

def printEvenAndOdd(start:int, end:int):
    temp_var = start
    sum = 0
    print("Even Numbers are: ", '\n')


    while (temp_var <= end):
        if (temp_var % 2 == 0):
            even.append(temp_var)
        else:
            odd.append(temp_var)
        sum += temp_var
        temp_var += 1
    
    print("Odd numbers are: ", '\n',odd)
    print("Even numbers are: ", '\n', even)
    print("Sum of numbers is: ", sum)

printEvenAndOdd(start, end)

# Q. Program to take start and end for the range of numbers and determine the total for the sum of numbers
num = int(input("Enter any integer number: "))


def addNum(num):
    sum = 0
    while (num > 0):
        digit = num % 10
        num = num // 10
        sum = sum + digit
    return sum


def reverseNumbers(num):
    n = num
    sum = 0
    while (n > 0):
        digit = n % 10
        n = n // 10
        sum = (sum * 10) + digit
    print(sum)


# Program to check if a given number is a palindrome or


def checkIfPalindrome(num, sum):
    if (num == sum):
        print("Int is palindrome")


def findFactorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial)


def checkIfPrime(num):
    for n in range(2, num):
        if (num % n == 0):
            print("Number is not prime")
            break
    else:
        print("Number is prime")


def checkIfPrimeWithWhile(num):
    n = num - 1
    while n >= 2:
        if (num % n == 0):
            print("Number is not prime")
            break
        n -= 1
    else:
        print("Number is prime")


def findFibonacciSeries(num):
    
    series = [0,3,5,6]
    n = 1
    n1 = 0
    n2 = 1
    while n <= num:
        n = n1 + n2
        n1 = n2
        series.append(n1)
        n2 = n
    print(series)


# reverseNumbers(num)
# checkIfPalindrome(num, sum)
# findFactorial(num)
# checkIfPrimeWithWhile(num)

findFibonacciSeries(num)
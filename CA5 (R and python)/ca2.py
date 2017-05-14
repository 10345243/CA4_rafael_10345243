import math

#using lambda() and map():
def add(list1, list2): #1
    return map(lambda x, y: x+y, list1, list2)

 
def divide(list1, list2): #2
    if list2 == 0:
        print ("Not possible")
    else: 
        return map(lambda x, y: x/float(y) if y!=0 else 'nan', list1, list2)
 
def square_root(list1): #3
    return map(lambda x: math.sqrt(x), list1)
 
def sin(list1): #4
    return map(lambda x: math.sin(x), list1)

def tan(list1): #5
    return map(lambda x: math.tan(x), list1)


def fac(list1): #6
    return map(lambda f: math.factorial(f), list1)
 
#using reduce() to check the smaller number of the list
def max(values): #7
    return reduce(lambda a, b: a if (a>b) else b, values)

 
#using filter() to check numbers of a list and return only odd numbers:
def odd_numer(list1): #8
    return filter(lambda x: x % 2, list1)


#list comprehension: converting a list of temperatures 
def to_fahrenheit(values): #9
    return [(float (9)/5*x +32) for x in values]
 

#generator: generating prime numbers
def isPrime(num): #10
    if(num==1):
        return False
    if(num==2):
        return True
    if(num%2==0):
        return False
    i = 3
    while(i<math.sqrt(num)+1):
        if num%i==0:
            return False
        i += 2
    return True

def getPrimes(n):
    yield 2
    i = 1
    while i <= n-2:
        i += 2
        if isPrime(i):
            yield i
            

 
 
 
#testing the 10 functions:
print ('Addition result = ', add([27, 95, 78, 9], [32, 9, 70, 9]))
print ('Division result = ', divide([34, 0, 4], [0, 66, -90]))
print ('Square root result = ', square_root([12, 25, 9]))
print ('Sine result = ', sin([90, 45, 60]))
print ('Tangent result = ', tan([30, -45, 160]))
print ('Factorial result = ', fac([1, 5, 6]))
print ('Max result = ', max([10, 78, 9, -12]))
print ('Odds result = ', odd_numer([1, 9, 36, 88, 79, 32, 79]))
print ('Fahrenheit result = ', to_fahrenheit([32, -5, 27.6, 37.8]))

#printing the prime numbers for n = 50:
p = getPrimes(50)
print ('Prime numbers: ')
for x in p:
    print (x)
print

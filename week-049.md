## [DAY-367] functions

make a fizzbuzz function that takes a parameter the final number to fizzbuzz to, also make another function to check if a number is prime, and print the prime numbers in the fizzbuzz function


```
def is_prime(n):
    if n== 0 or n == 1:
        return False
    for x in range(2,n):
        if n %x==0:
             return False
    return True
def fizzz(x):    
    for i in range(x):
        if i%15==0:
            print("fizzbuzz")
        elif i%5==0:
            print("buzz")
        elif i%3==0:
            print("fizzz")
        else:
            if is_prime(i):
                print("prime " + str(i))
            else:
                print(i)
fizzz(100000000000000)

```

## [DAY-368] functions

make a program that prints fizzbuzz or the area of the circle

> we are doing one small program per week, because high school in the netherlands starts at age 12, and its quite intense, so now we are taking it slow, this is the kind of program she can write by herself without help:

```
def fizzbuzz(n):
    for i in range(n):
        if i % 15 == 0:
            print("FIZZBUZZZ")
        elif i % 5 == 0:
            print("BUZZZZZ")
        elif i % 3 == 0:
            print("FIZZZZ")
        else:
            print(i)

def circumference(r):
    result = float(r)*2 * 3.14
    return result


ask = input("do u want fizzbuzz or area? ")
if ask == "fizzbuzz":
    a = input("what is the number")
    fizzbuzz(int(a))
elif ask == "area":
    re = input("what is the readius")
    v = circumference(re)
    print(v)
    
```
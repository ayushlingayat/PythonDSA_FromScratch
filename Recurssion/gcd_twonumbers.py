#Finding the gcd of two numbers

def gcdTwoNumbers(a,b):
    if b == 0:
        return a
    return gcdTwoNumbers(b,a%b)

def lcm(a,b):
    return a*b//gcdTwoNumbers(a,b)


print(gcdTwoNumbers(15,50))
print(lcm(15,50))
#ans ayega 5 okk

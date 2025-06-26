# n = 5
# i =1
#
# while i<=n:
#     print(i,end = " ")
#     i = i + 1

# now we will write this using recurssion

#print 1 to n using recursion
def printNumbers(i,n):
    #Recursion first thing is base case
    #base case
    if i > n:
        return

    #second is always the recursive case okk
    #recursive case
    print(i,end=" ")
    printNumbers(i+1,n)


printNumbers(1,10)

#print factorial of a number using recursion

def fact(n):
    #base case
    if n == 0:
        return 1
    return n * fact(n-1)

fact_of_four = fact(4)
print(fact_of_four,end=" \n")

fact_of_three = fact(3)
print(fact_of_three,end=" \n")

print(fact(2))

# write a recursive function to print 321 as output

def function_rev(n):
    #base case
    if n == 0:
        return
    print(n,end =" ")
    return function_rev(n-1)

function_output = function_rev(3)
print(function_output)


#joo command unexcuted phase mein atti in recurssion so vooh ek naa
#recursive stack mein chali jati okk

#function_rev Recursive stack one okk

def function_rev_recursivestack(n):
    #base case
    if n == 0:
        return

    function_rev_recursivestack(n - 1)
    print(n,end =" ")

    # 3 gaya in recursive stack
    # phir 2 gaya in stack
    # phir 1 gaya

    # phir 1 seeh ayya stack seeh bahar so print hoga 1
    # phir 2 and 3 print hoga in corresponding

function_output_recursivestack = function_rev_recursivestack(3)
print(function_output_recursivestack)




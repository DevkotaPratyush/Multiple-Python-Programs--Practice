#defining a function. showname- function (name)- parameters
def showname(name):
    age=10 #local variable
    print("My name is - " + name + " He is " + str(age) + " years old")

a="Pratyush" 
#Calling function with what you want to send to the argument(name)
showname(a)

#when a function is defined, variables are called parameters and when they are called they are called arguments


#positional argument- 

def showname2(*names):
    for index in range(len(names)):
        print(names[index])

showname2("Apple", "Banana", "Mango")

#default value 
def showname3(name="apple"):
    print("default value is - " + name)

showname3()

#return- 
def multiply(num1, num2):
    mul=num1*num2
    return(mul)

answer= multiply(1,2)

print(f"the multiplication result is: {answer}")

def activation(x):
    if x<0:
        return(0)
    else:
        return(1)
Value=activation(-2)
print(Value)

#yeild - continious returns- even multiple values
def producer():
    for num in range(0,10,1):
        if num%2==0:
            yield num

for n in producer():
    print(n) 


#recursion- 
def sum_recursion(n):
    #define the base line- WHEN TO STOP
    if n==0:
        return(0)
    else:
        return n + sum_recursion(n-1)
print(sum_recursion(5))

def process(txt, i):
 
    # base case - when to terminate
    if i == len(txt):
        return
 
    print(txt[i])
 
    # hop to the next character in the text
    process(txt, i+1)
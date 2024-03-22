a=0 
b=1
while a<100:
    print(a)
    a,b=b, a+b

#first 9 Fibonacci Numbers
print("The first 9 fibonacci numbers are- ")
a=0
b=1
for numbers in range(0,10):
    print(a)
    a=b
    b=a+b

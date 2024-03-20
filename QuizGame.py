print("Welcome to my Quiz!")
Playing=input("Do you Want to play? (Y/N) ")
if Playing.upper() != "Y":
    quit() 
print("Okay! Let's Start :) ")
Score=0
answer=input("Which is the highest Mountain of the World? ")
if answer.upper()== "EVEREST" : 
    print("Correct!")
    Score+=1
else: 
    print("Incorrect!") 

answer=input("What is the capital of Nepal? ")
if answer.upper()== "KATHMANDU" : 
    print("Correct!")
    Score+=1
else: 
    print("Incorrect!") 

answer=input("How many Districts are there in Nepal? ")
if answer.upper()== "77" : 
    print("Correct!")
    Score+=1
else: 
    print("Incorrect!") 

answer=input("How many states/ provinces are there in Nepal? ")
if answer== "7" : 
    print("Correct!")
    Score+=1
else: 
    print("Incorrect!") 

answer=input("What is the biggest festival of Nepal? ")
if answer.upper()== "DASHAIN" : 
    print("Correct!")
    Score+=1
else: 
    print("Incorrect!") 

print("You answered " + str(Score) + " questions correctly.")
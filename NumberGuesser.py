import random
top_of_range= input("Type a Number: ")
if top_of_range.isdigit(): 
    top_of_range=int(top_of_range)

    if top_of_range<=0 : 
        print("Please enter a digit greater than 0 next time")
        quit()
else:
    print("please type a number next time!")
    quit()
random_number=random.randrange(top_of_range)
guess=0

#continue= restarts the loop from top. break= ends the entire program
while True:
    guess+=1
    user_guess=input(" Guess the number between 0 to " + str(top_of_range)+" " )
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else: 
        print("Please enter a number next time.")
        continue
    if user_guess==random_number:
        print("YOU ARE CORRECT!")
        break
    elif user_guess> random_number: 
        print("Your guess was greater than the random number. Try Again!")
    else:
        print("Your guess was less than the random number. Try Again!")

print("You made it in ", guess, "attempts.")

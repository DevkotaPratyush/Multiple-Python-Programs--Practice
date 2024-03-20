

#Creating a function to view passwords
def view():
     with open('passwords.txt','r') as f:
         for line in f.readlines():
             data=line.rstrip()
             website, username,password=data.split('|')
             print("Website:",website, ",Username:",username, ",Password:", password)

#Creating a function to add passwords
def add():
    website=input('Enter the name of the website: ')
    name= input('Enter username for the website: ')
    pwd= input('Enter password you like to save: ')

# file handling- open password.txt qs "f" f is alias|| a= append(edit existing or create nonexistant) w= overright r=read
    with open('passwords.txt','a') as f:
        f.write(website + "|" + name + "|" + pwd+ "\n")

# asks if you want to add or view. if you hit q- it triggers break- so program ends. else it continues
while True:
    mode=input("Would you like to add or view your passwords? (view/ add) OR 'q' to quit ")
    if mode.upper()=="Q":
        break
    if mode.upper()=="VIEW":
        view()
    elif mode.upper()=="ADD":
        add()
    else:
        print("Invalide Choise.")
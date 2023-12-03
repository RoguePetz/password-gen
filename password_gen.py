import random
import string

print("Pick between INPUT, GENERATE, QUIT")
user_choice=input()

if user_choice.lower()== "quit":
    print("good bye")

elif user_choice.lower()== "input":
    password=input("password must be 12 digits and contain both numbers and alphabet")
    if len(password)==12 and password.isalnum() == True:
        print(password)
        print("password stored")
    else:
        print("password does not meet conditions")

elif user_choice.lower() == "generate":
    print("generating password")
    length= 12
    characters = string.ascii_letters + string.digits
    password = ''. join(random.choice(characters) for _ in range(length))
    print(password)
    print("password saved")
    
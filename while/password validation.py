# function check_password() that repeatedly asks the user to enter a password until they enter "python123"

def check_password():
    while True:
        password=input("enter password ")
        if password=="python123":
            print("access granted!")
            break
        else:
            print("wrong password")
            password=input("enter passwrod")






check_password()
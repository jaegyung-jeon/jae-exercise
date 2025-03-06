#function guess_number() that picks a random number 1-10.  user keep guessing until they get the correct one.
import random
def guess_number():
    ran_number=random.randint(1,11)


    while True:
        n=int(input("enter your name\n"))
        if ran_number<n:
            print("too high")

        elif ran_number>n:
            print("too low")

        else:
            print("correct")
            break




guess_number()
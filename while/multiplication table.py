#function. multiplication that prints the multiplication table for a given number n up to 10 using a while loop.

def multiplication_table():
    n = int(input("enter your number\n"))
    for a in range(1,11):
            print(f"{n}x{a}={n*a} ",end= "")
multiplication_table()
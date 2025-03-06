#write a function sum_numbers() that repeatedly asks the user for numbers and sums them. the function should stop when the user enters 0.

def sum_numbers():
    sum=0
    # n=int(input("enter your number"))
    while True:
        n=int(input("enter your number"))
        if n==0:
            break
        sum += n
    print(sum)


sum_numbers()

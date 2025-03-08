#function count_even_odd: asks the user for numbers until they enter -1.
# how many numbers were even and how many were odd.

def count_even_odd():


    counting_even = 0
    counting_odd = 0
    while True:

        number=int(input("enter a number: "))
        if number==-1:
            break

        elif number%2==0:
            counting_even+=1
        else:
            counting_odd+=1


    print(f"even number: {counting_even}")
    print(f"odd number: {counting_odd}")







count_even_odd()
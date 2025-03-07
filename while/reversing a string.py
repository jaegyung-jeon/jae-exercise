#function reverse_string(s) that reverses a given string using a while loop instead of python's built-in methods.

def reverse_string():
    letter=input("input: ")

    num=len(letter)-1
    while num>=0:
        print(letter[num],end="")
        num-=1
    print()

reverse_string()







#function reverse_string(s) that reverses a given string using a while loop instead of python's built-in methods.

def reverse_string():
    letter=input("input: ")
    counter=0
    lastindex=len(letter)-1
    while counter<=lastindex :
        print(letter[counter],end="")
        counter+=1


        
    print()

reverse_string()







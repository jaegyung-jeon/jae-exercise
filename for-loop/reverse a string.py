# Take a string as input and print it in reverse using a for loop.

letter=input("type your letters\n")

for i in range(-1,-len(letter)-1,-1):
    print(letter[i],end="+")

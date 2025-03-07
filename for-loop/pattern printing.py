# print the following pattern using nested for loops
# *
# **
# ***
# ****
# *****


for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()
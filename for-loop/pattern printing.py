# print the following pattern using nested for loops
# *
# **
# ***
# ****
# *****


for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print()
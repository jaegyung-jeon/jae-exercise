#sum of digits
# take an integer as input and calculate the sum of its digits using a for loop
num=str(input("input the number that you wnat to calculate\n"))
sum=0
for i in num:
    sum+=int(i)
print(sum)
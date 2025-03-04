# Count the number of vowels in a given string using a for loop.

name=input("type any letters\n")
vowel=["a","e","i","o","u"]
sum=0
for i in name:
    if (i in vowel):
        sum+=1
print(sum)

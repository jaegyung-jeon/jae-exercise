import random
word_list=["jae","heesoo","heekyung"]
name=random.choice(word_list)
print(name)
a=len(name)
placeholder=""
for i in range(a):
    placeholder+="_"
print(placeholder)


guess=input("guess the letter ").lower()
answer=""
for letters in name:
    if letters == guess:
        answer+=guess

    else:
        answer+="_"

print(answer)
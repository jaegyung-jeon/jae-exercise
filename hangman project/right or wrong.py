import random
word_list=["jae","heesoo","heekyung"]
name=random.choice(word_list)
print(name)

while True:
    guess=input("guess the letter ")
    if guess in name:
        print("right")
    else:
        print("wrong")
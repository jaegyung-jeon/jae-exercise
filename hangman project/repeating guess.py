import random
word_list=["jae","heesoo","heekyung"]
name=random.choice(word_list)
print(name)
a=len(name)
placeholder=""
for i in range(a):
    placeholder+="_"
print(placeholder)

correct_answer=[]


while True:
    guess = input("guess the letter ").lower()
    answer = ""
    correct_answer.append(guess)
    for letters in name:
        if letters in correct_answer:
            answer+=letters

        else:
            answer+="_"
    print(answer)

    
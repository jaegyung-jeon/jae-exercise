stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']






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



lives = 6
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

    if guess not in name:
        lives-=1
        print(stages[lives])

    if lives == 0:
        print("you lose")
        break

    if answer==name:
        print("game over")
        break


import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

question=input("do you want to play blackjack? type 'y' or 'n': ")
user_card_list=[]
user_score=0
computer_card_list=[]
if question=="y":
    print(art.logo)

    computer_card_list.append(random.choice(cards))

    for i in  range(3):
        user_card_list.append(random.choice(cards))
        user_score+=user_card_list[i]

    print(f"your cards: {user_card_list}, current score: {user_score}")
    print(f"computer's first card: {computer_card_list}")

    question_2=input("type y to get another card, type n to pass: ")
    if question_2=="y":
        user_card_list.append(random.choice(cards))
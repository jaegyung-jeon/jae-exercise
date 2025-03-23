# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary




















def find_highest_value(dictionary):
    highest_dic_value=0
    winner=""
    for bidder in dictionary:
        if dictionary[bidder]>highest_dic_value:
            highest_dic_value=dictionary[bidder]
            winner=bidder
    print(f"the winner is {winner} with the {highest_dic_value}")



bid_dictionary={}
while True:
    name=input("what's your name: ")
    bid=int(input("enter your $: "))
    bid_dictionary[name]=bid
    question=input("are there any other bidders? type 'yes' or 'no' ")
    if question=="no":
        find_highest_value(bid_dictionary)
        break

    elif question=="yes":
        print("\n"*10)
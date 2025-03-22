alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt():
    original_text=input("type your text: ")
    shift_amount=int(input("how many do you want to shift: "))

    after_text = ""
    for i in original_text:
        number=alphabet.index(i)+shift_amount
        after_text+=alphabet[number]
    print(after_text)


















encrypt()
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    output_text = ""

    for letter in text:
        if letter not in alphabet:
            output_text += letter

        if direction == "decode":
            shift *= -1

        shifted_position = alphabet.index(letter) + shift
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]


print(f"Here is the {direction}d result: {output_text}")

# ------------------------------------------------------------------------------


while True:
    caesar()
    restart = input("do you want to go back to restart?: ")
    if restart == "no":
        print("thanks for your dumb ass fuck job")
        break

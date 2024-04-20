from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(direction1, text1, shift1):
    new_word = ""
    if direction1 == "decode":
        shift1 *= -1
    for letter in text1:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift1        # making shift
            new_word += alphabet[new_position]      # making new word
        else:
            new_word += letter
    print(f"The {direction1}d text is {new_word}")


cont = True
print(logo)
while cont:
    direction = input("Enter 'encode' or 'decode' to decrypt:\n")
    text = input("Enter your message:\n").lower()
    shift = int(input("Enter the no. of shift:\n"))

    shift %= 25     # when shift is in large no.
    caesar_cipher(direction, text, shift)
    continue_encrypt = input("Do you want to continue Type 'yes' else Type 'no'\n")
    if continue_encrypt == "no":
        cont = False
        print("GoodBye")

from caesar_cipher import caesar

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    if restart.lower() != "yes":
        should_continue = False
        print("Goodbye!")
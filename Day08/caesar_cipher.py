alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    result = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = (position + shift) % 26
            elif direction == "decode":
                new_position = (position - shift) % 26
            result += alphabet[new_position]
        else:
            result += letter
    print(f"The {direction}d text is: {result}")

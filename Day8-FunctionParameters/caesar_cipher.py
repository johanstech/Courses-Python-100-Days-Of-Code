from caesar_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

ciphering = True

while ciphering:
    direction = input(
        "Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    def caesar_cipher(shift_amount, text, cipher_direction):
        if cipher_direction == "decode":
            shift_amount *= -1
        cipher_text = ""
        for char in text:
            if char in alphabet:
                index = alphabet.index(char)
                cipher_index = index + shift_amount
                cipher_text += alphabet[cipher_index]
            else:
                cipher_text += char
        print(f"The {cipher_direction}d text is: {cipher_text}")

    if direction != "encode" and direction != "decode":
        print("You fucked up...")
    else:
        caesar_cipher(shift_amount=shift, text=message,
                      cipher_direction=direction)

    again = input("Again? y/n\n").lower()
    if again == "n":
        ciphering = False

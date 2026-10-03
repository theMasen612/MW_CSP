#MW cipher
direction = input("Do you want to (E)ncode or (D)ecode: ")

message = input("What is your message: ")

shift = int(input("how much do you want to shift: "))


def caesar_shift(message, shift):

    new_message = ""

    for letter in message:
        if letter.isalpha():
            number = ord(letter)
            number = number + shift

            if letter.isupper():
                if number > 90:
                    number = number - 26
                if number < 65:
                    number = number + 26
            else:
                if number > 122:
                    number = number - 26
                if number < 97:
                    number = number + 26

            letter = chr(number)

        new_message = new_message + letter

    return new_message


if direction == "E":
    message = caesar_shift(message, shift)
    print("Your encrypted message is:", message)

else:
    message = caesar_shift(message, -shift)
    print("Your decrypted message is:", message)

#MW cipher
direction = input("would you like to (E)ncrypt or (D)ecrypt a message?: ").upper()
message = input("enter your message: ") 
shift = int(input("enter a shift amount: "))
if direction == "E":
    newmessage = ""
    for letter in message:
        if letter.isalpha():
            num = int(ord(letter))
            new =chr(shift + num)

        newmessage = newmessage + letter

    print(newmessage)
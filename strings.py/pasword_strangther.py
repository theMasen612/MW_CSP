# MW pasword strangthener
password = input("Enter a password: ")

length = False
uppercase = False
lowercase = False
number = False
symbol = False

if len(password) >= 8:
    length = True

if any(letter.isupper() for letter in password):
    uppercase = True

if any(letter.islower() for letter in password):
    lowercase = True

if any(letter.isdigit() for letter in password):
    number = True

if any(letter in "!@#$%^&*" for letter in password):
    symbol = True

score = 0

if length:
    score += 1
if uppercase:
    score += 1
if lowercase:
    score += 1
if number:
    score += 1
if symbol:
    score += 1

if score == 5:
    strength = "Strong"
elif score >= 3:
    strength = "Medium"
else:
    strength = "Weak"

print("\nPassword:", password)
print("Length:", length)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Number:", number)
print("Symbol:", symbol)
print("Strength:", strength)

if strength != "Strong":
    print("\nYou are missing:")

    if length == False:
        print("- At least 8 characters")

    if uppercase == False:
        print("- An uppercase letter")

    if lowercase == False:
        print("- A lowercase letter")

    if number == False:
        print("- A number")

    if symbol == False:
        print("- A symbol")
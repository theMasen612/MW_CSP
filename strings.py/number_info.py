# MW, number information 
for number in range(1, 21):
    if number % 2 == 0:
        if number % 5 == 0:
            print(number, "is even and divisible by 5")
        else:
            print(number, "is even and not divisible by 5")
    else:
        if number % 5 == 0:
            print(number, "is odd and divisible by 5")
        else:
            print(number, "is odd and not divisible by 5")

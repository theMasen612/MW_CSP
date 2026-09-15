# M,S fixing imputs 

# when you want a number 
while True:
    name = input("tell me your name: ").title().strip()
    if name.isnumeric():
        print("Thats wrong you are stupid I said word not number try again")
    elif " " in name:
        print("are you sure your not stupid, i asked for a word not a number try again")
    else:
        print(f"I like your name but it took way to long to get it right {name}")
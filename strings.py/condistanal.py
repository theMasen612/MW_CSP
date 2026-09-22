# MW condistanal notes

military_time = 900

if military_time > 600:
    print("Its to early go to bed!!!!!!!")
elif military_time < 900:
    print("good morning!")
elif military_time < 1200:
    print("good morning! you should be at school!")
elif military_time< 1700:
    print("good afternoon")
else:
    print("good evening")

    #nesting condistanal 

day = "saturday"
time = 900

if time > 900 and time < 1600:
    if day != "saturday" or day != "sunday":
        print("you should be at school!")
    else:
        if time > 1200:
            print("good afternoon!")
        else:
            print("good morning!")
else:
    print(" you are not requiared to be at school")

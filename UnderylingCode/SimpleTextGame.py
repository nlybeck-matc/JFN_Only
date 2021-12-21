#!/usr/bin/env python3

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2 or door #3""")

door = input("->")

# == Door Number 1 logic =====================
if door =="1":

        print("There's a giant bear here eating a cheese cake.")
        print("What do you do?\n")

        print("1. Take the cake.")
        print("2. Scream at the bear.")

        #== Bear logic =======================
        bear = input("->")

        if bear =="1":
                print("1) The bear eats your face off. Good job!")
        elif bear =="2":
                print("2) The bear eats your legs off. Good Job!")
        else:
                print(f"N)Well, doing {bear} is probably better.")
                print("Bear runs away.")

#== Door Number 2 Logic ======================
elif door =="2":
        print("You stare into the endless abyss at Cthulu's retina. \n")

        print("1. Blueberries.")
        print("2. Yellow jacket clothespins.")
        print("3. Understanding revolvers yelling melodies.")

        #== Insanity Logic ===================
        insanity = input("->")

        if insanity == "1" or insanity =="2":
                print("1) Your body survives powered by a mind of jello.")
                print("1) Good Job!")
        else:
                print("N) The insanity rots your eyes into a pool of muck.")
                print("N) Good job!")

#== Door Number 3 Logic =====================
elif door =="3":
        print("You are face to face with Obiwan Kenobi.\n")

        print("1. Ask him to sponsor your race.")
        print("2. Tell him you're protecting Padme on Naboo.")
        print("3. Face him on Mustafar.")

        #== Obiwan Logic ====================
        obiwan = input("->")

        if obiwan =="1":
                print("1) Now this is pod racing!")
                print("1) You win the race and get to become a Jedi. Wooh!")
        if obiwan =="2":
                print("2) You have to tell Padme you don't like sand.")
                print("2) She actually falls in love with you. Nice!")
        if obiwan =="3":
                print("3) He cuts your limbs off and you scream 'I HATE YOU!' at him.")
                print("3) Congrats Darth Vader!")
else:
        print("You did not select a door??? Good call :)")

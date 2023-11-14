answer = input("what you like to play?(yes/no)")
if answer.lower().strip() =="yes":
    answer = input("You have three tracks to reach the palace and you have weapons and two lives ,"
                   "would you like track1 or track2 or track3?").lower().strip()
    if answer == "track1":
        answer = input("you encounter a monster,would you like to attack or die.")

        if answer == "attack":
            print("Good choice,you finish the monster using the swords")
            print("wonderful ,now your way is easy")
        else:
            print("Only one life is left!!")

    elif answer == "track2":
        answer = input("Trains are coming opposite,would you like to jump or die.")

        if answer == "jump":
            print("Good choice,you successfully jumped on train  using jump stick ")
            print("great,now your way is easy")
        else:
            print("you lost one life")

    elif answer == "track3":
        answer = input("You fall into the pit ,you got hurt.you can use ladder or die")
        if answer == "ladder":
            print("Great choice")
        else:
            print("not the good choice,you have another life")
    else:
        print("Invalid choice,you lost!")

else:
    print("That's too bad")
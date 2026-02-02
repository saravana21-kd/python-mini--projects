print('''
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#''')
print("Welcome to Death or Life Game.")
print("Your mission is to find the Door.")

choice1 = input("You are in a room.where do you want to go?\n\t"
                "Type : \"Door 1\" \"Door 2\" \"Door3\"?").lower()

if choice1 == "door1" or choice1 == "door 1":
    print("You entered into Monster Room. GAME OVER")
elif choice1 == "door3" or choice1 == "door 3":
    print("You entered into Burning Room. GAME OVER")
elif choice1 == "door2" or choice1 == "door 2":
    print("You entered into the next room.")
    choice2 = input("where do you want to go?\n\t"
                "Type : \"Door 1\" \"Door 2\"?").lower()
    if choice2 == "door 1" or choice2 == "door1":
        choice3 = int(input("how many continents are there in the world?"))
        if choice3 == 7:
            print("You moved to a next room.")
            choice5 = (input("where do you want to go?\n\t"
                             "Type : \"Door 1\" \"Door 2\"?")).lower()
            if choice5 == "door 2" or choice5 == "door2":
                print("You moved to a next room.")
                choice6 = (input("where do you want to go?\n\t"
                                 "Type : \"Door 1\" \"Door 2\"?")).lower()
                if choice6 == "door 2" or choice6 == "door2":
                    print("You moved to a next room.")
                    choice7 = (input("where do you want to go?\n\t"
                                     "Type : \"Door 1\" \"Door 2\"?")).lower()
                    if choice7 == "door 1" or choice7 == "door1":
                        print("You moved to a next room.")
                        football = input("Who is Goat in football?\n\t").lower()
                        if football == "ronaldo":
                            print("ongratulations! YOU WIN 🎉")
                    if choice7 == "door 2" or choice7 == "door2":
                        print("You moved to a next room.")
                        cricket = input("Who is goat in cricket?\n\t").lower()
                        if cricket == "dhoni":
                            print("ongratulations! YOU WIN 🎉")
                else:
                    print("You entered into the monster room.GAME OVER")

            elif choice5 == "door 1" or choice5 == "door1":
                print("You entered into Monster Room. GAME OVER")
            else:
                print("Type error! Retry...")

    elif choice2 == "door 2" or choice2 == "door2":
        conti = int(input("How many planets are in the solar system?"))
        if conti == 8:
            print("You moved to a next room.")
            choice4 = (input("where do you want to go?\n\t"
                "Type : \"Door 1\" \"Door 2\"?")).lower()
            if choice4 == "door1" or choice4 == "door 1":
             moon = int(input("How many moons does jupiter have?"))
             if moon == 95:
                 print("ongratulations! YOU WIN 🎉")
             else:
                 print("You lose this GAME")
            else:
                print("You lose this GAME")
else:
    print("Invalid choice. Restart the game.")
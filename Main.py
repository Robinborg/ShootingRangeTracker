# Application for shooting range
'''
Create a program that works for shooting ranges.
- Starting score of 75
- 5 rounds for each platform of 5, with a maximum of 5 people
    - 5 rounds
    - 5 switches
    - 1-5 players
- ability to change the input if an error occurs
- Graphical interface, with input
- Collect and send the data to an email address

'''
# Starting score
score = 75

# List of players
players_playing = []
rounds = 0


# change the results according to new input

running = True
while running:
    for rounds in range(0, 6):
        if rounds == 0:
            print("Welcome to the shooting range")
            print("This is round number " + str(rounds) + " please start")
            print("Choose the amount of players")
            playerInput = input("How many are shooting: ")
            for elem in playerInput:
                players_playing.append(elem)
            input("what did you score?: ")
            print(score)

        elif rounds >= 1:
            input("what did you score?: ")
            print(score)
        elif input == "green, Green":
            break
        elif rounds > 0:
            print("This is round number " + str(rounds) + " good luck")
            color = input("What did you score?: ")
            if color == "Red":
                score -= 3
                print(score)
            elif color == "Orange":
                score -= 1
                print(score)



    print("This is the " + str(rounds) + " round")






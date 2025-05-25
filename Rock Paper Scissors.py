import random
options=["rock", "paper", "scissors"]

#I decided on dividing the different parts of it into function blocks.
#Makes it look cleaner and easily expandable in the future.

#round logic
def baseround():

    choice=input("Choose: ").lower()

    if choice=='end':
        return 'end'
    elif choice not in (options):
        print("Invalid input.")
        return 'Invalid'
    
    compchoice=random.choice(options)
    if choice==compchoice:
        print(f"The computer chooses {compchoice} too\nIt's a tie!!")
        return 'tie'
    elif(
    (choice=='rock'and compchoice=='scissors')or
    (choice=='paper'and compchoice=='rock')or
    (choice=='scissors'and compchoice=='paper')
    ):
        print(f"The computer chooses {compchoice}\nYou win!!")
        return 'player'
    else:
        print(f"The computer chooses {compchoice}\nThe computer wins!!")
        return 'computer'

#mode selection logic   
def modeselect():
    while True:
        print("Choose a game mode:\n" 
            "1. Classic Endless\n" 
            "2. Best-of-N\n" 
            "3. Knockout\n")
        modeinp=input("Pick the number beside your desired game mode: ")

        if modeinp == '1':
            return 'endless', None
        elif modeinp == '2':
            while True:
                target = input("Enter score limit: ")
                if target.isdigit() and int(target) > 0:
                    return 'knockout', int(target)
                else:
                    print("Invalid number for knockout mode. Please enter a positive integer")
        elif modeinp == '3':
            while True:
                target = input("Enter total number of rounds: ")
                if target.isdigit() and int(target) > 0:
                    if int(target)%2==0:
                        print("Choosing an even number might result in a tie.")
                    return 'bestof', int(target)  
                else:
                    print("Invalid!! Please enter a positive integer.")
        else:
            print("Invalid mode selection. Please try again.")

#base game logic
def basegame(mode, target=None):
    compwins = 0
    plwins = 0
    tiecount = 0
    rnd = 1
    print("\nEnter rock/paper/scissors or 'end' to quit")
    if mode=='endless':
        while True:
            print(f"\nRound {rnd}")
            result = baseround()  

            if result == 'end':
                break
            elif result == 'Invalid':
                continue
            rnd += 1
            if result == 'tie':
                tiecount += 1
            elif result == 'player':
                plwins += 1
            elif result == 'computer':
                compwins += 1
        if plwins > compwins:
            print("\nWell played twin!! You were leading when you quit :)")
        elif compwins > plwins:
            print("\nSneaky of you to quit when the computer was winning hahahahahaha!!")
        else:
            print("\nYou and the computer were tied at the end. PERFECTION!!!")

    elif mode == 'knockout':
        while plwins < target and compwins < target:
            print(f"\nRound {rnd}")
            result = baseround()
            if result == 'end':
                break
            elif result == 'Invalid':
                continue
            rnd += 1
            if result == 'tie':
                tiecount += 1
            elif result == 'player':
                plwins += 1
            elif result == 'computer':
                compwins += 1  
        if plwins > compwins:
            print("\nCongrats twin!!\n"
                "You won the game!!")
        elif compwins > plwins:
            print("\nYou lost hahahahahahha\n"
                "The computer won the game:(")
    
    elif mode == 'bestof':
        totalrounds = target
        while rnd <= totalrounds:
            print(f"\nRound {rnd} of {totalrounds}")
            result= baseround()
            if result == 'end':
                break
            elif result == 'Invalid':
                continue
            rnd += 1
            if result == 'tie':
                tiecount += 1
            elif result == 'player':
                plwins += 1
            elif result == 'computer':
                compwins += 1
        print("\n<<<Game Over>>>")
        if plwins > compwins:
            print("\nYou won the series dawg!!")
        elif compwins > plwins:
            print("\nlmfaooo the computer won the series :(")
        else:
            print("\nThe series ended in a sweet tie!!")


    print("\nScoreboard:")
    print(f"You: {plwins}")
    print(f"Computer: {compwins}")
    print(f"Ties: {tiecount}")
    total = plwins + compwins + tiecount
    if total > 0:
        win_percent = (plwins / total) * 100
        print(f"You won {round(win_percent, 2)}% of the rounds!")

#gamerunner    
if __name__ == "__main__":
    print("Rock! Paper! Scissors!\n")
    mode, target = modeselect()
    basegame(mode, target)
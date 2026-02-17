import random
import os

def difficultySelection ():
    print(UNDERLINE + "Please Choose Your Difficulty\n" + RESET)
    print(GREEN + "1. Easy")
    print(YELLOW + "2. Medium")
    print(RED + "3. Hard\n" + RESET)
    difficulty = input("Please Enter 1, 2, or 3: ")
    if difficulty not in ["1", "2", "3"]:
        print("That choice is invalid, please try again\n")
        difficultySelection()
    
    return difficulty

def randomNumsGenerator(dif):
    
    num1 = 0
    num2 = 0
    
    if dif == "1":
        num1 = random.randint(1, 100)
        if num1 > 54:
            num2 = random.randint(1, num1 - 50)
        elif num1 < 46:
            num2 = random.randint(num1 + 50, 100)
        else:
            choice0 = random.randint(1,2)
            if choice0 == 1:
                num2 = random.randint(1,10)
            else:
                num2 = random.randint(90, 100)

    if dif == "2":
        num1 = random.randint(1, 100)
        if num1 > 69:
            num2 = random.randint(num1 - 50, num1 - 25)
        elif num1 < 31:
            num2 = random.randint(num1 + 25, num1 + 50)
        elif 30 < num1 < 50:
            choice1 = random.randint(1,2)
            if choice1 == 1:
                num2 = random.randint(num1 + 25, num1 + 50)
            else:
                num2 = random.randint(1, num1 - 25)
        elif 50 < num1 < 70:
            choice2 = random.randint(1,2)
            if choice2 == 1:
                num2 = random.randint(num1 - 50, num1 - 25)
            else:
                num2 = random.randint(num1 + 25, 100)
        else:
            choice3 = random.randint(1,2)
            if choice3 == 1:
                num2 = random.randint(1, 25)
            else:
                num2 = random.randint(75, 100)

    if dif == "3":
        num1 = random.randint(1, 100)
        if num1 > 89:
            num2 = random.randint(num1 - 10, num1 - 5)
        elif num1 < 11:
            num2 = random.randint(num1 + 5, num1 + 10)
        else:
            choice4 = random.randint(1,2)
            if choice4 == 1:
                num2 = random.randint(num1 + 5, num1 + 10)
            else:
                num2 = random.randint(num1 - 10, num1 - 5)

    return num1, num2

def gameLogic(n1, n2, guess):

    if guess == n2:
        return "lost"
    
    if guess == n1:
        return "won"

    if guess > n1:
        return "lower"

    if guess < n1:
        return "higher"

def clearScreen():
    os.system("cls")

def centerText(text):
    width = os.get_terminal_size().columns
    padding = (width - len(text)) // 2
    print(" " * padding + text)

#FORMATTING
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

#COLORS
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

clearScreen()
centerText(BOLD + CYAN + "Welcome to WrongNumber!\n" + RESET)

while True:    
    difficulty = difficultySelection()
    winNum, loseNum = randomNumsGenerator(difficulty)
    i = 1

    while i < 8:
        guess = input("Please Enter Your Guess: ")
        i += 1
        decision = gameLogic(winNum, loseNum, int(guess))
        if decision == "lost":
            clearScreen()
            centerText(BOLD + RED + "You guessed the wrong number, you lose!" + RESET)
            break
        if decision == "won":
            clearScreen()
            centerText(BOLD + GREEN + "You guessed the right number, you win!" + RESET)
            break
        if decision == "lower":
            print("Your guess was to high, try again")
            continue
        if decision == "higher":
            print("Your guess was too low, try again")
            continue
        print(decision)

    if i > 7:
        clearScreen()
        centerText(RED + "You ran out of guesses, game over\n")
        centerText(CYAN + "The winning number was " + winNum + "\n" + RESET)
    
    print(UNDERLINE + "Please Choose an Option\n" + RESET)
    print("1. Play Again")
    print("2. End Gamee\n")
    selection = input("Please Enter 1 or 2: ")
        
    if selection == "1":
        clearScreen()
        continue
    if selection == "2":
        break
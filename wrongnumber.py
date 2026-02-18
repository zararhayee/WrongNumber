import random
import os

#Custom data type for the win and lose numbers
class NumberPair:
    def __init__(self, win, lose):
        self.win = win
        self.lose = lose

#Allows user to decide difficulty
def difficultySelection ():
    print(UNDERLINE + "Please Choose Your Difficulty\n" + RESET)
    print(GREEN + "1. Easy")
    print(YELLOW + "2. Medium")
    print(RED + "3. Hard\n" + RESET)
    difficulty = input("Please Enter 1, 2, or 3: ")
    
    #Making sure input is valid through recursion
    if difficulty not in ["1", "2", "3"]:
        print(" ")
        print(RED + "That choice is invalid, please try again\n" + RESET)
        difficultySelection()
    
    return difficulty

#Generates two random numbers based on difficulty parameter
def randomNumsGenerator(dif):
    
    num1 = 0
    num2 = 0
    
    #Logic for easy difficulty
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

    #Logic for medium difficulty
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

    #Logic for hard difficulty
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

    return NumberPair(num1, num2)

#Decides what to feedback to return based on guess submitted by user
def gameLogic(n1, n2, guess):

    if guess == n2:
        return "lost"
    
    if guess == n1:
        return "won"

    if guess > n1:
        return "lower"

    if guess < n1:
        return "higher"

#Clears the screen to make the game more immersive
def clearScreen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

#Allows text to be displayed in the middle of the terminal
def centerText(text):
    
    #Calculate width of terminal
    width = os.get_terminal_size().columns
    
    #Strips color and formatting codes
    cleanText = text.replace(CYAN, '').replace(GREEN, '').replace(YELLOW, '').replace(RED, '').replace(UNDERLINE, '').replace(BOLD, '').replace(RESET, '')
    
    #Add spacing
    padding = (width - len(cleanText)) // 2

    #Print final result
    print(" " * padding + text)

#FORMATTING CODES
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

#COLOR CODES
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

#Clear screen and show title when game is first started
clearScreen()
centerText(BOLD + CYAN + "Welcome to WrongNumber!\n" + RESET)

#Main game loop
while True:    
    
    #Set difficulty
    difficulty = difficultySelection()
    print(" ")
    print("You chose have 10 guesses, Good Luck!\n" )
    
    #Set wining and losing numbers
    numbers = randomNumsGenerator(difficulty)
    
    #Number of guesses
    i = 0 

    while i < 10:
        guessString = input("Please Enter Your Guess (1-100): ")
        
        #If someone wants to restart or exit game in the middle of gameplay, this will go straight to the end game menu
        if guessString.lower() == "exit":
            print(" ")
            break

        #Guess validation
        try:
            guess = int(guessString)
            
            #If user enters a number outside of the range
            if guess < 1 or guess > 100:
                print("")
                print(RED + "Guess Invalid, Try again\n" + RESET)
                continue
        
        #If user enters a non number
        except ValueError:
            print("")
            print(RED + "Guess Invalid, Try again\n" + RESET)
            continue
        
        #Increase number of guesses by 1
        i += 1

        #Calculate remainng number of guesses to display
        guessesRemaining = 10 - i

        #Sets the verdict returned by gameLogic function, then decides how to procceed based on verdict
        decision = gameLogic(numbers.win, numbers.lose, guess)
        if decision == "lost":
            clearScreen()
            centerText(BOLD + RED + "You guessed the wrong number, you lose!" + RESET)
            break
        if decision == "won":
            clearScreen()
            if i == 1:
                centerText(BOLD + GREEN + "You guessed the right number in " + str(i) + " guess, you win!" + RESET)
            else:
                centerText(BOLD + GREEN + "You guessed the right number in " + str(i) + " guesses, you win!" + RESET)
            break
        if decision == "lower":
            print("Your guess was to high, try again")
            print("You have " + str(guessesRemaining) + " guesses left")
            continue
        if decision == "higher":
            print("Your guess was too low, try again")
            print("You have " + str(guessesRemaining) + " guesses left")
            continue
        print(decision)

    #Checking to see if number of guesses were exceeded
    if i > 9 and decision not in ["won", "lost"]:
        clearScreen()
        centerText(RED + "You ran out of guesses, game over")
        centerText(CYAN + "The winning number was " + str(numbers.win) + "\n" + RESET)
    
    #End game menu
    print(UNDERLINE + "Please Choose an Option\n" + RESET)
    print("1. Play Again")
    print("2. End Game\n")
    
    #Validation for end game menu choice
    while True:
        selection = input("Please Enter 1 or 2: ")    
        if selection == "1":
            clearScreen()
            break
        elif selection == "2":
            break
        else:
            print(" ") 
            print(RED + "Invalid choice, try again\n" + RESET)
    
    #Need to break again if ending game
    if selection == "2":
        break
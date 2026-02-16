import random

def difficultySelection ():
    
    print("Please Choose Your Difficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty = input("Please Enter 1, 2, or 3: ")
    
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

while True:    
    print("Welcome to WrongNumber!")

    difficulty = difficultySelection()
    winNum, loseNum = randomNumsGenerator(difficulty)
    i = 1

    while i < 8:
        guess = input("Please Enter Your Guess: ")
        i += 1
        decision = gameLogic(winNum, loseNum, int(guess))
        if decision == "lost":
            print("You guessed the wrong number, you lose!")
            break
        if decision == "won":
            print("You guessed the right number, you win!")
            break
        if decision == "lower":
            print("Your guess was to high, try again")
            continue
        if decision == "higher":
            print("Your guess was too low, try again")
            continue
        print(decision)

    if i > 7:
        print("You ran out of guesses, game over")
    else:
        print("Please Choose an Option")
        print("1. Play Again")
        print("2. End Gamee")
        selection = input("Please Enter 1 or 2: ")
        if selection == "1":
            continue
        if selection == "2":
            break
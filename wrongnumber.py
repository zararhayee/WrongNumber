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






























def stressTest():
    for dif in ["1","2","3"]:
        for i in range(1000):
            n1, n2 = randomNumsGenerator(dif)

            if not (1 <= n1 <= 100):
                print("Invalid num1: ", n1)
                return

            if not (1 <= n2 <= 100):
                print("Invalid num2: ", n2)
                return

    print("Passed")

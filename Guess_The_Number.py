import random
Range = input("Enter Two Numbers:-").split(",")
chance = int(input("Enter How Many Times You Want To Play:-"))
Number = random.randint(int(Range[0]), int(Range[1]))
print("Game Started!!!")
while chance:
    print(f"\t \t Chances Left {chance}")
    User_Number = int(input("Enter Your Guessed Number:-"))
    if User_Number > Number:
        print(f"Too Big")
    elif User_Number < Number:
        print("Too Small")
    else:
        print(f"Correct Guess \n \t \t \t You Won")
        break
    chance -= 1
    if chance == 0:
        print(f"Opps You Lost Correct Guess Was {Number}")
        break



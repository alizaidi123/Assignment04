# High Low Guess Game

import random as rd
def hlg():
    score = 0
    for i in range(5):
        comp = rd.randint(1,100)
        user = rd.randint(1,100)
        print(f"Your number is {user}")
        ques = input("Guess if your number is higher or lower than Comp's Number")
        if "lower" in ques.lower():
            if comp >= user:
                print(f"Correct, Computer's Number was {comp}")
                score+=1
                print(f"Your current Score is {score} ")
            else:
                print(f"Incorrect, Computer's Number was {comp}")
                score-=1
                print(f"Your current Score is {score} ")
        if "higher" in ques.lower():
            if comp <= user:
                print(f"Correct, Computer's Number was {comp}")
                score += 1
                print(f"Your current Score is {score} ")
            else:
                print(f"Incorrect, Computer's Number was {comp}")
                score -= 1
                print(f"Your current Score is {score} ")
    print(f"Your Total Score is {score}")

hlg()

# Printing 10 random number

import random as rd

def ranNum():
    for i in range(1, 11):
        x = rd.randint(1, 100)
        print(x)
ranNum()


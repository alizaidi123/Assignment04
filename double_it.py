# Double it Game!

def doubleIt():
    user = int(input("Enter Your Number"))
    i = user
    while (i <= 100):
        x = 2*i
        print(f" Double of {i} is {x}")
        i = x
doubleIt()

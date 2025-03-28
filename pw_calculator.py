# Planetary Weight Calculator

def pwc():
    user = float(input("Enter your Weight Here"))
    ew = round(user,2)
    mw = ew * (37.8/100)
    mw = round(mw,2)
    print(f"Your Weight on Earth is {ew}")
    print(f"Your Equivalent Weight on Mars will be {mw} ")

pwc()


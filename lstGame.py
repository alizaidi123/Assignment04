# list Game

lst = [1,3,5,"Mango","Apple",True]

def lg():
    print("You can either, 'Access', 'Modify' or 'Slice' the list ")
    user = input("Choose What do you wanna do?")
    if "access" in user.lower():
       ind = int(input("Enter the Index Number you wanna access"))
       try:
           print(lst[ind])
       except:
           print("Index is out range")
    if "modify" in user.lower():
        ind = int(input("Enter the Index Number you wanna modify"))
        val = input("Enter the Value you wanna update")
        try:
            lst[ind] = val
            print(lst)
        except:
            print("Index is out range")
    if "slice" in user.lower():
        ind1 = int(input("Enter the Index Numbers you wanna start slice from"))
        ind2= int(input("Enter the Index Numbers you wanna end the slice at"))
        try:
            print(lst[ind1:ind2])
        except:
            print("Index is out range")

lg()

#Joke Bot

Ques = "What are looking for?"
Jk = "Here is a joke for you! Panaversity GPT - Sophia is heading out" \
       " to the grocery store. A programmer tells" \
       " her: get a liter of milk, and if they have eggs, " \
       "get 12. Sophia returns with 13 liters of milk. The programmer " \
       "asks why and Sophia replies: 'because they had eggs'"
Sor = "Sorry I only tell jokes"

def Joke() :
    print(Ques)
    user :str = input("Write your response here")
    if "joke" in user.lower():
        print(Jk)
    else:
        print(Sor)

Joke()

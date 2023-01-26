#randomnum_game
#bet
import random

print ("Welcome to One Stop Lottery!")
print ("Every $1 bet won gives a $5 prize.")
print ("Every $1 bet lost gives a $0 prize.")

usernumber = int(input("Please Choose Number:"))
bet = float(input("How much would you like to bet?"))

winning = bet*5
loss = bet*0

randomnumer = (random.randrange(1,99))
if usernumber == randomnumer:
    print ("You win, congratulations.")
    print ("Winning number is",randomnumer)
    print ("You won $",winning)
else:
    print("You lose, try again.")
    print ("Winning number is",randomnumer)
    print ("You won $",loss)
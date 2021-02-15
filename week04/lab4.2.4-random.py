# this program generates a random number between 0 and 100 to guess
# Author: Sarah McNelis



rangeFrom = 0
rangeTo = 100
numberToGuess = random(rangeFrom, rangeTo)


guess = int(input("Please guess a number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was", numberToGuess)
    
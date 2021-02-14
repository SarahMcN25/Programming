# this program prompts the user to guess a number
# until user guesses the correct number
# also tells user if their guess is too high or too low
# Author: Sarah McNelis

numberToGuess = 30

guess = int(input("Please guess a number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("too low")
    else:
        print ("too high")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was",numberToGuess)
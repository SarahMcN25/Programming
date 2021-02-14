# this program prompts the user to guess a number
# until user guesses the correct number
# Author: Sarah McNelis

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess) 

#instead of .format can use like abaove , numberToGuess
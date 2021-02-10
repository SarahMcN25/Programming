# this program reads in a number and prints out one more than that number
# author: Sarah McNelis

number = int(input("please enter a number:"))
newNumber = number + 1
print('{} plus one is {}'.format(number, newNumber))

# doesn't recognise number as being an integer
# thinks its a string 
# variable int lets it know it's an actual number

# this program leads in a string and strips any leading or trailing spaces
# also converts all letters to lower case
# also outputs lenght of the origional string and the normalised one
# author: Sarah McNelis

rawString = input("Please enter a string:")
normalisedString = rawString.strip().lower()

lenghtOfRawString = len(rawString)
lenghtOfNormalisedString = len(normalisedString)

print("That String normalised is: {}".format(normalisedString))
print("we reduced the input string from {} to {} characters".format(lenghtOfRawString, 
lenghtOfNormalisedString))

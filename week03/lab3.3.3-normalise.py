# this program reads in  a string
# strips any leading or trailing spaces
# converts string to lower case
# also outputs lenght of origional string and normalised one
# author: Sarah McNelis

rawString = input("Please enter a string:")
normalisedString = rawString.strip().lower()

lenghtOfRawString = len(rawString)
lenghtOfNormalisedString = len(normalisedString)

print("That string normalised is: {}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(
lenghtOfRawString, lenghtOfNormalisedString))

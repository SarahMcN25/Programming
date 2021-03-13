# Q3: What will contens of the file be once this program is run?
# Answer: file was already created in previous question
# therefore w mode will overwrite and output number of characters of new sentence: 13

with open ("test-b.txt", "w") as f2:
    data = f2.write("another line\n")
    print (data)
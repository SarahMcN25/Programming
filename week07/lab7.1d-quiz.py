# Q4: what will contents of file be after this program is run?
# Answer: test d, another line
# a mode opens/creates a file for appending/adding

with open("test-d.txt", "w") as f:
    data = f.write("test d\n")
    print(data)

with open("test-d.txt", "a") as f2:
    data = f2.write("another line\n")
    print (data)
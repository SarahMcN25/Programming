# Q2: assuming the file does not exist what will be outputted to the console when the program is run?
# Answer: w mode opens/creates a file for writing
# therefore the number of chars written will be outputted: 7

with open("test-b.txt", "w") as f:
    data =  f.write("test b\n")
    print (data)

with open ("test-b.txt", "w") as f2:
    data = f2.write("another line\n")
    print (data)
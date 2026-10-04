#read the file and store all the lines in list
with open("test.txt", "r") as reader:
    content = reader.readlines()
    #reversed(content)
    with open("test.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)
print(content)



    #need not close the file
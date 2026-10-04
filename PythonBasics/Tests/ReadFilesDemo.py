file = open("test.txt")

# #one single line at a time
# print(file.readline())
# print(file.readline())
#
# file.close()

# file = open("test.txt")
# print(file.read(3))
# file.close()

#Print line by line

# file2 = open("test.txt")
# line = file2.readline()
# while line != "":
#     print(line)
#     line = file2.readline()
# file2.close()

#List will be created
fileList = open("test.txt")

#Iterate through the loop
for line in fileList.readlines():
    print(line)

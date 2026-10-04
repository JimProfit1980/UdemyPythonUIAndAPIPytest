# with open("file1.txt","r") as reader:
#     content = reader.readlines()
#
# for line in content:
#     print(line)

file = open("file1.txt")
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()


with open('file1.txt', 'r') as file:
    content = file.read()
    print(content)

#Test 9 Passed

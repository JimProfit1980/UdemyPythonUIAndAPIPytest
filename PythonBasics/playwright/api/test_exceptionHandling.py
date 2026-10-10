# with open("file.txt","w") as writeFile:
#     writeFile.write("Hello World Appended\n")
try:
    with open("file.txt","r") as readFile:
        print(readFile.read())

except Exception as e:
    print(e)

finally:
    print("Finally always executes, used for cleaning up resources")

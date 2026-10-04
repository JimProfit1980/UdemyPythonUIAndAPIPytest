fruits = ["apple", "banana", "cherry","date","elderberry"]
print("First fruit: " + fruits[0])
print("Last fruit: " + fruits[-1])

text = "Fruits from index 1 to 2: "
del fruits[0]
del fruits[-1]
del fruits[-1]
print("{}{}".format(text,fruits))

#Passed 3

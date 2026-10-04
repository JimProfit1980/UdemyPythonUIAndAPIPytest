listArray = [1,2,"Hello","World",5,6,7,8,9,10]
# print(listArray)
# print(type(listArray))

# print(listArray[0] + listArray[1])
# print(listArray[2] + listArray[3])
#size of array
print(listArray)

listArray.insert(3,"September")
listArray.append("At The End of the array")
print(listArray)
listArray.reverse()
print(listArray)

listArray[2] = "hello"
listArray.reverse()
print(listArray)

del listArray[-1]
print(listArray)
# listArray.pop()
# print(listArray)
#print(listArray)
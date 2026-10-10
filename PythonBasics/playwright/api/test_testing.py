import asyncio
import time

data = [{"Honda": "Japan", "Founded": 1900}, {"VW": "Germany", "Founded": 1814}, {"Suzuki": "Japan", "Founded": 1817}]
count = 0
values = []
for car in data:  # car is one dictionary
    for key, value in car.items():  # each key/value pair in it
        key += "" + "Shane"
        print(key, ":", value)
        key += ""
        #print(key, ":")

    print("---")

#Output:
# Honda: Japan
# Founded: 1900
#---
#VW: Germany
# Founded: 1814
#
#
# def add(x,y):
#     return x+y
#
#
# addition = lambda x,y: x + y
# print(addition(1,2))
#
    numbers = [1,2,3,4,5]
    even_numbers = map(lambda x: x * 2,numbers)
    print(list(even_numbers))
#
# subtraction = lambda i, j: i - j
# print(subtraction(9,4))
#
# numbers = [1,2,3,4,5]
# newNumbers = map(lambda x: x*2,numbers)
# print(list(newNumbers))
#
# numbers = [1,2,3,4,5]
# newNumber = filter(lambda y: y * 2,numbers)
# print(list(newNumber))
#
# moreNumbers = [2323,4545,222,565656,878]
# evenNumbers = map(lambda x: x % 2 == 0,moreNumbers)
# print (list(evenNumbers))
#
# total = lambda x,y: x + y
# print(total(4,3))
#
#
# def fun(numbers):
#     num = [1, 3, 5, 7, 9]
#     if (numbers in num):
#         return True
#     else:
#         return False
#
#
# sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filtered = filter(fun, sequence)
#
# print('The filtered numbers are: ')
# for s in filtered:
#     print(s)
#
#
# num = [3,2,6,1]
#
# print(list(reversed(sorted(num))))
#
#
# def task(name):
#     print(f"It starts with {name}")
#     time.sleep(2)
#     print(f"It ends with {name}")
#
# print(task("Shane"))
# print(task("Peter"))
#
#
# async def task(name):
#     print(f"It starts with {name}")
#     await asyncio.sleep(2)
#     print(f"It ends with {name}")
#
#
# async def main():
#     await asyncio.gather(task("Shane"), task("Peter"))
#
# asyncio.run(main())
newList = [1,4,5,3,4]

print(sorted(newList[::-1]))



class MyClass:

    @classmethod
    def printClass(cls):
        print(cls.__name__)




MyClass.printClass()
car = {"make":"Toyota","model":"Camry","year":2020,"color":"Blue"}

for key,value in car.items():
    if key == "model":
        print("{}{}".format("Car model: ",value))

car["owner"] = "Rahul"
print("{}{}".format("Updated car dictionary: ", car))

#Test 5 Passed
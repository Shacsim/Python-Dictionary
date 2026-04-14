car = {"salom": "Assalomaleykum", "mashina": "Toyota", "model" : "carbon", "color" : "blue"}

key = input("Kalit kiriting: ")

if key in car:
    print(car[key])
else:
    print("Topilmadi")
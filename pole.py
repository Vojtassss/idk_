predmety = ["Matika", "Cestina", "Ajina", "Telak", "Programko", "Hardware"]
print (len(predmety))
x = predmety[0]
predmety[0] = "Ekonomika"
x = len(predmety)
predmety.append("Ekonomika")
predmety.pop(1)
for x in predmety:
    print(x)
# predmety.append("Ekonomika")
# predmety.pop(1)
predmety.remove("Hardware")
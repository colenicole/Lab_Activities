#CONDITIONAL WITH BOOLEAN OR
a = "Rose"
b = "Daisy"
c = "Shitzu"
d = "Bulldog"
e = input("Enter your choice:")

print(e)

if e == "a" or e == "b":
    print(" You selected a type of flower")
elif e == "c" or e == "d":
    print ("You selected a dog")
else:
    print("Wrong Selection")
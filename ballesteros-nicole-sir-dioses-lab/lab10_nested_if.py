firstNumber = int(input("Enter previous billing :"))
secondNumber = int(input("Enter present billing :"))
consumption = (firstNumber - secondNumber)

print("Consumption: " + str(consumption))


a = "Residential"
b = "Commercial"
c = "Industrial"
e = input("Enter your choice: ")

print(e)

if e == "a" or e == "A":
    print("You selected residential")
        
    if consumption >= 100:
        GMontlybill = int(consumption) * 18.75
        print("Gross monthly Income: " + str(GMontlybill))
        tax = float(GMontlybill) * .05
        print("Tax: " + str(tax))
        Finalbill = int(GMontlybill) + 0 + int(tax)
        print("Final Monthly Bill : " + str(GMontlybill))
            
    elif e == "b":
        print("You selected commercial")
        
    if consumption >= 100:
        GMontlybill = int(consumption) * 18.75
        print("Gross monthly Income: " + str(GMontlybill))
        tax = float(GMontlybill) * .05
        print("Tax: " + str(tax))
        Finalbill = int(GMontlybill) + 0 + int(tax)
        print("Final Monthly Bill : " + str(GMontlybill))
            
    elif e == "c":
        print("You selected industrial")
        
if consumption >= 100:
        GMontlybill = int(consumption) * 18.75
        print("Gross monthly Income: " + str(GMontlybill))
        tax = float(GMontlybill) * .05
        print("Tax: " + str(tax))
        Finalbill = int(GMontlybill) + 0 + int(tax)
        print("Final Monthly Bill : " + str(GMontlybill))
            
else:
    ("invalid selection please try again")
    
    


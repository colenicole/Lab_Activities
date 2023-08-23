# String Format no error

age = 48
txt = "My name is Jun, and I am {}"
print(txt.format(age))

# String Format no error
quantity = 5
unitcode = 102
price = 546.55
myorder = "I will buy {} pieces of product {} for {} pesos."
print(myorder.format(quantity, unitcode, price))

# String Format with error
age = 55
txt = "My name is Jude, I am" + age
print(txt)
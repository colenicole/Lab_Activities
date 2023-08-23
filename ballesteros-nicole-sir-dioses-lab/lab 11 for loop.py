#looping ..... using for loop
# program to find the sum of all numbers stored in a list
#list of numbers
numbers = [100, 15, 43, 58, 104, 212, 52, 47, 311]

#variable to store the sum
sum = 0
 
 # iterate over the list
for val in numbers:
    sum = sum + val
print("The sum is" , sum)
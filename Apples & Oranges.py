print("Welcome to the Fruit Market!")
print("The prices of the fruits are:")
print("Apple=20, Orange=25")
priceApples = 20
priceOranges = 25
apples=int(input("How many apples do you want to buy?"))
oranges=int(input("How many oranges do you want to buy?"))
total=(apples * priceApples + oranges * priceOranges)
print("Total amount is:" + str(total))
print("Solution:")
print((str(apples)) + " * " + (str(priceApples)) + " + " + (str(oranges)) + " * " + (str(priceOranges)) + " = " + (str(total)))
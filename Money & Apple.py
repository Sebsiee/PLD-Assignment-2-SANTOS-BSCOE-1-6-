print("Welcome!")
moneyAmount=int(input("Enter the amount of your money: "))
applePrice=int(input("What is the price of an apple? "))
totalApples=(moneyAmount / applePrice)
totalChange=(moneyAmount - applePrice )
if totalApples > 1:
 print("You can buy " + str("%.0f" % totalApples) + " apples and your change is " + str(totalChange) + " pesos.")  
elif totalApples == 1:
 print("You can buy " + str("%.0f" % totalApples) + " apple and your change is " + str(totalChange) + " pesos.")
else:
 print("You can't buy an apple and your change is " + str(totalChange) + " pesos.")

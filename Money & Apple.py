print("Welcome!")
moneyAmount=int(input("Enter the amount of your money: "))
applePrice=int(input("What is the price of an apple? "))
totalApples=(moneyAmount / applePrice)
totalChange=(moneyAmount - applePrice )
appleOrNot = totalApples
if appleOrNot > 1:
 print("You can buy " + str("%.0f" % appleOrNot) + " apples and your change is " + str(totalChange))  
elif appleOrNot == 1:
 print("You can buy " + str("%.0f" % appleOrNot) + " apple and your change is " + str(totalChange))
else:
 print("You can't buy an apple and your change is " + str(totalChange))

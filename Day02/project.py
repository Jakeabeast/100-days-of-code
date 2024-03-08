'''
DAY 2 PROJECT - Bill Split Calculator

The goal of this project is to calculate the price each person must pay for a split bill
'''

#=====================================================================
print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))

tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? ")) / 100 + 1

people = int(input("How many people to split the bill? "))

amount_per_person = bill * tip_percent / people
print(amount_per_person)

print("Each person should pay: $%g" % round(amount_per_person, 2))
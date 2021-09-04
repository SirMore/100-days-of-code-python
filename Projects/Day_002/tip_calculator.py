#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#Welcome message
print("=="*25)
print("Welcome to the Tip Calculator.")
print("=="*25)

#Gathering information from the user
bill = float(input("How much is the total bill? $"))

persons = int(input("How many people are to split the bill? "))
tip_percent = float(input("What percentage tip would you like to give? "))

# Calculating the percentage tip per person
tippings = 1 + (tip_percent/100)
cost_per_person = bill/persons
tip_each = (bill/persons)*tippings

#print the amount to be payed by each person
print(f"Each of the {persons} of you will have to pay an amount of ${cost_per_person:.2f} + a tip {tip_percent}% making a total payment of ${tip_each:.2f}")
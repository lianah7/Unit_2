# by Liana Hill
# last updated September 23, 2019
# unit 2 assignment option one
# this program creates a conversation between a chat bot and user to find the total cost and value of a car

name = input("What is your name?")
print("It's nice to meet you", name, "My name is Emma from Engineering.")

location = input("Where are you from?")
print(location, "sounds like an awesome place to be from.")

number = int(input("What is your favorite number?"))
print("Your favorite number", number, "is", number/2, "times bigger than my favorite number, 23!")

car = input("What is your dream car?")
print("That is such a cool car!")

cost = float(input("How much does the car cost?"))
print("That's expensive!")

years = int(input("How many years will it take for you to pay off the car?"))

# the following lines are for calculating the total cost of the car
annual_interest = float(input("What is the annual interest rate of the car?"))
monthly_interest = (annual_interest/100)/12
number_of_monthly_payments = years * 12

monthly_payments = (monthly_interest * cost) / (1 - (1 + monthly_interest) ** -(number_of_monthly_payments))
total_cost = monthly_payments * (12 * years)

print("Your monthly payment for a", str(car), "is", str(monthly_payments), "that is a total of", str(total_cost))





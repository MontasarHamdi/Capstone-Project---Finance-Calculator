# Import math to use math function.
# Request user to choose investment or bond and store under finance_type variable.
# Use """ for long input string.
# Use if statement for investment selection.
# Use .casefold to lowercase string entry whenever appropriate.
# Learned about .casefold via link below.
# https://stackoverflow.com/questions/61038788/if-statement-string-checking-with-casefold-python
# Request more user information based on investment selection and assign them to appropriate variables.
# Nest an if and elif statement for the 'simple' or 'compound' condition and code relevant calculations.
# Print total amount with f-string
# Use else for incorrect entry

# Use elif statement for bond selection.
# Request more user information based on bond selection and assign them to appropriate variables.
# code relevant calculations.
# Print total amount with f-string
# Use else for incorrect entry

import math

finance_type = input("""Choose either 'investment' or 'bond' from the menu below to proceed: 

investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan

Selection: """)

if finance_type.casefold() == "investment":
    deposit_amount = float(input("Please enter the amount you wish to deposit: "))
    interest_rate = int(input("Please enter annual interest rate (do not include % symbol): "))
    num_years = int(input("How many years do you plan on investing?: "))
    interest = input("Would you like 'simple' or 'compound' interest: ")

    if interest.casefold() == "simple":
        total_amount = round(deposit_amount*(1 + (interest_rate/100)*num_years), 2)
        print(f"The total amount if simple interest is applied is £{total_amount}.")
    elif interest.casefold() == "compound":
        total_amount = round(deposit_amount*math.pow(1+(interest_rate/100), num_years), 2)
        print(f"The total amount if compound interest is applied is £{total_amount}.")
    else:
        print("Incorrect entry!")

elif finance_type.casefold() == "bond":
    house_value = float(input("Please enter the present value of the house: "))
    interest_rate = int(input("Please enter annual interest rate (do not include % symbol): "))
    num_months = int(input("Please enter the number of months you plan to take to repay the bond: "))
    monthly_interest = round((interest_rate/100)/12, 2)
    total_amount = round((monthly_interest*house_value)/(1 - math.pow((1+monthly_interest), -num_months)), 2)
    print(f"The total repayment on the home loan each month is £{total_amount}.")

else:
    print("Incorrect Entry!")

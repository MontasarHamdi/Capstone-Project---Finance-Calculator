====FINANCE CALCULATOR====

For this task, assume that you have been approached by a small financial company and asked to create a program that 
allows the user to access two different financial calculators: an investment calculator and a home loan repayment 
calculator.
● Create a new Python file in this folder called finance_calculators.py.
● At the top of the file include the line import math

The user should be allowed to choose which calculation they want to do (Bond or Investment).

If the user selects investment ask the user to input:
● The amount of money that they are depositing.
● The interest rate (as a percentage). Only the number of the interest rate should be entered — don’t worry about 
having to deal with the added ‘%’, e.g. The user should enter 8 and not 8%.
● The number of years they plan on investing.
● Then ask the user to input if they want “simple” or “compound” interest, and store this in a variable called interest.
Depending on whether they typed “simple” or “compound”, output the appropriate amount that they will get back 
after the given period, at the specified interest rate. 

If the user selects ‘bond’, do the following: 
● Ask the user to input the present value of the house. e.g. 100000
● The interest rate. e.g. 7
● The number of months they plan to take to repay the bond. e.g. 120

■ Calculate how much money the user will have to repay each month and output the answer.

# loan-calculator
This is a project that I worked on as part of a course from Hyperskill. 

I learned the fundamentals of Python and used what I learned towards building this loan calculator.

As part of my learning, I practiced using mathematics with Python and learned how to use third-party modules and libraries. 

This program parses arguments from the command line and calculates a part of your loan based off of the inputs that you pass to the file. 

This program takes two types of loans: **annuity** and **differential**.

For example, if you want to calculate your annuity payment, then you would run this file in the command line like this:
	
	python3 loan-calculator.py --type=annuity --principal=(input) --periods=(input) --interest=(input)

The script will then take your inputs and calculate the annuity payment on your loan, as well as your overpayment, which is how much money you are paying out of pocket (above the principal) on the loan.


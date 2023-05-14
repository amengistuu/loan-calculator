import math
import argparse

# write your code here

parser = argparse.ArgumentParser()
# add parameters
parser.add_argument("--type", choices=["annuity", "diff"], help="You need to chose the type of payment: annuity or diff.")
parser.add_argument("--principal", help="You need enter the principal of the loan.")
parser.add_argument("--periods", help="You need enter the periods on the loan.")
parser.add_argument("--interest", help="You need enter the interest of the loan.")
parser.add_argument("--payment", help="You need to add the monthly payment amount.")

args = parser.parse_args()

def overpayment(yourPayment, principal, periods):
    return (yourPayment * periods) - principal

num_arguments_provided = sum(arg is not None for arg in vars(args).values())
# check for incorrect parameters
if num_arguments_provided < 4:
    print("Incorrect parameters. There are less than 4 arguments.")
elif args.type != "annuity" and args.type != "diff":
    print("Incorrect parameters")
elif args.principal is not None and int(args.principal) < 0:
    print("Incorrect parameters. Principal cannot be negative.")
elif args.periods is not None and int(args.periods) < 0:
    print("Incorrect parameters. Periods cannot be negative.")
elif args.interest is not None and float(args.interest) < 0:
    print("Incorrect parameters. Interest cannot be negative.")
else:
    # annuity payments
    if args.type == "annuity": 
        if not args.payment: # if payment is not provided, calculate the payment
            periods = int(args.periods)
            interest = float(args.interest) * .01
            nominal_interest = (interest) / (12 * 1)
            principal = float(args.principal)
            annuity_payment = principal * ((nominal_interest * math.pow((1 + nominal_interest), periods)) / (math.pow((1 + nominal_interest), periods) - 1))
            annuity_payment = math.ceil(annuity_payment)
            print(f"Your annuity payment = {annuity_payment}!")
            print(f"Overpayment = {overpayment(annuity_payment, principal, periods)}")
        elif int(args.payment) > 0 and not args.principal: # if payment is provided, and loan principal is not provided, calculate the principal
            periods = int(args.periods)
            interest = float(args.interest) * .01
            nominal_interest = (interest) / (12 * 1)
            annuity_payment = int(args.payment)
            principal = annuity_payment / ((nominal_interest * math.pow((1 + nominal_interest), periods)) / (math.pow((1 + nominal_interest), periods) - 1))
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {overpayment(annuity_payment, principal, periods)}")    
        elif int(args.payment) > 0 and not args.periods: # if payment is provided, and periods is not provided, calculate the periods
            interest = float(args.interest) * .01
            nominal_interest = (interest) / (12 * 1)
            annuity_payment = int(args.payment)
            principal = int(args.principal)
            periods = math.ceil(math.log((annuity_payment / (annuity_payment - nominal_interest * principal)), (1 + nominal_interest)))
            years = periods // 12
            months = periods % 12
            if months > 12:
                years = int(months / 12)
                months_remainder = months - (years * 12)
                if months_remainder == 0:
                    print(f"It will take {years} years to repay this loan!")
                    print(f"Overpayment = {annuity_payment * periods - principal}")
                elif months_remainder != 0:
                    print(f"It will take {years} years and {months_remainder} to repay this loan!")
                    print(f"Overpayment = {overpayment(annuity_payment, principal, periods)}")
            elif months == 12:
                print("It will take 1 year to repay this loan!") 
                print(f"Overpayment = {overpayment(annuity_payment, principal, periods)}")
            elif months < 12:
                print(f"It will take {months} to repar this loan!")
                print(f"Overpayment = {overpayment(annuity_payment, principal, periods)}")
    # differentiated payments
    elif args.type == "diff":
        periods = int(args.periods)
        interest = float(args.interest) * .01
        nominal_interest = (interest) / (12 * 1)
        sum = 0
        principal = float(args.principal)
        for month in range(1, periods + 1):
            month = int(month) # convert the month to type int so that we can use it in our formulas
            diff_payment = (principal / periods) + nominal_interest * (principal - ((principal * (month - 1)) / periods))
            diff_payment = math.ceil(diff_payment)
            sum += diff_payment
            print(f"Month {month}: payment is {diff_payment}")
        print(f"Overpayment = {sum - principal}")
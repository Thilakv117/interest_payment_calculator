def main():
    print("This is monthly payment load calculator: ")
    print("")
    princple = float(input('Load Amount: '))
    apr = float(input('Annual interest rate: '))
    years = int(input("Amount of Years: "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = princple* monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    print("%.2f" % monthly_payment)
main()
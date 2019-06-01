import requests
import re

source= "https://api.ratesapi.io/api/latest?base="
currencies = ["USD", "GBP", "EUR", "CAD", "CNY", "HKD", "JPY", "AUD", "BGN", "NZD", "ILS", "RUB", "PHP", "CHF", "TRY", "MYR", "HRK", "CZK", "IDR", "DKK", "NOK", "HUF", "MXN", "THB", "ISK", "ZAR", "BRL", "SGD", "PLN", "INR", "KRW", "RON", "SEK"]

# Continuously loop program until user does not want to continue.
while True:
    print("Currencies: USD, GBP, EUR, CAD, CNY, HKD, JPY, AUD, BGN, NZD, ILS, RUB, PHP, CHF, TRY, MYR, HRK, CZK, IDR, DKK, NOK, HUF, MXN, THB, ISK, ZAR, BRL, SGD, PLN, INR, KRW, RON, SEK")
    
    # Base currency input and validation
    while True:
        print("\nEnter base currency: ")
        base = input().upper()
        valid = True if base in currencies else False
        if valid:
            break
        print("Invalid currency.")
    
    # Target currency input and validation
    while True: 
        print("\nEnter target currency: ")
        target = input().upper()
        valid = True if target in currencies else False
        if valid:
            break
        print("Invalid currency.")

    # Currency amount input and validation
    while True:
        print("\nEnter currency amount: ")
        amount = input()
        if '.' in amount:
            decimal = re.findall(r'(\w+).(\w+)',amount)
            valid = True if decimal[0][0].isdigit and decimal[0][1].isdigit else False
            amount = "{0}.{1}".format(decimal[0][0], decimal[0][1])
        else:
            valid = True if amount.isdigit() else False
        if valid:
            break
        print("Invalid numbers.")

    # Retrieve currency data and output conversion
    ret = requests.get(source+base)
    print("\n1 {0} = {1} {2}".format(base, ret.json()['rates'][target], target))
    print("{0} {1} = {2} {3}".format(amount, base, float(amount) * ret.json()['rates'][target], target))
    
    # Prompt to redo the program.
    print("\nContinue? (y/n): ")
    if input() == 'n':
        raise SystemExit
    else:
        print("\n")
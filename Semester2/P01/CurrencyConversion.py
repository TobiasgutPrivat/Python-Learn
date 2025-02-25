import csv

with open('Semester2/P01/eurofxref.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# remove spaces in strings
data = [[x.strip() for x in row] for row in data]
currency_rates = dict(zip(data[0], data[1]))

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in currency_rates or to_currency not in currency_rates:
        return None
    return amount * float(currency_rates[to_currency]) / float(currency_rates[from_currency])

if "__main__" == __name__:
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency to convert from: ")
    to_currency = input("Enter the currency to convert to: ")
    result = convert_currency(amount, from_currency, to_currency)
    if result is not None:
        print(f"{amount} {from_currency} is equal to {result} {to_currency}")
    else:
        print("Invalid currency code")
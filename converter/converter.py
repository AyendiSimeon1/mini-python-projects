from forex_python.converter import CurrencyRates

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate

    return converted_amount

def main():
    print("Welcome To The Python Currency Converter App")
    amount = float(input("Enter the amount you want to convert:"))
    from_currency = input("Enter the Source Currency Code:")
    to_currency = input("Enter the target currency code: ")

    converted_amount = currency_converter(amount, from_currency, to_currency)

    print(f"{amount} in {from_currency} to {to_currency} is {converted_amount}")


if __name__ == "__main__":
    main()
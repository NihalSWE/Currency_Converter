#Curency conveter

from requests import get
from pprint import PrettyPrinter

BASE_URL="https://free.currconv.com/api/v7"
API_KEY="Enter Your API_KEY"

printer=PrettyPrinter()
def get_currencies():
    endpoint=f"/currencies?apiKey={API_KEY}"
    url=BASE_URL + endpoint
    data=get(url).json()['results']

   
    return data

def print_currencies(currencies):
    for currency_id, currency_data in currencies.items():
        name = currency_data['currencyName']
        symbol = currency_data.get("currencySymbol", "")
        print(f"{currency_id} - {name} - {symbol}")


def convert_amount(currency1, currency2):
    amount = float(input("Enter the amount to convert: "))

    endpoint = f"/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)
    data = response.json()

    if len(data) == 0:
        print("Invalid Currencies.")
        return

    rate = list(data.values())[0]
    converted_amount = amount * rate
    print(f"{amount:.2f} {currency1} -> {converted_amount:.2f} {currency2}")
    return converted_amount



def main():
    currencies=get_currencies()
    print("Welcome to the currency converter")
    print("List-lists the different countries")
    print("Convert-convert currencies")
    print("Rate-exchange rate")
    print()

    while True:
        command=input("Enter a command(q to quit): ").lower()
        if command=='q':
            break
        elif command=="list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter the source currency code (e.g., USD): ")
            currency2 = input("Enter the target currency code (e.g., CAD): ")
            convert_amount(currency1, currency2)

        elif command=="rate":
            currency1 = input("Enter the source currency code (e.g., USD): ")
            currency2 = input("Enter the target currency code (e.g., CAD): ")
            rate = convert_amount(currency1, currency2)
            print(f"{rate:.2f}")
        else :
            print('Unknown Command')
main()



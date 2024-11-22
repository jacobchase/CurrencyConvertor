import requests
 
class CurrencyConverter:
    rates = {}
    def __init__(self, url):
        data = requests.get(url).json()
        self.rates = data["rates"]
    
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.rates[from_currency]
        
        amount = round(amount * self.rates[to_currency], 2)
        print(f"{initial_amount} in {from_currency} is {amount} in {to_currency}")

if __name__ == "__main__":
 
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', "cfa36dc662cd09867f81c57a976617a5")  
    c = CurrencyConverter(url)
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))
 
    c.convert(from_country, to_country, amount)
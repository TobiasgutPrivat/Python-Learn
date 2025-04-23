import requests

def get_exchange_rate(target_currency):
    api_url = "https://open.er-api.com/v6/latest/CHF"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data: dict = response.json()
        rates: dict[str, float] = data.get('rates', {})
        if target_currency in rates:
            return rates[target_currency]
        else:
            raise ValueError(f"Exchange rate for '{target_currency}' not found.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred while fetching exchange rates: {e}")

if __name__ == "__main__":
    target_currency = "EUR"
    try:
        rate = get_exchange_rate(target_currency)
        print(f"1 CHF = {rate} {target_currency}")
    except Exception as e:
        print(e)

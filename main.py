import requests

API_KEY = "d9b4247da85447d81c7391a2"
BASE_CURRENCY = input("Enter base currency (e.g., USD, EUR, GBP) [Default: USD]: ").upper() or "USD"

url = f"https://v6.exchangerate-api.com/v6/d9b4247da85447d81c7391a2/latest/{BASE_CURRENCY}"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
	rates = data['conversion_rates']
	target = input("Enter target currency or press ENTER to see all rates: ").upper()
	print(f":\n[*] Base: {BASE_CURRENCY} | Updated: {data['time_last_update_utc']}")
	if target:
		if target in rates:
			print(f"[!] 1 {BASE_CURRENCY} = {rates[target]} {target}")
		else:
			print("Currency not found")
	else:
		print(f"[*] Displaying all {len(rates)} available exchange rates:")
		print("-" * 30)
		for code, rate in rates.items():
			print(f"{code}: {rate}")
		print("-" * 30)

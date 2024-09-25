import tkinter as tk
from tkinter import ttk
import requests

# Get the conversion rate from an API online
def convert_currency():
    try:
        amount = float(amount_var.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        # figure out if it is a cryptocurrency (this api only works for crypto). If it is a crypto currency, determine which it is.
        if from_currency in ["BTC", "ETH"]:
            # if its botcoin then insert the coin id for bitcoin into the url
            if from_currency == "BTC":
                coin_id = "bitcoin"
            # If it's not bitcoin, it is ethereum, therefore put the ethereum id into the url
            else:
                coin_id = "ethereum"
            # url that can be edited into any of the bitcoin exchange rates needed
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={to_currency.lower()}"
            # connect the internet and the code to work together (using the imported "requests")
            response = requests.get(url)
            data = response.json()
            conversion_rate = float(data[coin_id][to_currency.lower()])
        # if not a crypto currency at all, then the code knows it is a normal currency where it will use a different API
        else:
            # using CurrencyAPI for normal currencies
            # MY API key! (need to insert into url for the api to work)
            api_key = "cur_live_JoAYP3cikvSakrfdX5xBlvKv7OZ9Yy25O3mNcE0a"
            url = f"https://api.currencyapi.com/v3/latest?apikey={api_key}&currencies={to_currency}&base_currency={from_currency}"
        # connect the internet and the code to work together (using the imported "requests")
            response = requests.get(url)
            data = response.json()
            conversion_rate = float(data['data'][to_currency]['value'])

        # do the conversion math
        converted_amount = amount * conversion_rate
        result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")

    # error handling:
    except ValueError:
        result_label.config(text="Error: Please enter a valid number for the amount.")
    except requests.exceptions.RequestException:
        result_label.config(text="Error: There was a problem with the API request.")
    except KeyError:
        result_label.config(text="Error: Invalid currency conversion or API key issue.")


# Clear button logistics
def clear_fields():
    from_currency_combo.current(0)
    to_currency_combo.current(1)
    amount_var.set("")
    result_label.config(text="")


# The big window
window = tk.Tk()
window.title('Currency Exchange App')
window.geometry('450x450')

# Title box on top
ttk.Label(window, text="Currency Exchange!",
          background='purple', foreground="white",
          font=("Ubuntu Mono", 15)).grid(row=0, column=1)

# Label for "From Currency"
ttk.Label(window, text="From Currency:", font=("Ubuntu Mono", 10)).grid(column=0, row=2, padx=10, pady=25)

# Combobox creation for "From Currency"
from_currency_var = tk.StringVar()
from_currency_combo = ttk.Combobox(window, width=27, textvariable=from_currency_var)
from_currency_combo['values'] = ("USD", "CAD", "EUR", "GBP", "JPY", "AUD", "INR", "CHF",
                                 "CNY", "HKD", "NZD", "SGD", "BTC", "ETH", "ZAR", "MXN",
                                 "BRL", "RUB", "AED", "THB")
from_currency_combo.grid(column=1, row=2)
from_currency_combo.current(0)

# Label for "To Currency"
ttk.Label(window, text="To Currency:", font=("Ubuntu Mono", 10)).grid(column=0, row=3, padx=10, pady=25)

# Combobox creation for "To Currency"
to_currency_var = tk.StringVar()
to_currency_combo = ttk.Combobox(window, width=27, textvariable=to_currency_var)
to_currency_combo['values'] = ("USD", "CAD", "EUR", "GBP", "JPY", "AUD", "INR", "CHF",
                               "CNY", "HKD", "NZD", "SGD", "BTC", "ETH", "ZAR", "MXN",
                               "BRL", "RUB", "AED", "THB")
to_currency_combo.grid(column=1, row=3, padx=10, pady=10)
to_currency_combo.current(1)

# Label for Amount
ttk.Label(window, text="Amount:", font=("Ubuntu Mono", 10)).grid(column=0, row=15, padx=10, pady=25)

# Space to enter Amount
amount_var = tk.StringVar()
amount_entry = ttk.Entry(window, width=30, textvariable=amount_var)
amount_entry.grid(column=1, row=15)

# Convert button deign
convert_button = ttk.Button(window, text="Convert", command=convert_currency)
convert_button.grid(column=1, row=16, pady=20)

# Clear button design
clear_button = ttk.Button(window, text="Clear", command=clear_fields)
clear_button.grid(column=1, row=17, pady=20)

# The result (displays the converted amount)
result_label = ttk.Label(window, text="", font=("TUbuntu Mono", 12))
result_label.grid(column=1, row=18)

# Run the application
window.mainloop()

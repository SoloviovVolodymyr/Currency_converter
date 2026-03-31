import tkinter as tk
from tkinter import ttk

currency = ["UAH", "EUR", "USD"]
exchange_rates = {
    "USD": 1.0,
    "UAH": 44.0, 
    "EUR": 0.92,
}

def validate_input(new_value):
    if new_value == "":
        return True
    if new_value.count('.') > 1:
        return False
    for char in new_value:
        if not (char.isdigit() or char == '.'):
            return False
    return True

def calculations():
    from_curr = currency_option.get()
    to_curr = converted_currency.get()
    amount_str = currency_enter.get()
        
    if amount_str == "":
        converted_value_label.config(text="Error: enter amount!", fg="red")
        return

    rate_from = exchange_rates[from_curr]
    rate_to = exchange_rates[to_curr]
    currency_float = float(amount_str)
    
    converted_number = (currency_float / rate_from * rate_to)
    
    converted_value_label.config(
        text=f"Converted amount: {converted_number:.2f} {to_curr}", 
        fg="black"
    )

root = tk.Tk()
root.title("Currency Converter")
root.resizable(False, False)
root.config(padx=20, pady=20)

vcmd = (root.register(validate_input), '%P')

font_style = ("Arial", 12)

tk.Label(root, text="From currency:", font=font_style).grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Label(root, text="To currency::", font=font_style).grid(row=0, column=1, padx=10, pady=5, sticky="w")

currency_option = ttk.Combobox(root, values=currency, state="readonly", font=font_style, width=15)
currency_option.grid(row=1, column=0, padx=10, pady=5)
currency_option.current(0)

converted_currency = ttk.Combobox(root, values=currency, state="readonly", font=font_style, width=15)
converted_currency.grid(row=1, column=1, padx=10, pady=5)
converted_currency.current(2)

tk.Label(root, text="Enter amount:", font=font_style).grid(row=2, column=0, padx=10, pady=(15, 0), sticky="w")

currency_enter = tk.Entry(root, font=font_style, validate="key", validatecommand=vcmd, width=17)
currency_enter.grid(row=3, column=0, padx=10, pady=5)

conversion_button = tk.Button(root, text="Convert", font=font_style, command=calculations)
conversion_button.grid(row=3, column=1, padx=10, pady=5, sticky="we")

converted_value_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
converted_value_label.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
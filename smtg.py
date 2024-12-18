import tkinter as tk
from tkinter import ttk

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x300")

        # Variables
        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.rate_var = tk.DoubleVar()
        self.result_var = tk.StringVar()

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Amount Label and Entry
        tk.Label(self.root, text="Amount:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.amount_var).grid(row=0, column=1, padx=10, pady=10)

        # From Currency Label and Entry
        tk.Label(self.root, text="From Currency:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.from_currency_var).grid(row=1, column=1, padx=10, pady=10)

        # To Currency Label and Entry
        tk.Label(self.root, text="To Currency:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.to_currency_var).grid(row=2, column=1, padx=10, pady=10)

        # Exchange Rate Label and Entry
        tk.Label(self.root, text="Exchange Rate:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.rate_var).grid(row=3, column=1, padx=10, pady=10)

        # Convert Button
        ttk.Button(self.root, text="Convert", command=self.convert_currency).grid(row=4, column=0, columnspan=2, pady=20)

        # Result Label
        tk.Label(self.root, text="Converted Amount:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.result_var, state="readonly").grid(row=5, column=1, padx=10, pady=10)

    def convert_currency(self):
        try:
            amount = self.amount_var.get()
            rate = self.rate_var.get()
            if amount < 0 or rate <= 0:
                self.result_var.set("Invalid input")
            else:
                converted_amount = amount * rate
                self.result_var.set(f"{converted_amount:.2f}")
        except Exception as e:
            self.result_var.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
                

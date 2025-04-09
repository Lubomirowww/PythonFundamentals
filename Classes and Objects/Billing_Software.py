# Преработен вариант на интерфейса на BillingApp, така че да съответства на дизайна от снимката

import tkinter as tk
from tkinter import Text, filedialog, messagebox

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing Software")
        self.root.geometry("1050x650")
        self.root.configure(bg="lightgreen")

        # Заглавие
        title = tk.Label(root, text="Billing Software", font=("Arial", 24, "bold"), bg="lightgreen")
        title.grid(row=0, column=0, columnspan=4, pady=10)

        # Продукти и цени
        self.products = {
            "Medical Products": ["Sanitizer", "Face Mask", "Thermometer"],
            "Grocery Items": ["Rice", "Sugar", "Wheat"],
            "Cold Drinks": ["Coke", "Fanta", "Sprite"]
        }

        self.prices = {
            "Medical Products": [5, 2, 3],
            "Grocery Items": [1, 1, 2],
            "Cold Drinks": [1.5, 1.5, 1.5]
        }

        self.tax_rates = {
            "Medical Products": 0.05,
            "Grocery Items": 0.1,
            "Cold Drinks": 0.08
        }

        self.entries = {}

        # Създаване на продуктови колони
        col = 0
        for category in self.products:
            self.create_product_column(category, col)
            col += 1

        # Данни за клиент
        customer_frame = tk.Frame(root, bg="lightgreen")
        customer_frame.grid(row=1, column=3, padx=10, pady=10, sticky="n")

        tk.Label(customer_frame, text="Customer Name", bg="lightgreen", font=("Arial", 10, "bold")).grid(row=0, column=0)
        self.entry_name = tk.Entry(customer_frame, width=25)
        self.entry_name.grid(row=0, column=1, pady=2)

        tk.Label(customer_frame, text="Phone No.", bg="lightgreen", font=("Arial", 10, "bold")).grid(row=1, column=0)
        self.entry_phone = tk.Entry(customer_frame, width=25)
        self.entry_phone.grid(row=1, column=1, pady=2)

        tk.Label(customer_frame, text="Bill Number", bg="lightgreen", font=("Arial", 10, "bold")).grid(row=2, column=0)
        self.entry_bill = tk.Entry(customer_frame, width=25)
        self.entry_bill.grid(row=2, column=1, pady=2)

        # Текстово поле за бележката
        self.bill_text = Text(root, width=40, height=20, borderwidth=2)
        self.bill_text.grid(row=2, column=3, padx=10, pady=10, rowspan=2)

        # Бутони
        button_frame = tk.Frame(root, bg="lightgreen")
        button_frame.grid(row=4, column=3, pady=10)

        tk.Button(button_frame, text="Total", width=12, command=self.calculate_total).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Generate Bill", width=12, command=self.generate_bill).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Save", width=12, command=self.save_bill).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Clear", width=12, command=self.clear_all).grid(row=0, column=3, padx=5)

    def create_product_column(self, category, col):
        frame = tk.LabelFrame(self.root, text=category, font=("Arial", 12, "bold"), padx=10, pady=10, bg="lightgreen")
        frame.grid(row=1, column=col, padx=10, pady=10)
        self.entries[category] = []

        for i, product in enumerate(self.products[category]):
            tk.Label(frame, text=product, bg="lightgreen", font=("Arial", 10)).grid(row=i, column=0, sticky="w")
            entry = tk.Entry(frame, width=5)
            entry.insert(0, "0")
            entry.grid(row=i, column=1)
            self.entries[category].append(entry)

    def calculate_total(self):
        self.bill_text.delete("1.0", tk.END)
        total_amount = 0.0

        for category in self.products:
            subtotal = 0
            for i, entry in enumerate(self.entries[category]):
                quantity = int(entry.get())
                price = self.prices[category][i]
                subtotal += quantity * price
            tax = subtotal * self.tax_rates[category]
            total = subtotal + tax
            total_amount += total
            self.bill_text.insert(tk.END, f"{category} Subtotal: ${subtotal:.2f}\n")
            self.bill_text.insert(tk.END, f"{category} Tax: ${tax:.2f}\n")
            self.bill_text.insert(tk.END, f"{category} Total: ${total:.2f}\n\n")

        self.bill_text.insert(tk.END, f"Final Total: ${total_amount:.2f}\n")

    def generate_bill(self):
        self.bill_text.delete("1.0", tk.END)
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        bill_no = self.entry_bill.get()
        self.bill_text.insert(tk.END, f"Customer Name: {name}\n")
        self.bill_text.insert(tk.END, f"Phone No.: {phone}\n")
        self.bill_text.insert(tk.END, f"Bill No.: {bill_no}\n")
        self.bill_text.insert(tk.END, "-" * 30 + "\n")

        for category in self.products:
            for i, entry in enumerate(self.entries[category]):
                quantity = int(entry.get())
                if quantity > 0:
                    product = self.products[category][i]
                    price = self.prices[category][i] * quantity
                    self.bill_text.insert(tk.END, f"{product} x{quantity} = ${price:.2f}\n")

        self.bill_text.insert(tk.END, "-" * 30 + "\n")
        self.calculate_total()

    def save_bill(self):
        content = self.bill_text.get("1.0", tk.END)
        if content.strip() == "":
            messagebox.showwarning("Warning", "Bill is empty.")
            return

        file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file:
            file.write(content)
            file.close()
            messagebox.showinfo("Saved", "Bill saved successfully.")

    def clear_all(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_bill.delete(0, tk.END)
        for category_entries in self.entries.values():
            for entry in category_entries:
                entry.delete(0, tk.END)
                entry.insert(0, "0")
        self.bill_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()
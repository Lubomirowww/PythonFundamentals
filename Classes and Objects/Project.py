import tkinter as tk
from tkinter import Text, filedialog, messagebox

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mitko's Billing Software")
        self.root.geometry("1050x650")
        self.root.configure(bg="light green")

        self.products = {
            "Medical Products": ["Sanitizer", "Face Mask", "Hand Gloves", "Hair Shampoo", "Soap Dove", "Toothpaste"],
            "Grocery Items": ["Pizza", "Bread", "Sushi", "Milk", "Flour", "Spaghetti"],
            "Drinks": ["Coffee", "RedBull", "Coke", "Fanta", "Sprite", "Mineral Water"]
        }

        self.prices = {
            "Medical Products": [5, 2, 3, 4, 2.5, 3.5],
            "Grocery Items": [6, 1.5, 8, 2, 1.2, 3],
            "Drinks": [2.5, 3.5, 2.2, 2.3, 2, 1]
        }

        self.tax_rates = {
            "Medical Products": 0.05,
            "Grocery Items": 0.08,
            "Drinks": 0.10
        }

        self.entries = {}

        # === Customer Info ===
        tk.Label(root, text="Customer Name:", bg="grey").grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1)

        tk.Label(root, text="Phone:", bg="grey").grid(row=0, column=2)
        self.entry_phone = tk.Entry(root)
        self.entry_phone.grid(row=0, column=3)

        tk.Label(root, text="Bill No:", bg="grey").grid(row=0, column=4)
        self.entry_bill = tk.Entry(root)
        self.entry_bill.grid(row=0, column=5)

        # === Product Columns ===
        self.create_product_column("Medical Products", 0)
        self.create_product_column("Grocery Items", 2)
        self.create_product_column("Drinks", 4)

        # === Bill Area ===
        self.bill_text = Text(root, width=35, height=20)
        self.bill_text.grid(row=2, column=6, rowspan=10, padx=10, pady=10)

        # === Buttons ===
        tk.Button(root, text="Total", command=self.calculate_total).grid(row=12, column=2, pady=10)
        tk.Button(root, text="Generate Bill", command=self.generate_bill).grid(row=12, column=3, pady=10)
        tk.Button(root, text="Save", command=self.save_bill).grid(row=12, column=4, pady=10)
        tk.Button(root, text="Clear", command=self.clear_all).grid(row=12, column=5, pady=10)

    def create_product_column(self, category, col):
        tk.Label(self.root, text=category, font=('Arial', 10, 'bold'), bg="grey").grid(row=1, column=col, padx=10)
        self.entries[category] = []
        for i, item in enumerate(self.products[category]):
            tk.Label(self.root, text=item, bg="grey").grid(row=i+2, column=col, sticky="w", padx=10)
            entry = tk.Entry(self.root, width=5)
            entry.insert(0, "0")
            entry.grid(row=i+2, column=col+1)
            self.entries[category].append(entry)

    def calculate_total(self):
        self.bill_text.delete("1.0", tk.END)
        total = 0
        tax_total = 0
        for cat in self.products:
            subtotal = 0
            for i, e in enumerate(self.entries[cat]):
                qty = int(e.get())
                price = self.prices[cat][i]
                subtotal += qty * price
            tax = subtotal * self.tax_rates[cat]
            total += subtotal
            tax_total += tax
            self.bill_text.insert(tk.END, f"{cat}:\nSubtotal: {subtotal:.2f} лв | Tax: {tax:.2f} лв\n\n")

        grand_total = total + tax_total
        self.bill_text.insert(tk.END, "===========================\n")
        self.bill_text.insert(tk.END, f"Grand Total: {grand_total:.2f} лв\n")

    def generate_bill(self):
        self.bill_text.delete("1.0", tk.END)
        self.bill_text.insert(tk.END, f"SoftUni Billing System\n")
        self.bill_text.insert(tk.END, f"Bill No: {self.entry_bill.get()}\n")
        self.bill_text.insert(tk.END, f"Customer: {self.entry_name.get()}\n")
        self.bill_text.insert(tk.END, f"Phone: {self.entry_phone.get()}\n")
        self.bill_text.insert(tk.END, "===========================\n")
        self.bill_text.insert(tk.END, "Products\tQty\tPrice\n")
        self.bill_text.insert(tk.END, "---------------------------\n")

        for cat in self.products:
            for i, e in enumerate(self.entries[cat]):
                qty = int(e.get())
                if qty > 0:
                    name = self.products[cat][i]
                    price = self.prices[cat][i]
                    self.bill_text.insert(tk.END, f"{name}\t{qty}\t{qty*price:.2f}\n")

        self.bill_text.insert(tk.END, "---------------------------\n")
        self.calculate_total()

    def save_bill(self):
        bill_content = self.bill_text.get("1.0", tk.END)
        if not bill_content.strip():
            messagebox.showwarning("Warning", "No bill to save!")
            return
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, "w", encoding='utf-8') as file:
                file.write(bill_content)
            messagebox.showinfo("Saved", f"Bill saved as {filename}")

    def clear_all(self):
        for cat in self.entries:
            for entry in self.entries[cat]:
                entry.delete(0, tk.END)
                entry.insert(0, "0")
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_bill.delete(0, tk.END)
        self.bill_text.delete("1.0", tk.END)

# === Стартираме приложението ===
if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()

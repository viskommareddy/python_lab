import tkinter as tk

class BillingSystem:

    def __init__(self, master):
        self.master = master
        master.title("Billing System")

        # Create labels and entries for item name, quantity, and price
        self.item_label = tk.Label(master, text="Item Name:")
        self.item_label.grid(row=0, column=0, padx=5, pady=5)
        self.item_entry = tk.Entry(master)
        self.item_entry.grid(row=0, column=1, padx=5, pady=5)

        self.quantity_label = tk.Label(master, text="Quantity:")
        self.quantity_label.grid(row=1, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        self.price_label = tk.Label(master, text="Price:")
        self.price_label.grid(row=2, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(master)
        self.price_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create a button to add item to the bill
        self.add_button = tk.Button(master, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=1, padx=5, pady=5)

        # Create a text widget to display the bill
        self.bill_text = tk.Text(master, height=10, width=40)
        self.bill_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Create a button to calculate the total and clear the bill
        self.total_button = tk.Button(master, text="Calculate Total", command=self.calculate_total)
        self.total_button.grid(row=5, column=0, padx=5, pady=5)
        self.clear_button = tk.Button(master, text="Clear Bill", command=self.clear_bill)
        self.clear_button.grid(row=5, column=1, padx=5, pady=5)

        # Initialize the bill list and total
        self.bill_list = []
        self.total = 0

    def add_item(self):
        # Get the item name, quantity, and price from the entry fields
        item_name = self.item_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())

        # Add the item to the bill list and update the bill text widget
        self.bill_list.append((item_name, quantity, price))
        self.bill_text.insert(tk.END, f"{item_name} x {quantity} = {quantity * price:.2f}\n")

        # Clear the entry fields
        self.item_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def calculate_total(self):
        # Calculate the total and update the bill text widget
        self.total = sum([quantity * price for item_name, quantity, price in self.bill_list])
        self.bill_text.insert(tk.END, f"Total: {self.total:.2f}\n")

    def clear_bill(self):
        # Clear the bill list and total, and update the bill text widget
        self.bill_list = []
        self.total = 0
        self.bill_text.delete("1.0", tk.END)

# Create the GUI window and run the main loop
root = tk.Tk()
billing_system = BillingSystem(root)
root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Menu items with prices
menu = {
    'Pizza': 400,
    'Pasta': 300,
    'Coffee': 100,
    'Shake': 140,
    'Steak': 250
}

order_items = []
order_total = 0

# Function to add item
def add_item(item):
    global order_total
    order_items.append(item)
    order_total += menu[item]
    order_listbox.insert(tk.END, f"{item} - ₹{menu[item]}")
    total_label.config(text=f"Total: ₹{order_total}")

# Function to show the final bill
def show_bill():
    if not order_items:
        messagebox.showinfo("Empty", "No items in order.")
        return

    bill_text = "\n".join([f"{item} - ₹{menu[item]}" for item in order_items])
    bill_text += f"\n\nTotal: ₹{order_total}"
    messagebox.showinfo("Your Bill", bill_text)

# Function to reset the entire order
def reset_order():
    global order_total
    order_items.clear()
    order_total = 0
    order_listbox.delete(0, tk.END)
    total_label.config(text="Total: ₹0")

# Function to remove a selected item
def remove_selected_item():
    global order_total
    selected_index = order_listbox.curselection()

    if selected_index:
        item_line = order_listbox.get(selected_index)
        item_name = item_line.split(" - ₹")[0]
        order_items.remove(item_name)
        order_total -= menu[item_name]
        order_listbox.delete(selected_index)
        total_label.config(text=f"Total: ₹{order_total}")
    else:
        messagebox.showinfo("No selection", "Please select an item to remove.")

# Main GUI window
root = tk.Tk()
root.title("Zeromiles Restaurant - Order System")
root.geometry("400x550")

tk.Label(root, text="Welcome to Zeromiles Kupwara", font=("Helvetica", 16)).pack(pady=10)

# Create a button for each menu item
for item in menu:
    tk.Button(root, text=f"{item} - ₹{menu[item]}", width=30, command=lambda i=item: add_item(i)).pack(pady=2)

# Order summary
tk.Label(root, text="\nOrder Summary:").pack()
order_listbox = tk.Listbox(root, width=40)
order_listbox.pack()

# Total bill label
total_label = tk.Label(root, text="Total: ₹0", font=("Helvetica", 14))
total_label.pack(pady=10)

# Action buttons
tk.Button(root, text="Show Bill", command=show_bill).pack(pady=5)
tk.Button(root, text="Reset Order", command=reset_order).pack(pady=5)
tk.Button(root, text="Remove Selected Item", command=remove_selected_item).pack(pady=5)

# Run the application
root.mainloop()
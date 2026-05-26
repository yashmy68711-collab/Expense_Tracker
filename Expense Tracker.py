import tkinter as tk
from tkinter import messagebox

expenses = []
total = 0

def add_expense():
    global total

    item = item_entry.get().strip()
    amount = amount_entry.get().strip()

    if item == "" or amount == "":
        messagebox.showerror(
            "Error",
            "Fill all fields"
        )
        return

    try:
        amount = float(amount)
    except:
        messagebox.showerror(
            "Error",
            "Enter valid amount"
        )
        return

    expenses.append(f"{item} - ₹{amount}")

    expense_list.insert(tk.END,
    f"{item} - ₹{amount}")

    total += amount

    total_label.config(
        text=f"Total: ₹{total}"
    )

    item_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Expense Tracker")
window.geometry("400x400")

title = tk.Label(
    window,
    text="Expense Tracker",
    font=("Arial", 16, "bold")
)

title.pack(pady=10)

tk.Label(window, text="Expense Name").pack()

item_entry = tk.Entry(window, width=30)
item_entry.pack(pady=5)

tk.Label(window, text="Amount").pack()

amount_entry = tk.Entry(window, width=30)
amount_entry.pack(pady=5)

tk.Button(
    window,
    text="Add Expense",
    command=add_expense,
    width=20
).pack(pady=10)

expense_list = tk.Listbox(
    window,
    width=40,
    height=10
)

expense_list.pack(pady=10)

total_label = tk.Label(
    window,
    text="Total: ₹0",
    font=("Arial", 12, "bold")
)

total_label.pack()

window.mainloop()
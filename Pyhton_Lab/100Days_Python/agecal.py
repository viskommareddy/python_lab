import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        birth_date = datetime.strptime(entry_birth_date.get(), '%m/%d/%Y')
        today_date = datetime.now()
        age = today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))
        messagebox.showinfo('Age Calculator', f'Your age is {age} years')
    except ValueError:
        messagebox.showerror('Age Calculator', 'Please enter a valid birth date in the format MM/DD/YYYY')

# Create a Tkinter window
root = tk.Tk()
root.title('Age Calculator')

# Create labels and entry boxes
label_birth_date = tk.Label(root, text='Enter your birth date (MM/DD/YYYY):', font=('Helvetica', 12))
label_birth_date.pack(pady=10)
entry_birth_date = tk.Entry(root, font=('Helvetica', 12))
entry_birth_date.pack(pady=10)

# Create a button to calculate age
button_calculate_age = tk.Button(root, text='Calculate Age', font=('Helvetica', 12), command=calculate_age)
button_calculate_age.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

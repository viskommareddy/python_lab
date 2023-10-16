import tkinter as tk
from datetime import datetime
# Create the GUI window
root = tk.Tk()
root.geometry('250x100')
root.title('Digital Clock')

# Create the clock label
clock_label = tk.Label(root, font=('Verdana', 24, 'bold'), bg='white')
clock_label.pack(fill=tk.BOTH, expand=1)
# Function to get the current time
def get_time():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, get_time)
get_time()

root.mainloop()

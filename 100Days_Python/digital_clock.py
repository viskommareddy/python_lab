import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # create input field
        self.input_field = tk.Entry(master, width=30, justify='right')
        self.input_field.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # create number buttons
        for i in range(10):
            button = tk.Button(master, text=str(i), padx=15, pady=10, command=lambda num=i: self.input_number(num))
            button.grid(row=(i // 3) + 1, column=(i % 3), padx=5, pady=5)

        # create operation buttons
        tk.Button(master, text="+", padx=15, pady=10, command=lambda: self.operation("+")).grid(row=1, column=3, padx=5, pady=5)
        tk.Button(master, text="-", padx=15, pady=10, command=lambda: self.operation("-")).grid(row=2, column=3, padx=5, pady=5)
        tk.Button(master, text="*", padx=15, pady=10, command=lambda: self.operation("*")).grid(row=3, column=3, padx=5, pady=5)
        tk.Button(master, text="/", padx=15, pady=10, command=lambda: self.operation("/")).grid(row=4, column=3, padx=5, pady=5)
        tk.Button(master, text="^", padx=15, pady=10, command=lambda: self.operation("**")).grid(row=5, column=3, padx=5, pady=5)
        tk.Button(master, text="√", padx=15, pady=10, command=lambda: self.operation("sqrt")).grid(row=1, column=4, padx=5, pady=5)
        tk.Button(master, text="sin", padx=15, pady=10, command=lambda: self.operation("sin")).grid(row=2, column=4, padx=5, pady=5)
        tk.Button(master, text="cos", padx=15, pady=10, command=lambda: self.operation("cos")).grid(row=3, column=4, padx=5, pady=5)
        tk.Button(master, text="tan", padx=15, pady=10, command=lambda: self.operation("tan")).grid(row=4, column=4, padx=5, pady=5)
        tk.Button(master, text="log", padx=15, pady=10, command=lambda: self.operation("log")).grid(row=5, column=4, padx=5, pady=5)

        # create clear and equal buttons
        tk.Button(master, text="C", padx=15, pady=10, command=self.clear).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(master, text="=", padx=15, pady=10, command=self.calculate).grid(row=5, column=2, padx=5, pady=5)

    # function to add input numbers to the input field
    def input_number(self, num):
        current = self.input_field.get()
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, str(current) + str(num))

    # function to handle arithmetic operations
    def operation(self, op):
        if op == "sqrt":
            current = float(self.input_field.get())
            self.input_field

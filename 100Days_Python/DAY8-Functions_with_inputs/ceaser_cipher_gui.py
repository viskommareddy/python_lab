from tkinter import *

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    return end_text

def submit():
    direction = direction_entry.get()
    text = text_entry.get().lower()
    shift = int(shift_entry.get())
    if direction == "decode":
        shift *= -1
    result_text.delete(0.0, END)
    result = ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
    result_text.insert(END, result)

root = Tk()
root.title("Caesar Cipher")

welcome_label = Label(root, text="Welcome to Vishnu's  Cipher")
welcome_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

direction_label = Label(root, text="Enter 'encode' for encryption of the text (or) enter 'decode' for decryption of the code.")
direction_label.grid(row=1, column=0, padx=10, pady=10)

direction_entry = Entry(root, width=30)
direction_entry.grid(row=1, column=1, padx=10, pady=10)

text_label = Label(root, text="Enter the text that is to be processed")
text_label.grid(row=2, column=0, padx=10, pady=10)

text_entry = Entry(root, width=30)
text_entry.grid(row=2, column=1, padx=10, pady=10)

shift_label = Label(root, text="Enter the number for shifting")
shift_label.grid(row=3, column=0, padx=10, pady=10)

shift_entry = Entry(root, width=30)
shift_entry.grid(row=3, column=1, padx=10, pady=10)

submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

result_label = Label(root, text="Result:")
result_label.grid(row=5, column=0, padx=10, pady=10)

result_text = Text(root, width=30, height=5)
result_text.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()

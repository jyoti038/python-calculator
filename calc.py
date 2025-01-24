import tkinter as tk

# Function to perform the calculation
def calculate():
    try:
        result = eval(entry.get())  # eval safely evaluates the entered expression
        label_result.config(text="Result: " + str(result))
    except Exception as e:
        label_result.config(text="Error! Invalid input")

# Function to update the entry box when a button is clicked
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Setting up the main window
window = tk.Tk()
window.title("Calculator")

# Entry widget for user input
entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Creating buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Adding buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, width=10, height=2, font=("Arial", 18), command=calculate)
    elif text == 'C':
        button = tk.Button(window, text=text, width=10, height=2, font=("Arial", 18), command=clear)
    else:
        button = tk.Button(window, text=text, width=10, height=2, font=("Arial", 18), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Label to show the result
label_result = tk.Label(window, text="Result: ", font=("Arial", 18))
label_result.grid(row=5, column=0, columnspan=4)

# Run the application
window.mainloop()

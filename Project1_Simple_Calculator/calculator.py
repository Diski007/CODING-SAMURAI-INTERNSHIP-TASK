import tkinter as tk

# Global expression string
expression = ""

# Function to handle button press
def press(symbol):
    global expression
    expression += str(symbol)
    screen.set(expression)

# Function to evaluate the expression
def calculate():
    global expression
    try:
        result = str(eval(expression))
        screen.set(result)
        expression = result  # Allow chaining calculations
    except:
        screen.set("Error")
        expression = ""

# Function to clear the screen
def clear():
    global expression
    expression = ""
    screen.set("")

# Function to delete the last character
def delete_last():
    global expression
    expression = expression[:-1]
    screen.set(expression)

# Set up GUI window
root = tk.Tk()
root.title("Calculator by Vincent")
root.geometry("300x400")


# Display field
screen = tk.StringVar()
display = tk.Entry(root, textvariable=screen, font=("Arial", 20), bd=10, insertwidth=2,
                   width=14, borderwidth=4, justify='right')
display.grid(row=0, column=0, columnspan=4)


# --- Number Buttons ---
btn_1 = tk.Button(root, text="1", command=lambda: press("1"), height=2, width=5, font=("Arial", 16))
btn_1.grid(row=3, column=0)

btn_2 = tk.Button(root, text="2", command=lambda: press("2"), height=2, width=5, font=("Arial", 16))
btn_2.grid(row=3, column=1)

btn_3 = tk.Button(root, text="3", command=lambda: press("3"), height=2, width=5, font=("Arial", 16))
btn_3.grid(row=3, column=2)

btn_4 = tk.Button(root, text="4", command=lambda: press("4"), height=2, width=5, font=("Arial", 16))
btn_4.grid(row=2, column=0)

btn_5 = tk.Button(root, text="5", command=lambda: press("5"), height=2, width=5, font=("Arial", 16))
btn_5.grid(row=2, column=1)

btn_6 = tk.Button(root, text="6", command=lambda: press("6"), height=2, width=5, font=("Arial", 16))
btn_6.grid(row=2, column=2)

btn_7 = tk.Button(root, text="7", command=lambda: press("7"), height=2, width=5, font=("Arial", 16))
btn_7.grid(row=1, column=0)

btn_8 = tk.Button(root, text="8", command=lambda: press("8"), height=2, width=5, font=("Arial", 16))
btn_8.grid(row=1, column=1)

btn_9 = tk.Button(root, text="9", command=lambda: press("9"), height=2, width=5, font=("Arial", 16))
btn_9.grid(row=1, column=2)

btn_0 = tk.Button(root, text="0", command=lambda: press("0"), height=2, width=5, font=("Arial", 16))
btn_0.grid(row=4, column=1)

# --- Operator Buttons ---
btn_add = tk.Button(root, text="+", command=lambda: press("+"), height=2, width=5, font=("Arial", 16))
btn_add.grid(row=1, column=3)

btn_sub = tk.Button(root, text="-", command=lambda: press("-"), height=2, width=5, font=("Arial", 16))
btn_sub.grid(row=2, column=3)

btn_mul = tk.Button(root, text="*", command=lambda: press("*"), height=2, width=5, font=("Arial", 16))
btn_mul.grid(row=3, column=3)

btn_div = tk.Button(root, text="/", command=lambda: press("/"), height=2, width=5, font=("Arial", 16))
btn_div.grid(row=4, column=3)

# --- Control Buttons ---
btn_clear = tk.Button(root, text="C", command=clear, height=2, width=5, font=("Arial", 16))
btn_clear.grid(row=4, column=0)

btn_equal = tk.Button(root, text="=", command=calculate, height=2, width=5, font=("Arial", 16))
btn_equal.grid(row=4, column=2)

btn_del = tk.Button(root, text="DEL", command=delete_last, height=2, width=5, font=("Arial", 16))
btn_del.grid(row=5, column=3)

# Optional: Add more rows if needed
root.mainloop()

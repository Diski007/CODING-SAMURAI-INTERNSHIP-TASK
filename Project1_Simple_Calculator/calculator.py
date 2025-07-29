import tkinter as tk

calculation = ""

def add_calculator(symbol):
    global calculation
    calculation += str(symbol)
    text_screen.delete(1.0, "end")
    text_screen.insert(1.0, calculation)
    
    
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_screen.delete(1.0, "end")
        text_screen.insert(1.0, calculation)
         
    except:
        clearfield()
        text_screen.insert(1.0, "Error") 
        
def delete_last_character():
    global calculation
    calculation = calculation[:-1]
    text_screen.delete(1.0, "end")
    text_screen.insert(1.0, calculation)

def clearfield():
    global calculation
    calculation = ""
    text_screen.delete(1.0, "end")
    pass

root = tk.Tk()
root.geometry("300x400")
root.title("Calculator by Vincent")
root.iconbitmap(r"C:\Users\DELL\Desktop\Python_test\Pyth__samurai_train\Project1_Simple_Calculator\calculator.ico")
text_screen = tk.Text(root, height=2, width=25, font=("Arial", 16))
text_screen.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_calculator(1), height=2, width=5, font=("Arial", 16))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_calculator(2), height=2, width=5, font=("Arial", 16))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_calculator(3), height=2, width=5, font=("Arial", 16))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_calculator(4), height=2, width=5, font=("Arial", 16))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_calculator(5), height=2, width=5, font=("Arial", 16))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_calculator(6), height=2, width=5, font=("Arial", 16))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_calculator(7), height=2, width=5, font=("Arial", 16))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_calculator(8), height=2, width=5, font=("Arial", 16))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_calculator(9), height=2, width=5, font=("Arial", 16))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_calculator(0), height=2, width=5, font=("Arial", 16))
btn_0.grid(row=5, column=1)
btn_plus = tk.Button(root, text="+", command=lambda: add_calculator("+"), height=2, width=5, font=("Arial", 16))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_calculator("-"), height=2, width=5, font=("Arial", 16))
btn_minus.grid(row=3, column=4)
btn_multiply = tk.Button(root, text="*", command=lambda: add_calculator("*"), height=2, width=5, font=("Arial", 16))
btn_multiply.grid(row=4, column=4)
btn_divide = tk.Button(root, text="/", command=lambda: add_calculator("/"), height=2, width=5, font=("Arial", 16))
btn_divide.grid(row=5, column=4)
btn_equal = tk.Button(root, text="=", command=evaluate_calculation, height=2, width=15, font=("Arial", 16))
btn_equal.grid(row=6, columnspan=5)
btn_clear = tk.Button(root, text="C", command=clearfield, height=2, width=5, font=("Arial", 16))
btn_clear.grid(row=5, column=2)
btn_percentage = tk.Button(root, text="%", command=lambda: add_calculator("%"), height=2, width=5, font=("Arial", 16))
btn_percentage.grid(row=6, column=4)
btn_delete = tk.Button(root, text="DEL", command=delete_last_character, height=2, width=5, font=("Arial", 16))
btn_delete.grid(row=5, column=3)


root.mainloop()
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Arithmetic Calculator")
root.geometry("750x500")


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Invalid input.Must be a natural number"

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == '1':
            result = add(num1, num2)
        elif operation == '2':
            result = subtract(num1, num2)
        elif operation == '3':
            result = multiply(num1, num2)
        elif operation == '4':
            result = divide(num1, num2)
        
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input")

tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

operation_var = tk.StringVar()
operation_var.set('1')

tk.Radiobutton(root, text="Addition", variable=operation_var, value='1').grid(row=2, column=0)
tk.Radiobutton(root, text="Subtraction", variable=operation_var, value='2').grid(row=2, column=1)
tk.Radiobutton(root, text="Multiplication", variable=operation_var, value='3').grid(row=3, column=0)
tk.Radiobutton(root, text="Division", variable=operation_var, value='4').grid(row=3, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=4, column=0, columnspan=2)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()

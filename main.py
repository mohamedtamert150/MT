import tkinter as tk
from math import sqrt, sin, cos, tan, log, pi, e

# Function to handle button presses
def button_press(value):
    current = input_field.get()
    if value == "C":
        input_field.delete(0, tk.END)
    elif value == "=":
        try:
            # Replace '÷' with '/' and '×' with '*' for evaluation
            expression = current.replace("÷", "/").replace("×", "*")
            result = eval(expression)
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, str(result))
        except Exception:
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, "Error")
    elif value == "√":
        try:
            result = sqrt(float(current))
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, str(result))
        except Exception:
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, "Error")
    elif value == "^":
        input_field.insert(tk.END, "**")
    elif value == "π":
        input_field.insert(tk.END, str(pi))
    elif value == "e":
        input_field.insert(tk.END, str(e))
    else:
        input_field.insert(tk.END, value)

# Create main application window
app = tk.Tk()
app.title("Calculator")
app.geometry("400x600")
app.resizable(False, False)
app.configure(bg="#333")  # Background: Dark gray

# Input field
input_field = tk.Entry(
    app, font=("Arial", 28), bd=10, insertwidth=2, width=14, justify="right", bg="#222", fg="white"
)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Buttons for the calculator
buttons = [
    ("C", "#ff6666"), ("√", "#ffcc66"), ("^", "#ffcc66"), ("÷", "#ffcc66"),
    ("7", "#666"), ("8", "#666"), ("9", "#666"), ("×", "#ffcc66"),
    ("4", "#666"), ("5", "#666"), ("6", "#666"), ("-", "#ffcc66"),
    ("1", "#666"), ("2", "#666"), ("3", "#666"), ("+", "#ffcc66"),
    ("0", "#666"), (".", "#666"), ("=", "#66cc66"), ("π", "#666"),
    ("sin", "#666"), ("cos", "#666"), ("tan", "#666"), ("log", "#666"),
    ("e", "#666"), ("(", "#666"), (")", "#666"), ("", "#333")
]

# Create buttons
row = 1
col = 0
for text, color in buttons:
    if text != "":
        btn = tk.Button(
            app, text=text, font=("Arial", 20), bg=color, fg="white",
            width=5, height=2, command=lambda value=text: button_press(value)
        )
        btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
app.mainloop()

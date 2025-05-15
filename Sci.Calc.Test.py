from tkinter import *
import math
import re
from CalculationCore import evaluate_expression
from memory import Memory

#create the window
window = Tk()

#set size of window to full screen always once launched
window.geometry("300x500")
window.title("Scientific Calculator")

# Create the grid structure of the window
window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=6)
window.grid_columnconfigure(1, weight = 1)

# Memory navigation backwards
def show_previous_calculation():
    global history_index
    if not history_list:
        history.delete(0, END)
        history.insert(0, "No History")
        return

    history_index += 1
    if history_index >= len(history_list):
        history_index = 0  # Loop back to most recent

    history.delete(0, END)
    history.insert(0, history_list[history_index])

# Memory navigation fowards
def show_next_calculation():
    global history_index
    if not history_list:
        history.delete(0, END)
        history.insert(0, "No History")
        return

    history_index -= 1
    if history_index < 0:
        history_index = len(history_list) - 1  # Loop to oldest

    history.delete(0, END)
    history.insert(0, history_list[history_index])


header = Frame(window , bg = "green")
header.grid(row = 0, column = 1, padx= 3, pady=2, sticky = "nesw")

header.columnconfigure(0, weight=1)
prev_btn = Button(header, text= "⬆", font=("Arial", 10, "bold"), command= show_previous_calculation).grid(row=0, column=0, ipadx= 10, padx=5, pady=5, sticky="w")
prev_btn = Button(header, text= "History", font=("Arial", 10, "bold"), command= show_previous_calculation).grid(row=0, column=0, ipadx= 10, padx=5, pady=5, sticky="n")
prev_btn = Button(header, text= "⬇", font=("Arial", 10, "bold"), command= show_next_calculation).grid(row=0, column=0, ipadx= 10, padx=5, pady=5, sticky="e")

# Create the result diplay area
history = Entry(window, font=("Helvetica", 30), bg = "white", fg = "black",  justify="right")
history.grid(row = 1, column = 1, padx= 3, pady=2, sticky = "nesw")
history.insert(0, "0")
# Create the calculations area
calc = Frame(window, bg = "green")
calc.grid(row = 2, column = 1, padx= 3, pady=2, sticky = "nesw")

calc_list = [
    ['sin(', 'cos(', 'tan(', 'log(', 'ln'],
    ['!', '^', '(', ')', '√'],
    ['MC', 'AC', '%', 'DEL', '÷'],
    ['MR', '7', '8', '9', 'x'],
    ['M+', '4', '5', '6', '+'],
    ['M-', '1', '2', '3', '-'],
    ['e', 'π', '0', '.', '='],
]

memory = Memory()
last_answer = 0

history_list = []
history_index = -1

last_input = False

def on_button_click(value):
    global history_index, last_answer, last_input
    current = history.get()

    if value == "AC":
        history.delete(0, END)
        history.insert(0, "0")
        return
    elif value == "DEL":
        history.delete(len(current)-1, END) if len(current) > 1 else history.delete(0, END)
        if len(current) <= 1:
            history.insert(0, "0")
        return
    elif value == "=":
        result = evaluate_expression(current)
        if result != "Error":
            last_answer = float(result)
            history_list.insert(0, result)
            history_index = -1
        history.delete(0, END)
        history.insert(0, result)
        return
    elif value == "MC":
        memory.clear()
        history_index = -1
        history.delete(0, END)
        history.insert(0, "No History")
        
        return
    elif value == "MR":
        history.delete(0, END)
        history.insert(0, str(memory.recall()))
        return
    elif value == "M+":
        try:
            memAdd = int(current) + int(last_answer)
            memAdd2 = str(memAdd)
            result = eval(memAdd2)
            last_answer = result
            history_list.insert(0, str(result))
            history_index = -1
            history.delete(0, END)
            history.insert(0, str(memAdd2))
        except ValueError:
            pass
        return
    elif value == "M-":
        try:
            memAdd = int(current) - int(last_answer)
            memAdd2 = str(memAdd)
            result = eval(memAdd2)
            last_answer = result
            history_list.insert(0, str(result))
            history_index = -1
            history.delete(0, END)
            history.insert(0, str(memAdd2))
        except ValueError:
            pass
        return

    if current == "0" or current == "Error" or last_input:
        history.delete(0, END)
        last_input = False
    history.insert(END, value)

# Bind Enter key to "="
window.bind('<Return>', lambda event: on_button_click('='))
# Bind Backspace key to "DEL"
window.bind('<BackSpace>', lambda event: on_button_click('DEL'))
# Bind Up arrow to "Previous"
window.bind('<Up>', lambda event: show_previous_calculation())
# Bind Down arrow to "Next"
window.bind('<Down>', lambda event: show_next_calculation())

# Loop for the calculation buttons and customization.
for row in range(1, 8):
    calc.grid_rowconfigure(row, weight=1)
    for col in range(5):
        calc.grid_columnconfigure(col, weight=1)
        btn = calc_list[row - 1][col]
        if not btn:
            continue
        btn_mod = {"text": btn}
        if btn in ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']:
            btn_mod["fg"] = "red"
            btn_mod["font"] = ("Helvetica", 12, "bold")
        Button(calc, **btn_mod, command=lambda b=btn: on_button_click(b)).grid(
            row=row, column=col, padx=5, pady=5, sticky="nsew"
        )

# Run the GUI
window.mainloop()
import webbrowser
import math
from utils.configure import base_color
from utils.history_widget import update_history
from utils.shared_history import add_calculation
from utils.winmain_module import entry_result, equation
from tkinter import END




#symbols function to write them in entry
def show(value):
    global equation
    equation += value
    entry_result.delete(0, END)
    entry_result.insert(0, equation)


#function to C button (clear whole entry)
def clear():
    global equation
    equation = ""
    entry_result.delete(0, END)

#calculate standard actions (1 + 1, etc.)

def calculate():
    global equation
    result = ""
    h_result = ""
    if equation != "":
        try:
            #calculation for root with specified base
            if '√' in equation:
                base, number = equation.split('√')  # Split into base and number
                base = float(base)
                number = float(number)
                if number < 0 and base % 2 == 0:
                    result = "Mathematical Error"  # Even root of a negative number
                else:
                    result = number ** (1 / base)  # Calculate the root

            # calculation for logarithm with specified base
            elif 'log' in equation:
                base, number = equation.split('log')
                base = float(base)
                number = float(number)
                if number <= 0 or base <= 0 or base == 1:
                    result = "Mathematical Error"  # Invalid logarithm input
                else:
                    result = math.log(number, base)  # Calculate the logarithm
            elif "lavish" in equation:
                webbrowser.open_new("https://www.youtube.com/watch?v=flYgpeWsC2E")
                result = "Welcome To The New Way Of Living"
                add_calculation("|-/")
            # Handle regular expressions (e.g., 2 + 3 * 4)
            else:
                result = eval(equation)
        except Exception as e:
            result = "Syntax Error"

    # Update the result in the entry widget
    entry_result.delete(0, END)
    entry_result.insert(0, result)

    h_result = str(result)
    # Add the calculation to the history
    if result != "Syntax Error" and result != "Mathematical Error" and result != "":
        add_calculation(f"{equation} = {h_result}")  # Append equation and result to history
        update_history()  # Update the history display

    # Clear the equation for the next input
    equation = ""


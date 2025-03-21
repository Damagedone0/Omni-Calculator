#library and file imports
from tkinter import *
import customtkinter
import customtkinter as ctk
import webbrowser
import math
from utils.shared_history import add_calculation
from utils.winmain_module import equation, entry_result




#calculate functions as log2,square root, sin, cos and etc.
#work after writing in entry a number and press buttons with scientific functions
def math_func(func_name, base="None"):
    global equation
    equation = entry_result.get()
    result = ""

    if equation != "":
        try:
            # Get the number from the entry widget
            number = float(entry_result.get())

            # Handle logarithm with base
            if func_name == "log":
                func_result = math.log(number)  # Calculate log with specified base
                add_calculation(f"ln({number}) = {func_result}")
            elif func_name == "change_sign":
                func_result = number * -1
                add_calculation(f"({number}) * -1 = {func_result}")
            elif func_name == "log10":
                func_result = math.log(number,10)  # Default is natural log
                add_calculation(f"log10({number}) = {func_result}")
            elif func_name == "1/":
                func_result = 1/number
                add_calculation(f"1/{number} = {func_result}")
            elif func_name == "sqrt" and base != "None":
                base = float(base)  # Convert base to float
                func_result = number ** (1/base)  # Calculate root with specified base
                add_calculation(f"{base}√{number} = {func_result}")
            elif func_name == "sqrt":
                func_result = math.sqrt(number)  # Default is square root
                add_calculation(f"√{number} = {func_result}")
            elif func_name == "fac":
                number = int(entry_result.get())
                func_result = math.factorial(number)
                add_calculation(f"{number}! = {func_result}")
            elif func_name == "sin":
                func_result = float(math.sin(number))
                add_calculation(f"sin{number} = {func_result}")
            elif func_name == "cos":
                func_result = float(math.cos(number))
                add_calculation(f"cos{number} = {func_result}")
            elif func_name == "tan":
                func_result = float(math.tan(number))
                add_calculation(f"tan{number} = {func_result}")
            elif func_name == "log2":
                func_result = float(math.log(number,2))
                add_calculation(f"log2({number}) = {func_result}")
            elif func_name == "fabs":
                func_result = float(math.fabs(number))
                add_calculation(f"|{number}| = {func_result}")
            else:
                # Dynamically get the math function using getattr for other functions
                func = getattr(math, func_name)
                func_result = func(number)


            # Update result to include the function result
            result = str(func_result)

        except Exception as e:
            result = "Syntax Error"
            equation = ""

    # Update the entry widget with the result
    entry_result.delete(0, END)
    entry_result.insert(0, result)
    #clear last result after press any button or Clear(C)
    equation = ""



from tkinter import END
from utils.winmain_module import entry_result, equation
from utils.main_functions_module import calculate, show



# Function to handle keyboard input including Backspace
#if Enter is pressed, it calculates expression
#if backspace is pressed, it deletes last character in entry widget
def key_input(event):
    global equation
    if event.keysym == 'Return':
        calculate()
    elif event.keysym == 'BackSpace':
        equation = equation[:-1]
        entry_result.delete(0, END)
        entry_result.insert(0, equation)
        return "break"  # Prevent default behavior
    elif event.char:
        show(event.char)
        return "break"  # Prevent default behavior

#bind for make def key_input work
entry_result.bind('<Key>', key_input)


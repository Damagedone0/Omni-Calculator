# Imports from libs
# (Customtkinter, tkinter, math, PIL, webbrowser, currency_converter, matplotlib,sympy, numpy and etc)

from utils.additional_functions_module import *
from utils.menu_module import create_main_menu
from utils.history_widget import history_page
from utils.winmain_module import root, entry_result
from utils.math_module import math_func
from utils.main_functions_module import calculate, show, clear
from utils.calculator_modes import science_frame,basic_frame
from utils.entry_key_input import key_input
from utils.buttons_module import *



#initialize menu for use functions of calculator
menubar = create_main_menu(root = root)





#bind hotkeys for menu
root.bind("<Control-q>", lambda event: root.quit()) #close calculator
root.bind("<F1>", lambda event: about_win()) # open program "about" window
root.bind("<Control-h>", lambda event: history_page()) # open history journal
root.bind("<Control-g>", lambda event: graph_build_win()) # open graph window
root.bind("<F2>", lambda event: author_page()) # open github's repository with calculator
root.bind("<Control-u>",lambda event: Units_Converter()) # open window for units converter
root.bind("<Control-n>",lambda event: translator_window()) # open window for convert System of numbers
root.bind("<Control-c>", lambda event: currency_win()) # open window for currency converter

#basic calculator buttons (from import)
basic_mode()

#scientific calculator buttons (from import)
scientific_mode()


#initialize main window and whole program
if __name__ == "__main__":
    root.mainloop()




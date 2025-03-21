#Imports from libraries to make app work
from tkinter import *
import customtkinter as ctk
import customtkinter
import tkinter as tk
from utils.additional_functions_module import (
    graph_build_win, translator_window, currency_win, Units_Converter,
      about_win, author_page
    )
from utils.configure import base_color,hover_color
from utils.winmain_module import root
from utils.history_widget import history_page
from utils.calculator_modes import set_calculator_mode

#Menu Code
def create_main_menu(root):
    menu = Menu(root)
    

    
    # Select Types of Calculator
    program_menu = Menu(menu,tearoff = 0)
    type_menu = Menu(program_menu, tearoff=0)
    program_menu.add_cascade(label="Change Calculator Type", menu=type_menu) #Cascade for switch calculator's modes
    type_menu.add_command(label="Basic Calculator", command=lambda: set_calculator_mode("basic")) #basic calculator mode
    type_menu.add_command(label="Scientific Calculator", command=lambda: set_calculator_mode("scientific")) #scientific calculator mode
    
    #history (History) cascade
    program_menu.add_cascade(label="History", command=history_page, accelerator= 'Ctrl-H')
    #Creator's Page (cascade)
    program_menu.add_cascade(label="Creator's Page", command=author_page, accelerator="F2")
    #Exit Command
    menu.add_cascade(label="Program", menu=program_menu)
    program_menu.add_command(label="Exit", command=root.quit, accelerator='Ctrl+Q')

    #Cascade for Converters
    converter_menu = Menu(menu,tearoff = 0)
    converter = Menu(converter_menu)
    menu.add_cascade(label="Converters", menu=converter_menu)
    converter_menu.add_command(label="Numeral System", command= translator_window, accelerator='Ctrl-N')
    converter_menu.add_command(label="Units of Measurement", command =Units_Converter,accelerator='Ctrl-U')

    #Func Cascade
    func_menu = Menu(menu, tearoff=0)
    function_menu = Menu(func_menu)
    menu.add_cascade(label="Functions", menu=func_menu)
    func_menu.add_command(label="Currency Convert", command= currency_win, accelerator='Ctrl-C')
    # Graphs Window cascade
    func_menu.add_cascade(label="Build Graphs Of Functions", command= graph_build_win,accelerator='Ctrl-G')
    #about program win
    copyright_menu = Menu(menu,tearoff = 0)
    about_prog = Menu(copyright_menu)
    menu.add_cascade(label="About", menu=copyright_menu)
    copyright_menu.add_command(label="About Program", command=about_win, accelerator="F1")

    root.config(menu = menu)





  
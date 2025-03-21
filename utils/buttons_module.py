from tkinter import END
import customtkinter
from utils.calculator_modes import science_frame, basic_frame
from utils.configure import (base_color, base_height, base_width, 
    sci_height, sci_width, button_color, button_color2, button_color3, hover_color
)
from utils.winmain_module import root
from utils.main_functions_module import calculate, show, clear
from utils.math_module import math_func


#Buttons of calculator (splitted by mode of calculator)



def basic_mode():
    #basic mode buttons initialize
    button_clear = customtkinter.CTkButton(basic_frame,text="C",font=("Segoe UI", 20),bg_color=base_color, width=base_width,height=base_height,fg_color="#960300",hover_color=hover_color, command= lambda: clear())
    button_clear.grid(row=0,column=0)
    button_degree = customtkinter.CTkButton(basic_frame,text="x^a",font=("Segoe UI", 20),bg_color=base_color, width=base_width,height=base_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("**"))
    button_degree.grid(row=0,column=1)
    button_division = customtkinter.CTkButton(basic_frame,text="÷",font=("Segoe UI", 20),bg_color=base_color, width=base_width,height=base_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("/"))
    button_division.grid(row=0,column=2)
    button_multiply = customtkinter.CTkButton(basic_frame,text="X",font=("Segoe UI", 20),bg_color=base_color, width=base_width,height=base_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("*"))
    button_multiply.grid(row=0,column=3)

    button_seven = customtkinter.CTkButton(basic_frame,text="7",font=("Segoe UI", 20), width=base_width,height=base_height,bg_color=base_color,fg_color=button_color,hover_color=hover_color, command= lambda: show("7"))
    button_seven.grid(row=1,column=0)
    button_eight = customtkinter.CTkButton(basic_frame,text="8",font=("Segoe UI", 20), width=base_width,height=base_height,bg_color=base_color,fg_color=button_color,hover_color=hover_color, command= lambda: show("8"))
    button_eight.grid(row=1,column=1)
    button_nine = customtkinter.CTkButton(basic_frame,text="9",font=("Segoe UI", 20), width=base_width,height=base_height,fg_color=button_color,bg_color=base_color,hover_color=hover_color, command= lambda: show("9"))
    button_nine.grid(row=1,column=2)
    button_minus = customtkinter.CTkButton(basic_frame,text="-",font=("Segoe UI", 20), width=base_width,height=base_height,fg_color=button_color,bg_color=base_color,hover_color=hover_color, command= lambda: show("-"))
    button_minus.grid(row=1,column=3)

    button_four = customtkinter.CTkButton(basic_frame,text="4",font=("Segoe UI", 20), width=base_width,height=base_height,fg_color=button_color,bg_color=base_color,hover_color=hover_color, command= lambda: show("4"))
    button_four.grid(row=2,column=0)
    button_five = customtkinter.CTkButton(basic_frame,text="5",font=("Segoe UI", 20), width=base_width,height=base_height,fg_color=button_color,bg_color=base_color,hover_color=hover_color, command= lambda: show("5"))
    button_five.grid(row=2,column=1)
    button_six = customtkinter.CTkButton(basic_frame,text="6",font=("Segoe UI", 20), width=base_width,height=base_height,fg_color=button_color,bg_color=base_color,hover_color=hover_color, command= lambda: show("6"))
    button_six.grid(row=2,column=2)
    button_plus = customtkinter.CTkButton(basic_frame,text="+",font=("Segoe UI", 20), width=base_width,height=base_height,fg_color=button_color,bg_color=base_color,hover_color=hover_color, command= lambda: show("+"))
    button_plus.grid(row=2,column=3)

    button_one = customtkinter.CTkButton(basic_frame,text="1",font=("Segoe UI", 20), width=base_width,height=base_height,fg_color=button_color,bg_color=base_color,hover_color=hover_color, command= lambda: show("1"))
    button_one.grid(row=3,column=0)
    button_two = customtkinter.CTkButton(basic_frame,text="2",font=("Segoe UI", 20), width=base_width,height=base_height,fg_color=button_color,bg_color=base_color,hover_color=hover_color, command= lambda: show("2"))
    button_two.grid(row=3,column=1)
    button_three = customtkinter.CTkButton(basic_frame,text="3",font=("Segoe UI", 20), width=base_width,height=base_height,fg_color=button_color,bg_color=base_color,hover_color=hover_color, command= lambda: show("3"))
    button_three.grid(row=3,column=2)
    button_square = customtkinter.CTkButton(basic_frame,text="√x",font=("Segoe UI", 20), width=base_width,height=base_height,fg_color=button_color,hover_color=hover_color,bg_color=base_color, command= lambda: math_func("sqrt"))
    button_square.grid(row=3,column=3)

    button_point = customtkinter.CTkButton(basic_frame,text=".",font=("Segoe UI", 20),bg_color=base_color, width=base_width,height=base_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("."))
    button_point.grid(row=4,column=0)
    button_zero = customtkinter.CTkButton(basic_frame,text="0",font=("Segoe UI", 20),bg_color=base_color, width=base_width,height=base_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("0"))
    button_zero.grid(row=4,column=1)
    button_change_sign = customtkinter.CTkButton(basic_frame,text="±",font=("Segoe UI", 20),bg_color=base_color, width=base_width,height=base_height,fg_color=button_color,hover_color=hover_color, command= lambda: math_func("change_sign"))
    button_change_sign.grid(row=4,column=2)
    button_equal = customtkinter.CTkButton(basic_frame,text="=",font=("Segoe UI", 20),bg_color=base_color, width=base_width,height=base_height,fg_color=button_color3,hover_color=hover_color, command= lambda: calculate())
    button_equal.grid(row=4,column=3)


def scientific_mode():
        
    #buttons for scientific calculator
    button_change_row = customtkinter.CTkButton(science_frame,text="1/x",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: math_func("1/"))
    button_change_row.grid(row=0,column=0)
    button_clear = customtkinter.CTkButton(science_frame,text="C",font=("Segoe UI", 20), width=sci_width,height=sci_height,bg_color=base_color,fg_color="#960300",hover_color=hover_color, command= lambda: clear())
    button_clear.grid(row=0,column=1)
    button_degree = customtkinter.CTkButton(science_frame,text="x^a",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("**"))
    button_degree.grid(row=0,column=2)
    button_division = customtkinter.CTkButton(science_frame,text="÷",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("/"))
    button_division.grid(row=0,column=3)
    button_multiply = customtkinter.CTkButton(science_frame,text="X",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("*"))
    button_multiply.grid(row=0,column=4)
    button_pi =  customtkinter.CTkButton(science_frame,text="π",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("3.141592"))
    button_pi.grid(row=0,column=5)

    button_log = customtkinter.CTkButton(science_frame,text="log10",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: math_func("log10"))
    button_log.grid(row=1, column=0)
    button_seven = customtkinter.CTkButton(science_frame,text="7",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color2,hover_color=hover_color, command= lambda: show("7"))
    button_seven.grid(row=1,column=1)
    button_eight = customtkinter.CTkButton(science_frame,text="8",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color2,hover_color=hover_color, command= lambda: show("8"))
    button_eight.grid(row=1,column=2)
    button_nine = customtkinter.CTkButton(science_frame,text="9",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color2,hover_color=hover_color, command= lambda: show("9"))
    button_nine.grid(row=1,column=3)
    button_minus = customtkinter.CTkButton(science_frame,text="-",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("-"))
    button_minus.grid(row=1,column=4)
    button_sin = customtkinter.CTkButton(science_frame,text="SIN",font=("Segoe UI", 20),bg_color=base_color,width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command=lambda: math_func("sin"))
    button_sin.grid(row=1,column=5)


    button_e = customtkinter.CTkButton(science_frame,text="e",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("2.718281"))
    button_e.grid(row=2, column = 0)
    button_four = customtkinter.CTkButton(science_frame,text="4",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color2,hover_color=hover_color, command= lambda: show("4"))
    button_four.grid(row=2,column=1)
    button_five = customtkinter.CTkButton(science_frame,text="5",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color2,hover_color=hover_color, command= lambda: show("5"))
    button_five.grid(row=2,column=2)
    button_six = customtkinter.CTkButton(science_frame,text="6",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color2,hover_color=hover_color, command= lambda: show("6"))
    button_six.grid(row=2,column=3)
    button_plus = customtkinter.CTkButton(science_frame,text="+",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("+"))
    button_plus.grid(row=2,column=4)
    button_cos = customtkinter.CTkButton(science_frame,text="COS",font=("Segoe UI", 20),bg_color=base_color,width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command=lambda: math_func("cos"))
    button_cos.grid(row=2,column=5)


    button_log_two = customtkinter.CTkButton(science_frame,text="log2",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: math_func("log2"))
    button_log_two.grid(row=3, column=0)
    button_one = customtkinter.CTkButton(science_frame,text="1",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color2,hover_color=hover_color, command= lambda: show("1"))
    button_one.grid(row=3,column=1)
    button_two = customtkinter.CTkButton(science_frame,text="2",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color2,hover_color=hover_color, command= lambda: show("2"))
    button_two.grid(row=3,column=2)
    button_three = customtkinter.CTkButton(science_frame,text="3",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color2,hover_color=hover_color, command= lambda: show("3"))
    button_three.grid(row=3,column=3)
    button_root = customtkinter.CTkButton(science_frame,text="√x",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: math_func("sqrt"))
    button_root.grid(row=3,column=4)
    button_tan = customtkinter.CTkButton(science_frame,text="TAN",font=("Segoe UI", 20),bg_color=base_color,width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command=lambda: math_func("tan"))
    button_tan.grid(row=3,column=5)

    button_factorial = customtkinter.CTkButton(science_frame,text="n!",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: math_func("fac"))
    button_factorial.grid(row=4,column=0)
    button_point = customtkinter.CTkButton(science_frame,text=".",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: show("."))
    button_point.grid(row=4,column=1)
    button_zero = customtkinter.CTkButton(science_frame,text="0",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color2,hover_color=hover_color, command= lambda: show("0"))
    button_zero.grid(row=4,column=2)
    button_change_sign = customtkinter.CTkButton(science_frame,text="±",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: math_func("change_sign"))
    button_change_sign.grid(row=4,column=3)
    button_equal = customtkinter.CTkButton(science_frame,text="=",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color3,hover_color=hover_color, command= lambda: calculate())
    button_equal.grid(row=4,column=4)
    button_three_root = customtkinter.CTkButton(science_frame,text="3√x",font=("Segoe UI", 20),bg_color=base_color,width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command=lambda: math_func("sqrt", "3"))
    button_three_root.grid(row=4,column=5)

    button_log_y = customtkinter.CTkButton(science_frame,text="logy",font=("Segoe UI", 20),bg_color=base_color,width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command=lambda: show("log"))
    button_log_y.grid(row=5,column = 0)
    button_natural_log = customtkinter.CTkButton(science_frame,text="ln",font=("Segoe UI", 20),bg_color=base_color,width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command=lambda: math_func("log"))
    button_natural_log.grid(row=5,column = 1)
    button_abs = customtkinter.CTkButton(science_frame,text="|x|",font=("Segoe UI", 20),bg_color=base_color,width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command=lambda: math_func("fabs"))
    button_abs.grid(row=5,column=2)
    button_closebracket = customtkinter.CTkButton(science_frame,text="(",font=("Segoe UI", 20),bg_color=base_color,width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command=lambda: show("("))
    button_closebracket.grid(row=5,column=3)
    button_bracket = customtkinter.CTkButton(science_frame,text=")",font=("Segoe UI", 20),bg_color=base_color, width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command= lambda: show(")"))
    button_bracket.grid(row=5,column=4)
    button_y_root = customtkinter.CTkButton(science_frame,text="y√x",font=("Segoe UI", 20),bg_color=base_color,width=sci_width,height=sci_height,fg_color=button_color,hover_color=hover_color, command=lambda: show("√"))
    button_y_root.grid(row=5,column=5)

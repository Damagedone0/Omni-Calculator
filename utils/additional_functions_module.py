#library and file imports
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import customtkinter
import customtkinter as ctk
from currency_converter import CurrencyConverter
from customtkinter import CTkToplevel
import webbrowser
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils.configure import icon_img, base_color, button_color, hover_color
from utils.winmain_module import root


#my github page
def author_page():
    webbrowser.open_new("https://github.com/Damagedone0")



#def for graph window
def graph_build_win():
    graph_win = CTkToplevel(root)
    graph_win.title("Graphs Of Function Builder")
    graph_win.geometry("800x385")
    graph_win.resizable(False,False)
    graph_win.config(bg=base_color)
    graph_win.wm_transient(root)
    graph_win.after(201, lambda: graph_win.iconbitmap(icon_img))

    def build_graph():
        entry_input = graph_entry.get()
        if entry_input != "":
            try:

                x, y = sp.symbols('x y')
                func = sp.sympify(entry_input)  # Parse the input function

                if radio_option_var.get() == 1:  # Simple Function (1 variable)
                    # Generate x values
                    x_values = np.linspace(-10, 10, 400)
                    # Evaluate y values for the function
                    y_values = [func.subs(x, val).evalf() for val in x_values]

                    plt.clf()  # Clear previous plots
                    fig, ax = plt.subplots()

                    # Plot the function as a continuous line
                    ax.plot(x_values, y_values, label=f'f(x) = {entry_input}', color="blue")

                    # Set labels and title
                    ax.set_xlabel('X-axis')
                    ax.set_ylabel('Y-axis')
                    ax.set_title('Graph of Function')

                    # Enable grid and legend
                    ax.grid(True)
                    ax.legend()

                elif radio_option_var.get() == 2:  # Function of two variables
                    # Reduce the resolution of the meshgrid to improve performance
                    resolution = 50  # Adjust this value for better performance
                    X = np.linspace(-10, 10, resolution)
                    Y = np.linspace(-10, 10, resolution)
                    X, Y = np.meshgrid(X, Y)

                    # Convert the symbolic function to a numpy-compatible function
                    func_np = sp.lambdify((x, y), func, "numpy")

                    # Evaluate Z values using numpy (vectorized for performance)
                    Z = func_np(X, Y)

                    plt.clf()  # Clear previous plots
                    fig, ax = plt.subplots()

                    # Use contour plot for two-variable functions
                    contour = ax.contourf(X, Y, Z, levels=50, cmap='viridis')  # Filled contour plot
                    plt.colorbar(contour, ax=ax, label='Function Value')  # Color bar to show value scale

                    # Set labels and title
                    ax.set_xlabel('X-axis')
                    ax.set_ylabel('Y-axis')
                    ax.set_title(f'Graph of f(x,y) = {entry_input}')

                    ax.grid(True)  # Enable grid on the subplot
                elif radio_option_var.get() == 3:  # Logarithmic Graph
                    # Generate x values (avoid log(0) by starting from a small positive number)
                    x_values = np.linspace(0.1, 10, 400)
                    # Evaluate y values for the function
                    y_values = [func.subs(x, val).evalf() for val in x_values]

                    plt.clf()  # Clear previous plots
                    fig, ax = plt.subplots()

                    # Plot the function with logarithmic scaling
                    ax.plot(x_values, y_values, label=f'f(x) = {entry_input}', color="blue")

                    # Set logarithmic scaling for x-axis, y-axis, or both
                    ax.set_xscale('log')  # Logarithmic x-axis
                    ax.set_yscale('log')  # Logarithmic y-axis

                    # Set labels and title
                    ax.set_xlabel('X-axis (log scale)')
                    ax.set_ylabel('Y-axis (log scale)')
                    ax.set_title('Logarithmic Graph of Function')

                    # Enable grid and legend
                    ax.grid(True, which="both", linestyle='--')  # Grid for logarithmic scale
                    ax.legend()

                # Draw on canvas
                graph_canvas.figure.clear()  # Clear previous figure
                graph_canvas.figure = fig  # Set the new figure
                graph_canvas.draw()  # Update the canvas with new data

            except Exception as e:
                # Stop and hide the progress bar if an error occurs
                messagebox.showerror("Error", f"Invalid input: {e}")

    def help_syn():
        messagebox.showinfo("Help Syntax","\nUSE X,Y AS UNKNOWNS \n\n x^2(or y) → ** \n\ndivision → / \n\nmultiply →  * \n\n")



    # button for syntax writing
    help_button = customtkinter.CTkButton(graph_win, width=250,height= 20,font=("Segoe UI", 10), text="Reference For Correct Syntax Of Functions", fg_color="#60c94b", bg_color=base_color, text_color="#000000",hover_color=hover_color, command= help_syn)
    help_button.place(x=25 ,y=20)

    # entry for graph
    entry_placeholder = "Entry Function..."
    graph_entry = customtkinter.CTkEntry(graph_win, width=200,font=("Segoe UI", 15), justify = "center", bg_color=base_color)
    graph_entry.insert(0,entry_placeholder)
    graph_entry.place(x=45,y=50)

    #Clear Insert of entry
    def clear_placeholder(event):
        if graph_entry.get() == entry_placeholder:
            graph_entry.delete(0, 'end')  # Clear the entry

    graph_entry.bind("<FocusIn>", clear_placeholder)


    #button for build
    graph_build_button = customtkinter.CTkButton(graph_win,font=("Segoe UI", 15), width=150,height=20,text="Build Graph Of Input Function",bg_color=base_color,fg_color=button_color,hover_color=hover_color,command=build_graph)
    graph_build_button.place(x=40,y= 100)

    #options
    radio_option_var = customtkinter.IntVar(value=0)

    one_radio_button = customtkinter.CTkRadioButton(graph_win,font=("Segoe UI", 15),text="Simple (1 Variable) Function", variable= radio_option_var,value=1)
    one_radio_button.place(x=50,y=150)
    sec_radio_button = customtkinter.CTkRadioButton(graph_win,font=("Segoe UI", 15),text="2 Variable Function", variable= radio_option_var,value=2)
    sec_radio_button.place(x=50,y=175)
    thrd_radio_button = customtkinter.CTkRadioButton(graph_win,font=("Segoe UI", 15),text="Logarithmic Function", variable= radio_option_var,value=3)
    thrd_radio_button.place(x=50,y=200)

    #frame for Graph canvas
    graph_frame = customtkinter.CTkFrame(graph_win, width=500,height=500)
    graph_frame.place(x=300,y=0)

    #graph canvas converts to tkinter
    graph_canvas = FigureCanvasTkAgg(master=graph_frame)
    graph_canvas.draw()
    graph_canvas.get_tk_widget().pack( fill=tk.BOTH, expand=True)
    graph_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)



#Convert Number in four main system of numbers
def translator_window():
    # new window settings
    translator_win = CTkToplevel(root)
    translator_win.title("Converter NS")
    translator_win.geometry("250x250")
    translator_win.resizable(False, False)
    translator_win.after(201, lambda : translator_win.iconbitmap(icon_img))
    translator_win.wm_transient(root)
    translator_win.config(bg=base_color)

    
    

    #widgets
    entry_text_NS = "Enter Number..."

    e_one = customtkinter.CTkEntry(translator_win,bg_color=base_color,font=("Segoe UI", 12), width=100, height=30, justify="center")
    e_one.insert(0, entry_text_NS)

    # Function to clear the entry when focused
    def clear_placeholder(event):
        if e_one.get() == entry_text_NS:
            e_one.delete(0, 'end')  # Clear the entry

    # Bind the focus in event to clear placeholder
    e_one.bind("<FocusIn>", clear_placeholder)

    e_one.pack(padx=10,pady=10)



    input_base_list = ["Binary", "Decimal","Octon", "Hexadecimal"]
    input_base = StringVar(translator_win)
    input_base.set(input_base_list[0])

    base_menu = customtkinter.CTkOptionMenu(translator_win,font=("Segoe UI", 15), variable=input_base, values= input_base_list, bg_color=base_color,fg_color=hover_color , button_hover_color=base_color, dropdown_hover_color=base_color, button_color=button_color)
    base_menu.pack(pady=10)

    # Function
    def NStranslate():
        input_value = e_one.get()
        base = input_base.get()
        results = {}
        try:
            if base == "Binary":
                decimal_value = int(input_value, 2)
            elif base == "Decimal":
                decimal_value = int(input_value)
            elif base == "Octon":
                decimal_value = int(input_value, 8)
            elif base == "Hexadecimal":
                decimal_value = int(input_value, 16)
            else:
                raise ValueError("Invalid Base Number System Selected.")

            # Store results in various Bases
            results["Binary"] = bin(decimal_value)[2:]
            results["Decimal"] = decimal_value
            results["Octon"] = oct(decimal_value)[2:]
            results["Hexadecimal"] = hex(decimal_value)[2:].upper()

            # display results
            result_message = "\n".join([f"{key}: {value}" for key, value in results.items()])
            messagebox.showinfo("Conversion Results", result_message)

        except ValueError:
            messagebox.showerror("Input Error", "Invalid Number Format")
    #Help Function
    def Help():
        messagebox.showinfo("Help","Write a number and choose a system so\n that it can be converted into other systems")

    help_button = customtkinter.CTkButton(translator_win,command=Help,bg_color=base_color,font=("Segoe UI", 10), text="Help", width=100, height=30, fg_color=button_color,hover_color=hover_color)
    help_button.pack()
    #Button for Function
    translate_button= customtkinter.CTkButton(translator_win,bg_color=base_color,font=("Segoe UI", 10), text="Convert!", command= NStranslate, width=100, height=30, fg_color=button_color,hover_color=hover_color)
    translate_button.pack(pady=10,padx=50)


#Currency converter
def currency_win():
    cur_win = CTkToplevel(root)
    cur_win.title("Currency Converter")
    cur_win.geometry("200x300")
    cur_win.wm_transient(root)
    cur_win.resizable(False,False)
    cur_win.config(bg=base_color)
    cur_win.after(201, lambda: cur_win.iconbitmap(icon_img))

    def convert_currency():
        input_entry = input_cur.get()
        select = input_base.get()
        res_select = output_base.get()
        converter = CurrencyConverter()
        result = 0
        try:
            input_entry = float(input_entry)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
            return
        #Dollar
        if select == "$ - USD" and res_select == "€ - EUR":
            result = str(converter.convert(int(input_entry), 'USD', 'EUR'))
        elif select == "$ - USD" and res_select == "¥ - JPY":
            result = str(converter.convert(int(input_entry), 'USD', 'JPY'))
        elif select == "$ - USD" and res_select == "£ - GBP":
            result = str(converter.convert(int(input_entry), 'USD', 'GBP'))
        elif select == "$ - USD" and res_select == "¥ - CNY":
            result = str(converter.convert(int(input_entry), 'USD', 'CNY'))
        #Euro
        elif select == "€ - EUR" and res_select == "$ - USD":
            result = str(converter.convert(int(input_entry), 'EUR', 'USD'))
        elif select == "€ - EUR" and res_select == "¥ - JPY":
            result = str(converter.convert(int(input_entry), 'EUR', 'JPY'))
        elif select == "€ - EUR" and res_select == "£ - GBP":
            result = str(converter.convert(int(input_entry), 'EUR', 'GBP'))
        elif select == "€ - EUR" and res_select == "¥ - CNY":
            result = str(converter.convert(int(input_entry), 'EUR', 'CNY'))
        #Japanese Yen
        elif select == "¥ - JPY" and res_select == "$ - USD":
            result = str(converter.convert(int(input_entry), 'JPY', 'USD'))
        elif select == "¥ - JPY" and res_select == "€ - EUR":
            result = str(converter.convert(int(input_entry), 'JPY', 'EUR'))
        elif select == "¥ - JPY" and res_select == "£ - GBP":
            result = str(converter.convert(int(input_entry), 'JPY', 'GBP'))
        elif select == "¥ - JPY" and res_select == "¥ - CNY":
            result = str(converter.convert(int(input_entry), 'JPY', 'CNY'))
        #Chinese Yen
        elif select == "¥ - CNY" and res_select == "$ - USD":
            result = str(converter.convert(int(input_entry), 'CNY', 'USD'))
        elif select == "¥ - CNY" and res_select == "€ - EUR":
            result = str(converter.convert(int(input_entry), 'CNY', 'EUR'))
        elif select == "¥ - CNY" and res_select == "£ - GBP":
            result = str(converter.convert(int(input_entry), 'CNY', 'GBP'))
        elif select == "¥ - CNY" and res_select == "¥ - JPY":
            result = str(converter.convert(int(input_entry), 'CNY', 'JPY'))
        #Pound sterling
        elif select == "£ - GBP" and res_select == "$ - USD":
            result = str(converter.convert(int(input_entry), 'GBP', 'USD'))
        elif select == "£ - GBP" and res_select == "€ - EUR":
            result = str(converter.convert(int(input_entry), 'GBP', 'EUR'))
        elif select == "£ - GBP" and res_select == "¥ - CNY":
            result = str(converter.convert(int(input_entry), 'GBP', 'CNY'))
        elif select == "£ - GBP" and res_select == "¥ - JPY":
            result = str(converter.convert(int(input_entry), 'GBP', 'JPY'))
        
        #if the same currency selected in both options
        elif select == res_select:
            result = input_entry

        output_cur.configure(state="normal")
        output_cur.delete(0, 'end')
        output_cur.insert(0, str(result))
        output_cur.configure(state="disabled")




    list_cur = ["$ - USD", "¥ - JPY", "€ - EUR", "£ - GBP", "¥ - CNY"]
    input_base = StringVar(cur_win)
    input_base.set(list_cur[0])
    output_base = StringVar(cur_win)
    output_base.set(list_cur[2])

    option_input = customtkinter.CTkOptionMenu(cur_win, values=list_cur, variable=input_base, font=("Segoe UI", 30),bg_color=base_color,fg_color=hover_color , button_hover_color=base_color, dropdown_hover_color=base_color, button_color=button_color)
    option_input.place(x=30, y=0)

    option_output = customtkinter.CTkOptionMenu(cur_win, values=list_cur, variable=output_base,font=("Segoe UI", 30),bg_color=base_color,fg_color=hover_color , button_hover_color=base_color, dropdown_hover_color=base_color, button_color=button_color)
    option_output.place(x=30, y=125)

    input_cur = customtkinter.CTkEntry(cur_win,width=150, height=30,font=("Segoe UI", 30), justify = "center", bg_color=base_color,fg_color=base_color)
    input_cur.place(x=25,y=50)



    output_cur = customtkinter.CTkEntry(cur_win, width=150, height=30, font=("Segoe UI", 30), justify="center", bg_color=base_color,fg_color=base_color, state="disabled")
    output_cur.place(x=25, y=170)

    convert_button = customtkinter.CTkButton(cur_win, width= 50, height=40, font=("Segoe UI", 30), text="Convert",fg_color="#960303",bg_color=base_color,hover_color=hover_color, command=convert_currency)
    convert_button.place(x=40,y=240)

#Units of measurement converter

def Units_Converter():
    units_win = CTkToplevel(root)
    units_win.title("units of measurement")
    units_win.geometry("500x300")
    units_win.config(bg=base_color)
    units_win.resizable(False, False)
    units_win.wm_transient(root)
    units_win.after(201, lambda : units_win.iconbitmap(icon_img))

    def convert_unit():
        input_value = input_entry.get()
        try:
            input_value = float(input_value)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
            return

        select = input_base.get()
        res_select = output_base.get()
        result_value = 0


        #for some reason * and / are work reversed (multiply is division and division is multiply)
        # Speed conversions
        if select == "Km/H" and res_select == "M/Sec":
            result_value = input_value * 3.6  # Km/H to M/Sec
        elif select == "M/Sec" and res_select == "Km/H":
            result_value = input_value / 3.6  # M/Sec to Km/H

        # Mass conversions
        elif select == "Kg" and res_select == "Gr":
            result_value = input_value / 1000  # Kg to Gr
        elif select == "Gr" and res_select == "Kg":
            result_value = input_value * 1000  # Gr to Kg

        # Volume/Length conversions
        elif select == "L" and res_select == "Ml":
            result_value = input_value / 1000  # L to Ml
        elif select == "Ml" and res_select == "L":
            result_value = input_value * 1000  # Ml to L
        elif select == "Km" and res_select == "M":
            result_value = input_value / 1000  # Km to M
        elif select == "M" and res_select == "Km":
            result_value = input_value * 1000  # M to Km
        elif select == "Sm" and res_select == "M":
            result_value = input_value * 100
        elif select == "M" and res_select == "Sm":
            result_value = input_value / 100
        elif select == "Sm" and res_select == "Km":
            result_value = input_value * 100000
        elif select == "Km" and res_select == "Sm":
            result_value = input_value / 100000

        # Inches conversions
        elif select == "Inches" and res_select == "Sm":
            result_value = input_value / 2.54  # Inches to Cm
        elif select == "Sm" and res_select == "Inches":
            result_value = input_value * 2.54  # Cm to Inches
        elif select == "Inches" and res_select == "M":
            result_value = input_value / 0.0254  # Inches to M
        elif select == "M" and res_select == "Inches":
            result_value = input_value * 0.0254  # M to Inches

        # Square metres conversions
        elif select == "M^2" and res_select == "Km^2":
            result_value = input_value * 1_000_000  # M^2 to Km^2
        elif select == "Km^2" and res_select == "M^2":
            result_value = input_value / 1_000_000  # Km^2 to M^2

        # Cubic metres conversions
        elif select == "M^3" and res_select == "Km^3":
            result_value = input_value * 1_000_000_000  # M^3 to Km^3
        elif select == "Km^3" and res_select == "M^3":
            result_value = input_value / 1_000_000_000  # Km^3 to M^3


        # Same unit conversion
        elif select == res_select:
            result_value = input_value

        # Display the result
        result_entry.configure(state="normal")
        result_entry.delete(0, 'end')
        result_entry.insert(0, str(result_value))
        result_entry.configure(state="disabled")


    input_text = "Input Unit"

    input_entry = customtkinter.CTkEntry(units_win, width=150,font=("Segoe UI", 20), justify="center",bg_color=base_color)
    input_entry.place(x=50, y=100)

    result = "Result Unit"

    result_entry = customtkinter.CTkEntry(units_win, width=150,font=("Segoe UI", 20), state="disabled",bg_color=base_color, justify= "center")
    result_entry.place(x=300, y=100)

    input_list = ["Km/H", "M/Sec", "Kg", "Gr", "L", "Ml", "M^2","M^3","Km^2","Km^3", "Km", "M", "Sm","Inches"]
    input_base = StringVar(units_win)
    input_base.set(input_list[0])

    output_list = ["Km/H", "M/Sec", "Kg", "Gr", "L", "Ml", "M^2", "M^3","Km^2","Km^3", "Km", "M","Sm","Inches"]
    output_base = StringVar(units_win)
    output_base.set(input_list[0])

    under_one_label = customtkinter.CTkLabel(units_win, width=100,font=("Segoe UI", 15), height=20, text=input_text, bg_color=base_color)
    under_one_label.place(x=60, y=150)
    under_two_label = customtkinter.CTkLabel(units_win, width=100,font=("Segoe UI", 15), height=20, text=result,bg_color=base_color)
    under_two_label.place(x=340, y=150)

    output_base = customtkinter.CTkOptionMenu(units_win, variable= output_base,font=("Segoe UI", 20), values=output_list, bg_color=base_color,fg_color=hover_color , button_hover_color=base_color, dropdown_hover_color=base_color, button_color=button_color)
    output_base.place(y=10, x=50)

    input_base = customtkinter.CTkOptionMenu(units_win, variable= input_base,font=("Segoe UI", 20), values=input_list, bg_color=base_color,fg_color=hover_color , button_hover_color=base_color, dropdown_hover_color=base_color, button_color=button_color)
    input_base.place(x=300, y=10)

    text_label = customtkinter.CTkLabel(units_win, text="Choose Unit of Measurement To Convert",font=("Segoe UI", 20), width=100, height=10,bg_color=base_color)
    text_label.pack(pady=50)

    button = customtkinter.CTkButton(units_win, text="Convert",font=("Segoe UI", 20), height=5, width=10, fg_color="#32a852",hover_color="#0c5e22", command=convert_unit)
    button.place(x=215, y=200)

#window about program license and copyright

def about_win():
    about_window = CTkToplevel(root)
    about_window.title("Program intelligence")
    about_window.geometry("500x500")
    about_window.resizable(0,0)
    about_window.config(bg=base_color)
    about_window.wm_transient(root)
    about_window.after(201, lambda: about_window.iconbitmap(icon_img))
    logo_img = "logo.png"
    image = Image.open(logo_img)

    license_text= (
        "Copyright (c) 2025 Dmg717 \n\n Software: OmniCalc\nVersion: 1.0\n\n"
        "MIT License\n\n"
        "Permission is hereby granted, free of charge, to any person to use,\n copy, modify, merge, publish, distribute, sublicense,\n and/or sell copies of the software, subject to the following conditions:\n\n"
        "1. The above copyright notice and this permission notice\n must be included in all copies or substantial portions of the software.\n\n"
        "2. THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND."
    )
    image_wid = customtkinter.CTkImage(dark_image=image, light_image=image, size=(200,200))
    img_label = customtkinter.CTkLabel(about_window, bg_color=base_color, text="", image=image_wid)
    img_label.pack()
    about_label = customtkinter.CTkLabel(about_window, text=license_text, font=("Segoe UI", 12), bg_color=base_color)
    about_label.pack()

    close_button = customtkinter.CTkButton(about_window,width=100,height=15, text="Ok",font=("Segoe UI", 15), text_color="#000000", bg_color=base_color, hover_color=hover_color, fg_color="#960300", command=about_window.destroy)
    close_button.place(x=390, y=465)

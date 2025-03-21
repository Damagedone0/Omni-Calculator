import customtkinter
from utils.winmain_module import root
from utils.configure import base_color



#frame for basic mode of calculator
basic_frame = customtkinter.CTkFrame(root, width=570, height=550,bg_color=base_color)
basic_frame.pack(expand=True)

#frame for scientific mode of calculator
science_frame = customtkinter.CTkFrame(root, width=570, height=550,bg_color=base_color)
science_frame.pack(expand=True)


# Function to set calculator mode
def set_calculator_mode(mode="basic"):
    global equation
    equation = ""
    if mode == "basic":
        science_frame.pack_forget()
        basic_frame.pack(expand=True)
    elif mode == "scientific":
        basic_frame.pack_forget()
        science_frame.pack(expand=True)
set_calculator_mode()



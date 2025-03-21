import customtkinter as ctk
import customtkinter
from utils.configure import base_color


## Config of Calculator main window
root = ctk.CTk() #create main window
root.title("Omni Calculator")  # Program Title
customtkinter.set_appearance_mode("Dark") #CTK color theme
customtkinter.set_default_color_theme("dark-blue")
root.geometry("410x455")  # Program Size
root.resizable(False, False)  # Resizeable Function (False in standard)
root.iconbitmap("icon.ico") #Icon for program
root.config(bg=base_color) # Background color



equation = ""

# Create an Entry widget for displaying the expression
entry_result = customtkinter.CTkEntry(root, width=397,height=60,bg_color=base_color, font=("Segoe UI", 30), justify='center',text_color="white", fg_color="#282828")
entry_result.pack(pady=10)


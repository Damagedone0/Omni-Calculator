import customtkinter
import customtkinter as ctk
from utils.configure import base_color,hover_color
from utils.winmain_module import root
from utils.shared_history import clear_history, get_history



#History Journal Code

history_textbox = None  # Declare history_textbox as a global variable

# Function to update history table
def update_history():
    global history_textbox
    if history_textbox is not None:  # Check if history_textbox is initialized
        history_textbox.configure(state="normal")  # Enable editing
        history_textbox.delete("1.0", "end")  # Clear the textbox

        # Insert each calculation from the history list into the textbox
        for calc in get_history():
            history_textbox.insert("end", calc + "\n")

        history_textbox.configure(state="disabled")  # Disable editing




#GUI func to see history
def history_page():
    global history_textbox  # Access the global history_textbox

    def hide_frame():
        history_frame.place_forget()

    def on_clear_history():
        clear_history()  # Clear the history list
        update_history()


    # Main body - frame
    history_frame = customtkinter.CTkFrame(root, width=410, height=410)
    history_frame.place(x=0, y=80)

    # Label
    history_label = customtkinter.CTkLabel(history_frame, text="History", font=("Segoe UI", 20))
    history_label.pack()

    # Textbox for history
    history_textbox = customtkinter.CTkTextbox(history_frame, width=410, height=410, state="disabled", font=("Segoe UI", 30))
    history_textbox.pack(fill="both", expand=True, pady=10)

    # Close button
    close_button = customtkinter.CTkButton(history_frame, height=30, width=30, font=("Segoe UI", 15), text="X", text_color="#960300", bg_color=base_color, hover_color=hover_color, fg_color=base_color, command=hide_frame)
    close_button.place(x=380, y=0)

    # Clear history button
    clear_history_button = customtkinter.CTkButton(history_frame, height=30, width=30, font=("Segoe UI", 15), text="🗑", text_color="#960300", bg_color=base_color, hover_color=hover_color, fg_color=base_color, command=on_clear_history)
    clear_history_button.place(x=350, y=0)


    # Update the history textbox after it's initialized
    update_history()

    return history_frame


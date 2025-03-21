# list where program saves calculations
history = []

#function to make a strings with solutions and add it in update func
def add_calculation(calculation):
    """
    Add a calculation to the history list.
    """
    global history
    history.append(calculation)

#function to get a list in any other file
def get_history():
    """
    Get the current history list.
    """
    global history
    return history

#function to clear story when button is pressed
def clear_history():

    """
    Clear the history list.
    """
    global history 
    history = []  # Clear the history list
    
    
    
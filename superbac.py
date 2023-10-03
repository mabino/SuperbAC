import tkinter as tk

# Function to start or stop the AC
def start_stop_ac():
    # Implement the logic to start or stop the AC here
    pass

# Function to toggle the "floating" behavior of the window
def toggle_floating():
    if float_var.get():
        root.attributes("-topmost", True)
    else:
        root.attributes("-topmost", False)

# Function to capture the next keypress
def capture_key(event):
    key_pressed = event.keysym
    key_capture_entry.delete(0, tk.END)  # Clear the current entry
    key_capture_entry.insert(0, key_pressed)  # Display the captured key

# Function to clear the key assignment field
def clear_key_field():
    key_capture_entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Superb AC")

# Set the minimum size for the window
root.minsize(360, 270)

# Create a label widget with the "Superb AC" message
label = tk.Label(root, text="Superb AC")
label.pack(padx=20, pady=20)  # Add some padding around the label

# Create a button widget labeled "Start/Stop"
start_stop_button = tk.Button(root, text="Start/Stop", command=start_stop_ac)
start_stop_button.pack()

# Create a Checkbutton for "Floating Window"
float_var = tk.IntVar()
float_checkbox = tk.Checkbutton(root, text="Floating Window", variable=float_var, command=toggle_floating)
float_checkbox.pack()

# Create an Entry widget to capture and display the pressed key
key_capture_label = tk.Label(root, text="Assign a Key")
key_capture_label.pack()
key_capture_entry = tk.Entry(root)
key_capture_entry.pack()
key_capture_entry.bind("<KeyPress>", capture_key)  # Bind the event handler to keypress events

# Create a button widget labeled "Clear"
clear_button = tk.Button(root, text="Clear Assigned Key", command=clear_key_field)
clear_button.pack()

# Start the tkinter main loop
root.mainloop()

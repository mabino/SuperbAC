import tkinter as tk
import threading
import time
import pyautogui
import keyboard  # Import the keyboard library
import os, sys

app_name = "Superb AC"
app_window_size = "320x160"
selected_hotkey = 'F7'
start_msg = f"Start Clicks ({selected_hotkey})"
stop_msg = f"Stop Clicks ({selected_hotkey})"
mouse_x, mouse_y = 200, 200

# Default click interval in milliseconds
default_click_interval = 1000

def set_icon():
    try:
        if getattr(sys, 'frozen', False):  # Check if the script is frozen (i.e., packaged)
            base_path = sys._MEIPASS  # Get the base path of the packaged application
        else:
            base_path = os.path.abspath(".")  # Use the current directory if not packaged
        icon_path = os.path.join(base_path, "superbac.ico")
        root.iconbitmap(icon_path)
    except Exception as e:
        print(f"Error setting icon: {e}")



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def background_task():
    global is_running, mouse_x, mouse_y
    while is_running:
        pyautogui.click(mouse_x, mouse_y)
        time.sleep(click_interval / 1000)  # Convert to seconds
        mouse_x, mouse_y = pyautogui.position()

def toggle_floating():
    if float_var.get():
        root.attributes("-topmost", True)
    else:
        root.attributes("-topmost", False)

def toggle_thread(event=None):
    global is_running
    if is_running:
        is_running = False
        stop_button.config(text=start_msg)
        # Make the Click Interval field interactive when not running
        click_interval_entry.config(state="normal")
    else:
        is_running = True
        stop_button.config(text=stop_msg)
        # Make the Click Interval field read-only when running
        click_interval_entry.config(state="disabled")
        thread = threading.Thread(target=background_task)
        thread.start()

def on_closing():
    global is_running
    is_running = False
    root.destroy()

# Function to validate and update the click interval
def update_click_interval():
    try:
        value = int(click_interval_entry.get())
        if 0 < value <= 9999:
            global click_interval
            click_interval = value
        else:
            click_interval_entry.delete(0, tk.END)  # Clear the entry if invalid
            click_interval_entry.insert(0, str(click_interval))
    except ValueError:
        # Handle non-integer input
        click_interval_entry.delete(0, tk.END)
        click_interval_entry.insert(0, str(click_interval))

is_running = False
click_interval = default_click_interval  # Initialize with default value

root = tk.Tk()
root.title(app_name)
root.attributes("-topmost", True)
# Call set_icon to set the application icon
set_icon()
# Center the Tkinter window on the primary display
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Create a Frame to contain the Start/Stop button
button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=10)

stop_button = tk.Button(button_frame, text=start_msg, command=toggle_thread)
stop_button.pack()

# Create the "Floating Window" checkbox
float_var = tk.IntVar(value=1)
float_checkbox = tk.Checkbutton(root, text="Floating Window", variable=float_var, command=toggle_floating)
float_checkbox.place(relx=.95, rely=.95, anchor=tk.SE)

# Create the "Click Interval (ms)" label and entry field
click_interval_label = tk.Label(root, text="Click Interval (ms):")
click_interval_label.place(x=10, y=10)  # Position in the top left corner

click_interval_entry = tk.Entry(root, validate="key", validatecommand=update_click_interval)
click_interval_entry.insert(0, str(default_click_interval))  # Set default value
click_interval_entry.place(x=10, y=30)  # Position below the label

# Define a function to stop the background task
def stop_background_task():
    global is_running
    is_running = False
    stop_button.config(text=start_msg)
    # Make the Click Interval field interactive when not running
    click_interval_entry.config(state="normal")

# Bind the F7 key to stop the background task
keyboard.add_hotkey(selected_hotkey, toggle_thread)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.geometry(app_window_size)
# Center the Tkinter window on the primary display
center_window(root)
root.mainloop()

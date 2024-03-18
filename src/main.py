from utils import *
from style import *
from menu import create_input_amount_of_points

# Create tkinter Window
root = tk.Tk()
root.title("Bezier Curve Builder")

# Close Tkinter Window
def quit_window() -> None:
    root.quit() 
    root.destroy()

# Window Size and Position
window_width = 400
window_height = 240
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

entry_amount_of_points = create_input_amount_of_points(root)

# Bind the window close event to the quit function
root.protocol("WM_DELETE_WINDOW", quit_window)

# Start main loop
root.mainloop()

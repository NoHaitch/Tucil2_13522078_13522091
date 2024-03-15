from util import *
from chart import generate_chart
from menu import create_input_menu

def build_bezier_curve(entry_point0_x, entry_point0_y, entry_point1_x, entry_point1_y,
                       entry_point2_x, entry_point2_y, entry_iteration):
    # Retrieve input values
    point0_x = float(entry_point0_x.get())
    point0_y = float(entry_point0_y.get())
    point1_x = float(entry_point1_x.get())
    point1_y = float(entry_point1_y.get())
    point2_x = float(entry_point2_x.get())
    point2_y = float(entry_point2_y.get())
    iteration = int(entry_iteration.get())
    
    # Store the points
    points : list[Point] = [(point0_x, point0_y), (point1_x, point1_y), (point2_x, point2_y)]

    # Build your Bezier curve here using the input values
    print("Bezier curve built with the following points:")
    print(f"Point 0: ({point0_x}, {point0_y})")
    print(f"Point 1: ({point1_x}, {point1_y})")
    print(f"Point 2: ({point2_x}, {point2_y})")
    print(f"Iteration: {iteration}")

    # Generate line chart
    generate_chart(points)

def quit_window():
    root.quit()  # Stops the main loop
    root.destroy()  # Closes the Tkinter window

# Create main window
root = tk.Tk()
root.title("Bezier Curve Builder")

# Window Size 
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

# ========== Window Content ==========

font_family = "Courier New"

# Create input menu
entry_point0_x, entry_point0_y, entry_point1_x, entry_point1_y, entry_point2_x, entry_point2_y, entry_iteration = create_input_menu(root, build_bezier_curve, quit_window, font_family)

# Button to build Bezier curve
build_button = tk.Button(root, text="Build Bezier Curve", command=lambda: build_bezier_curve(entry_point0_x, entry_point0_y, entry_point1_x, entry_point1_y, entry_point2_x, entry_point2_y, entry_iteration), font=(font_family, 16, "bold"))
build_button.pack(pady=10)

# Add a quit button
quit_button = tk.Button(master=root, text="Quit", command=quit_window, font=(font_family, 14))
quit_button.pack(side=tk.BOTTOM)

# Bind the window close event to the quit function
root.protocol("WM_DELETE_WINDOW", quit_window)

# Start main loop
root.mainloop()

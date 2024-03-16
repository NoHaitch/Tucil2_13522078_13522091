from utils import *
from style import *
from chart import generate_chart
from menu import create_input_menu
from bfBezier import bfBezier
from dcBezier import dcBezier

def build_bezier_curve(points, iteration, use_divide_conquer):
    # Print input points for debugging
    print("Input points:", points)
    print("Iteration:", iteration)

    # Validate if the iteration is not empty
    if iteration == '':
        tk.messagebox.showerror("Error", "Please enter the iteration value.")
        return

    # Validate if any of the entry points are empty
    for point in points:
        if '' in point:
            tk.messagebox.showerror("Error", "Please enter both x and y coordinates for all points.")
            return

    # Convert points to Point objects
    control_points = [Point(float(x), float(y)) for x, y in points]

    if use_divide_conquer:
        pass
        # Use Divide Conquer algorithm
        bf_bezier_points = dcBezier(control_points[0], control_points[1], control_points[2], int(iteration))
    else:
        # Use Brute Force algorithm
        bf_bezier_points = bfBezier(control_points[0], control_points[1], control_points[2], int(iteration))

    # Build your Bezier curve here using the input values
    print("Bezier curve built with the following points:")
    print(f"Iteration: {iteration}")
    for i, point in enumerate(control_points):
        print(f"Control Points {i}: ({point.x}, {point.y})")
    for i, point in enumerate(bf_bezier_points):
        print(f"Bezier Points {i}: ({point.x}, {point.y})")

    # Generate line chart
    generate_chart(control_points, bf_bezier_points)

def quit_window():
    root.quit()  # Stops the main loop
    root.destroy()  # Closes the Tkinter window

# Create main window
root = tk.Tk()
root.title("Bezier Curve Builder")

# Window Size 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

# ========== Window Content ==========

# Create input menu
entry_iteration, get_points = create_input_menu(root)

# Label above the buttons
label = tk.Label(root, text="Choose Algorithm:", font=(font_family, font_size_normal))
label.pack(pady=10)

# Frame to hold buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Brute Force button
bf_button = tk.Button(button_frame, text="Brute Force", command=lambda: build_bezier_curve(get_points(), entry_iteration.get(), False), font=(font_family, font_size_normal, "bold"))
bf_button.grid(row=0, column=0, padx=5)

# Divide Conquer button
dc_button = tk.Button(button_frame, text="Divide Conquer", command=lambda: build_bezier_curve(get_points(), entry_iteration.get(), True), font=(font_family, font_size_normal, "bold"))
dc_button.grid(row=0, column=1, padx=5)

# Add a quit button
quit_button = tk.Button(master=root, text="Quit", command=quit_window, font=(font_family, font_size_normal))
quit_button.pack(side=tk.BOTTOM)

# Bind the window close event to the quit function
root.protocol("WM_DELETE_WINDOW", quit_window)

# Start main loop
root.mainloop()

import tkinter as tk

def build_bezier_curve():
    # Retrieve input values
    point0_x = float(entry_point0_x.get())
    point0_y = float(entry_point0_y.get())
    point1_x = float(entry_point1_x.get())
    point1_y = float(entry_point1_y.get())
    point2_x = float(entry_point2_x.get())
    point2_y = float(entry_point2_y.get())
    iteration = int(entry_iteration.get())
    
    # Build your Bezier curve here using the input values
    print("Bezier curve built with the following points:")
    print(f"Point 0: ({point0_x}, {point0_y})")
    print(f"Point 1: ({point1_x}, {point1_y})")
    print(f"Point 2: ({point2_x}, {point2_y})")
    print(f"Iteration: {iteration}")

# ========== Window initialization ==========

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

# Title
title_label = tk.Label(root, text="Bezier Curve Builder", font=(font_family, 20, "bold"))
title_label.pack(pady=10)

# Sub-title
subtitle_label = tk.Label(root, text="made by Sean and Francisco", font=(font_family, 14))
subtitle_label.pack()

# Point Inputs
point_frame = tk.Frame(root)
point_frame.pack(pady=10)

point0_label = tk.Label(point_frame, text="Point 0:", font=(font_family, 14))
point0_label.grid(row=0, column=0, padx=5, pady=2, sticky="e")
entry_point0_x = tk.Entry(point_frame, width=5, font=(font_family, 14))
entry_point0_x.grid(row=0, column=1, padx=5, pady=2)
entry_point0_y = tk.Entry(point_frame, width=5, font=(font_family, 14))
entry_point0_y.grid(row=0, column=2, padx=5, pady=2)

point1_label = tk.Label(point_frame, text="Point 1:", font=(font_family, 14))
point1_label.grid(row=1, column=0, padx=5, pady=2, sticky="e")
entry_point1_x = tk.Entry(point_frame, width=5, font=(font_family, 14))
entry_point1_x.grid(row=1, column=1, padx=5, pady=2)
entry_point1_y = tk.Entry(point_frame, width=5, font=(font_family, 14))
entry_point1_y.grid(row=1, column=2, padx=5, pady=2)

point2_label = tk.Label(point_frame, text="Point 2:", font=(font_family, 14))
point2_label.grid(row=2, column=0, padx=5, pady=2, sticky="e")
entry_point2_x = tk.Entry(point_frame, width=5, font=(font_family, 14))
entry_point2_x.grid(row=2, column=1, padx=5, pady=2)
entry_point2_y = tk.Entry(point_frame, width=5, font=(font_family, 14))
entry_point2_y.grid(row=2, column=2, padx=5, pady=2)

# Iteration Input
iteration_label = tk.Label(root, text="Iteration (>= 1):", font=(font_family, 14))
iteration_label.pack()

entry_iteration = tk.Entry(root, width=10, font=(font_family, 14))
entry_iteration.pack()

# Button to build Bezier curve
build_button = tk.Button(root, text="Build Bezier Curve", command=build_bezier_curve, font=(font_family, 16, "bold"))
build_button.pack(pady=10)

# Start main loop
root.mainloop()

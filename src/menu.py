import tkinter as tk

def create_input_menu(root, build_bezier_curve, quit_window, font_family):
    """
    Creates the input menu for Bezier Curve Builder.
    """
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
    iteration_label = tk.Label(root, text="Iteration :", font=(font_family, 14))
    iteration_label.pack()

    entry_iteration = tk.Entry(root, width=10, font=(font_family, 14))
    entry_iteration.pack()

    return entry_point0_x, entry_point0_y, entry_point1_x, entry_point1_y, entry_point2_x, entry_point2_y, entry_iteration

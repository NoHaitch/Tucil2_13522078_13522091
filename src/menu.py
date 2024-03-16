import tkinter as tk
from style import *

num_points = 3  # Default to 3 points, can be modified as needed

def create_input_menu(root) -> tk.Entry:
    """
    Creates the input menu for Bezier Curve Builder.
    """
    # Title
    title_label = tk.Label(root, text="Bezier Curve Builder", font=(font_family, font_size_title, "bold"))
    title_label.pack(pady=10)

    # Sub-title
    subtitle_label = tk.Label(root, text="made by Sean and Francisco", font=(font_family, font_size_normal))
    subtitle_label.pack()

    # Function to create input fields for a single point
    def create_point_input(frame, index):
        point_label = tk.Label(frame, text=f"Point {index}:", font=(font_family, font_size_normal))
        point_label.grid(row=index, column=0, padx=5, pady=2, sticky="e")
        entry_point_x = tk.Entry(frame, width=5, font=(font_family, font_size_normal))
        entry_point_x.grid(row=index, column=1, padx=5, pady=2)
        entry_point_y = tk.Entry(frame, width=5, font=(font_family, font_size_normal))
        entry_point_y.grid(row=index, column=2, padx=5, pady=2)
        return entry_point_x, entry_point_y

    # Point Inputs
    point_frame = tk.Frame(root)
    point_frame.pack(pady=10)

    point_entries = []

    for i in range(num_points):
        point_entries.append(create_point_input(point_frame, i))

    # Iteration Input
    iteration_label = tk.Label(root, text="Iteration :", font=(font_family, font_size_normal))
    iteration_label.pack()

    entry_iteration = tk.Entry(root, width=10, font=(font_family, font_size_normal))
    entry_iteration.pack()

    def get_points():
        return [(entry_point_x.get(), entry_point_y.get()) for entry_point_x, entry_point_y in point_entries]

    return entry_iteration, get_points

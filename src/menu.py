from utils import *
from style import *
from chart import generate_bf_chart, generate_dc_chart
from bfBezier import bfBezier
from dcBezier import dcBezier

# Menu - Ask for amount of control points
def create_input_amount_of_points(root : Tk) -> None:
    # Title
    title_label = tk.Label(root, text="Bezier Curve Builder", font=(font_family, font_size_title, "bold"))
    title_label.pack(pady=10)

    # Sub-title
    subtitle_label = tk.Label(root, text="made by Sean and Francisco", font=(font_family, font_size_subtitle))
    subtitle_label.pack()

    # Amount of Control Point Label
    iteration_label = tk.Label(root, text="Amount of Points :", font=(font_family, font_size_normal))
    iteration_label.pack(pady=10)

    # Amount of Control Point Input
    entry_amount_of_points = tk.Entry(root, width=10, font=(font_family, font_size_normal))
    entry_amount_of_points.pack(pady=10)

    # Button
    button_frame = tk.Frame(root)
    button_frame.pack()
    bf_button = tk.Button(button_frame, text="Start Building", command=lambda: create_input_points(entry_amount_of_points.get()), font=(font_family, font_size_normal, "bold"))
    bf_button.grid(row=0, column=0, padx=5)

    return 

# Menu - Ask for all control points
def create_input_points(string_amount_of_points : str) -> None:
    # Validate amount of points 
    if string_amount_of_points.strip() == '':
        messagebox.showerror("Error", "Please enter the amount of points.")
        return

    if not string_amount_of_points.isdigit():
        messagebox.showerror("Error", "Amount of Points must be a number.")
        return
    else: 
        amount_of_points = int(string_amount_of_points)
    
    if amount_of_points < 3:
        messagebox.showerror("Error", "Amount of Points must be 3 or above.")
        return
    
    # Create tkinter Window
    root = tk.Tk()
    root.title("Bezier Curve Builder")

    # Window Size and Position
    window_width = 400
    window_height = 350 + (25 * (amount_of_points - 3))
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))
    
    # Title
    title_label = tk.Label(root, text=f"Input {amount_of_points} Points", font=(font_family, font_size_subtitle, "bold"))
    title_label.pack(pady=10)
        
    def create_point_input(frame, index) -> tuple[Entry, Entry]:
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

    for i in range(amount_of_points):
        point_entries.append(create_point_input(point_frame, i))

    def get_points() -> list[tuple[str, str]]:
        return [(entry_point_x.get(), entry_point_y.get()) for entry_point_x, entry_point_y in point_entries]

    # Iteration Input
    iteration_label = tk.Label(root, text="Iteration :", font=(font_family, font_size_normal))
    iteration_label.pack()

    entry_iteration = tk.Entry(root, width=10, font=(font_family, font_size_normal))
    entry_iteration.pack()

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

# Build Bezier Curve Logic 
def build_bezier_curve(points : list[tuple[str, str]], str_iteration : str, use_divide_conquer : bool):
    # Validate all points
    for point in points:
        if point[0].strip() == '' or point[1].strip() == '' :
            messagebox.showerror("Error", "Please fill all x and y coordinates.")
            return
        
        if not is_float(point[0]) or not is_float(point[1]) :
            messagebox.showerror("Error", "All x and y coordinates must be a real number.")
            return
    
    # Validate iteration
    if str_iteration.strip() == '':
        messagebox.showerror("Error", "Please enter the iteration value.")
        return
    
    if not str_iteration.isdigit():
        messagebox.showerror("Error", "Iteration must be a positive number.")
        return
    else:
        iteration = int(str_iteration)
    
    if iteration < 1:
        messagebox.showerror("Error", "Iteration must be a positive number.")
        return

    # Convert points to Point objects
    control_points = [Point(float(x), float(y)) for x, y in points]

    if use_divide_conquer:
        # Use Divide Conquer algorithm
        dc_bezier_points, time = dcBezier(control_points, iteration, len(control_points))

        # Generate Chart
        generate_dc_chart(control_points, dc_bezier_points, time)
    else:
        # Checks if the amount of points = 3
        if len(control_points) != 3:
            messagebox.showerror("Error", "Brute Force is only available for 3 points.")
            return

        # Use Brute Force algorithm
        bf_bezier_points, time = bfBezier(control_points[0], control_points[1], control_points[2], iteration)
        
        # Generate Chart
        generate_bf_chart(control_points, bf_bezier_points, time)

        
    
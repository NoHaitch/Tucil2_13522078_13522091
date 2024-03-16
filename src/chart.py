from utils import *
from style import *

def generate_chart(control_points: list[Point], bezier_points: list[Point]) -> None:
    # Create the main window
    root = tk.Tk()
    root.title("Bezier Curve")

    # Create the Matplotlib figure
    fig, ax = plt.subplots()

    control_points_x = [point.x for point in control_points]
    control_points_y = [point.y for point in control_points]
    bezier_points_x = [point.x for point in bezier_points]
    bezier_points_y = [point.y for point in bezier_points]

    # ===== Control Points =====
    ax.scatter(control_points_x, control_points_y, s=40, edgecolors=color_control_point, facecolors=color_control_point, linewidth=2)
    ax.plot(control_points_x, control_points_y, color=color_control_point, linewidth=1)

    # ===== Bezier Points =====
    ax.scatter(bezier_points_x, bezier_points_y, s=40, edgecolors=color_bezier_point, facecolors=color_bezier_point, linewidth=2)
    ax.plot(bezier_points_x, bezier_points_y, color=color_bezier_point, linewidth=1)

    # Set labels and title
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Bezier Curve")

    # Add some empty space around the chart
    ax.set_xlim(min(control_points_x) - empty_space_chart, max(control_points_x) + empty_space_chart)
    ax.set_ylim(min(control_points_y) - empty_space_chart, max(control_points_y) + empty_space_chart)

    # Embed the plot into the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Function to quit the application
    def quit_window():
        root.quit()
        root.destroy()

    # Add a quit button
    quit_button = tk.Button(master=root, text="Quit", command=quit_window)
    quit_button.pack(side=tk.BOTTOM)

    # Bind the window close event to the quit function
    root.protocol("WM_DELETE_WINDOW", quit_window)

    # Start the main loop
    root.mainloop()
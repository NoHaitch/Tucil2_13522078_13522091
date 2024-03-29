from utils import *
from style import *

# Generate Chart for Brute Force
def generate_bf_chart(control_points: list[Point], bezier_points: list[Point], time: int) -> None:
    # Create the main window
    root = tk.Tk()
    root.title(f"Result Bezier Curve - {len(control_points)} Points - Brute Force")

    root.geometry("800x800")

    # Create the Matplotlib figure
    fig, ax = plt.subplots()

    # ===== Control Points =====
    control_points_x = [point.x for point in control_points]
    control_points_y = [point.y for point in control_points]
    ax.scatter(control_points_x, control_points_y, s=control_point_circle_radius, edgecolors=color_control_point, facecolors=color_control_point, linewidth=control_point_line_width)
    ax.plot(control_points_x, control_points_y, color=color_control_point, linewidth=control_point_line_width)

    # ===== Bezier Points =====
    bezier_points_x = [point.x for point in bezier_points]
    bezier_points_y = [point.y for point in bezier_points]
    if len(bezier_points) > 15:
        ax.scatter(bezier_points_x, bezier_points_y, s=15, edgecolors=color_bezier_point, facecolors=color_bezier_point, linewidth=2)
        ax.plot(bezier_points_x, bezier_points_y, color=color_bezier_point, linewidth=bezier_line_width)
    else:
        ax.scatter(bezier_points_x, bezier_points_y, s=bezier_circle_radius, edgecolors=color_bezier_point, facecolors=color_bezier_point, linewidth=2)
        ax.plot(bezier_points_x, bezier_points_y, color=color_bezier_point, linewidth=bezier_line_width)

    # Set labels and title
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Brute Force Bezier Curve")

    # Add some empty space around the chart
    ax.set_xlim(min(control_points_x) - empty_space_chart, max(control_points_x) + empty_space_chart)
    ax.set_ylim(min(control_points_y) - empty_space_chart, max(control_points_y) + empty_space_chart)

    # Embed the plot into the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Runtime
    time_ms = round(time * 1000, 2)
    time_text = tk.Label(root, text=f"Run Time: {time_ms} ms", font=("Helvetica", 10))
    time_text.place(x=40, y=770, anchor="sw")


# Generate Chart for Divide And Conquer
def generate_dc_chart(control_points: list[Point], bezier_points_list: list[list[Point]], time: int) -> None:
    # Create the main window
    root = tk.Tk()
    root.title(f"Result Bezier Curve - {len(control_points)} Points - Divide and Conquer")

    # Set window size
    root.geometry("800x800")

    # Create the Matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 5.5))

    # ===== Control Points =====
    control_points_x = [point.x for point in control_points]
    control_points_y = [point.y for point in control_points]
    ax.scatter(control_points_x, control_points_y, s=control_point_circle_radius, edgecolors=color_control_point, facecolors=color_control_point, linewidth=control_point_line_width)
    ax.plot(control_points_x, control_points_y, color=color_control_point, linewidth=control_point_line_width, label=f'Control Points')

    # ===== Bezier Curve =====
    # Create a colormap
    colormap = plt.cm.get_cmap('tab10')

    # Function to update plot when slider value changes
    def update(val):
        iteration = int(slider.val) - 1
        ax.clear()
        ax.scatter(control_points_x, control_points_y, s=control_point_circle_radius, edgecolors=color_control_point, facecolors=color_control_point, linewidth=control_point_line_width)
        ax.plot(control_points_x, control_points_y, color=color_control_point, linewidth=control_point_line_width, label=f'Control Points')
        bezier_points = bezier_points_list[iteration]
        if(iteration == -1):
            num_lines = len(bezier_points_list)            
            max_amount_of_lines = max([len(bezier_points) for bezier_points in bezier_points_list])
            for i, bezier_points in enumerate(bezier_points_list):
                bezier_points_x = [point.x for point in bezier_points]
                bezier_points_y = [point.y for point in bezier_points]
                color = colormap(i / num_lines)  # Generate a color from the colormap
                if max_amount_of_lines > 15:
                    ax.scatter(bezier_points_x, bezier_points_y, s=15, edgecolors=color, facecolors=color, linewidth=bezier_line_width)
                    ax.plot(bezier_points_x, bezier_points_y, color=color, linewidth=bezier_line_width, label=f'Iteration-{i+1}')
                else:
                    ax.scatter(bezier_points_x, bezier_points_y, s=bezier_circle_radius, edgecolors=color, facecolors=color, linewidth=bezier_line_width)
                    ax.plot(bezier_points_x, bezier_points_y, color=color, linewidth=bezier_line_width, label=f'Iteration-{i+1}')
        else:
            color = colormap(iteration / len(bezier_points_list))
            bezier_points_x = [point.x for point in bezier_points]
            bezier_points_y = [point.y for point in bezier_points]
            if len(bezier_points) > 15:
                ax.scatter(bezier_points_x, bezier_points_y, s=15, edgecolors=color, facecolors=color, linewidth=bezier_line_width)
                ax.plot(bezier_points_x, bezier_points_y, color=color, linewidth=bezier_line_width, label=f'Iteration-{iteration+1}')
            else:
                ax.scatter(bezier_points_x, bezier_points_y, s=bezier_circle_radius, edgecolors=color, facecolors=color, linewidth=bezier_line_width)
                ax.plot(bezier_points_x, bezier_points_y, color=color, linewidth=bezier_line_width, label=f'Iteration-{iteration+1}')
        ax.legend()
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_title("Divide and Conquer Bezier Curve")
        ax.set_xlim(min(control_points_x) - empty_space_chart, max(control_points_x) + empty_space_chart)
        ax.set_ylim(min(control_points_y) - empty_space_chart, max(control_points_y) + empty_space_chart)

    # Add slider
    slider_ax = plt.axes([0.1, 0.01, 0.8, 0.03], facecolor='lightgoldenrodyellow')
    slider = Slider(slider_ax, 'Iteration', 0, len(bezier_points_list), valinit=0, valstep=1)
    slider.on_changed(update)

    # Set slider label
    slider_label = plt.text(0.5, 0.02, 'Iteration', ha='center')

    # Initialize plot with first iteration
    update(0)

    # Embed the plot into the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=5)

    # Runtime
    time_ms = round(time * 1000, 2)
    time_text = tk.Label(root, text=f"Run Time: {time_ms} ms", font=("Helvetica", 10))
    time_text.place(x=40, y=750, anchor="sw")
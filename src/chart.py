from util import *

def generate_chart(control_points: list[Point]) -> None:
    # Create the main window
    root = tk.Tk()
    root.title("Bezier Curve")

    # Create the Matplotlib figure
    fig, ax = plt.subplots()

    x = [point[0] for point in control_points]
    y = [point[1] for point in control_points]

    # Plot control points with matching color and thicker border
    ax.scatter(x, y, s=40, edgecolors='#C34468', facecolors='#C34468', linewidth=2)

    # Connect the points with a colored line
    ax.plot(x, y, color='#C34468', linewidth=1)

    # Set labels and title
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Bezier Curve")

    # Add some empty space around the chart
    ax.set_xlim(min(x) - 5, max(x) + 5)
    ax.set_ylim(min(y) - 5, max(y) + 5)

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
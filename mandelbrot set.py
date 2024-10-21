import matplotlib
# Set the backend to 'TkAgg' or 'Qt5Agg' (change according to your installation)
matplotlib.use('TkAgg')  # or 'Qt5Agg'

import numpy as np
import matplotlib.pyplot as plt

# Setting parameters
xDomain = np.linspace(-2, 1.5, 500)
yDomain = np.linspace(-2, 2, 500)
bound = 2
max_iterations = 50  # Any positive integer value
colormap = 'magma'   # Set to any matplotlib valid colormap

# A flag to control whether the loop should run
stop_animation = False
power = 1  # Starting power value

# Function to compute and plot the multibrot set
def plot_multibrot(power):
    iterationArray = []
    for y in yDomain:
        row = []
        for x in xDomain:
            c = complex(x, y)
            z = 0
            for iterationNumber in range(max_iterations):
                if abs(z) >= bound:
                    row.append(iterationNumber)
                    break
                else:
                    z = z**power + c  # Multibrot formula
            else:
                row.append(0)
        iterationArray.append(row)

    iterationArray = np.array(iterationArray)

    # Plotting the data
    plt.clf()  # Clear the previous plot
    ax = plt.axes()
    ax.set_aspect('equal')

    graph = ax.pcolormesh(xDomain, yDomain, iterationArray, cmap=colormap, shading='auto')
    plt.colorbar(graph)
    plt.xlabel("Real-Axis")
    plt.ylabel("Imaginary-Axis")
    plt.title(f'Multibrot set for $z_{{new}} = z^{{{power}}} + c$')
    plt.gcf().set_size_inches(5, 4)

    plt.draw()  # Redraw the current frame
    plt.pause(0.1)  # Pause briefly to allow plot to refresh

# Function to update the animation
def update_animation():
    global power, stop_animation
    if not stop_animation:
        plot_multibrot(power)
        power += 0.1  # Increment power
        if power > 10:  # Reset power if it exceeds 10
            power = 1
        plt.gcf().canvas.flush_events()  # Ensure events are processed
        update_animation()  # Call this function again

# Function to stop the animation
def stop_animation_func(event):
    global stop_animation
    stop_animation = True
    plt.close()  # Close the plot when stopped

# Start the animation
plt.ion()  # Turn on interactive mode
plt.figure()  # Create a new figure
update_animation()  # Start the animation

# Connect the key press event to stop the animation
plt.gcf().canvas.mpl_connect('key_press_event', stop_animation_func)

# Keep the plot window open and responsive
plt.show(block=True)  # Ensure that plt.show() blocks until the plot is closed

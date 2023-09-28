import pandas as pd
import matplotlib.pyplot as plt

dataset_path = "data/sensor_data.csv"

df = pd.read_csv(dataset_path)

# Create a single figure and axis outside the loop
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel('Red')
ax.set_ylabel('Green')

for index, row in df.iterrows():
    # Normalize the RGB values to the [0, 1] range required by Matplotlib
    normalized_red = row["Red"] / 255.0
    normalized_green = row["Green"] / 255.0
    normalized_blue = row["Blue"] / 255.0

    # Create a color tuple (R, G, B) and update the rectangle's color
    color_tuple = (normalized_red, normalized_green, normalized_blue)

    if index > 0:
        ax.patches[0].set_facecolor(color_tuple)  # Update the color of the existing rectangle
    else:
        ax.add_patch(plt.Rectangle((0, 0), 1, 1, color=color_tuple))  # Create the initial rectangle

    plt.pause(0.1)  # Pause for visualization

plt.close()

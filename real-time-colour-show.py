import matplotlib.pyplot as plt

# Read 8-bit RGB color values (replace these values with your data)
red = 101
green = 101
blue = 101

# Normalize the RGB values to the [0, 1] range required by Matplotlib
normalized_red = red / 255.0
normalized_green = green / 255.0
normalized_blue = blue / 255.0

# Create a color tuple (R, G, B) and display it
color_tuple = (normalized_red, normalized_green, normalized_blue)

# Create a figure with a colored rectangle
fig, ax = plt.subplots()
ax.add_patch(plt.Rectangle((0, 0), 1, 1, color=color_tuple))

# Set axis limits and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel('Red')
ax.set_ylabel('Green')

# Display the color
plt.show()

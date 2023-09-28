import serial
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define my port and baud rate
port_addr = "/dev/cu.usbmodem14101"
baud_rate = 9600

ser = serial.Serial(port=port_addr, baudrate=baud_rate)

# Create a figure, axis, and a rectangle
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel('Red')
ax.set_ylabel('Green')

color_rectangle = patches.Rectangle((0, 0), 1, 1, color='white')
ax.add_patch(color_rectangle)

plt.ion()  # Turn on interactive mode

try:
    while True:
        data_read = ser.readline().decode().strip()
        values = data_read.split(',')[:-1]

        if len(values) == 3:
            r, g, b = map(int, values)

            normalized_red = r / 255.0
            normalized_green = g / 255.0
            normalized_blue = b / 255.0

            # Update the color of the existing rectangle
            color_tuple = (normalized_red, normalized_green, normalized_blue)
            color_rectangle.set_color(color_tuple)

            # Redraw the plot
            fig.canvas.flush_events()

except KeyboardInterrupt:
    pass  # Exit the loop gracefully when Ctrl+C is pressed

# Close the serial connection
ser.close()

plt.ioff()  # Turn off interactive mode
plt.show()

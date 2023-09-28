import serial
import pandas as pd

# Define my port and baud rate
port_addr = "/dev/cu.usbmodem14101"
baud_rate = 9600
dataset_path = "data/sensor_data.csv"

ser = serial.Serial(port=port_addr, baudrate=baud_rate)

# Initialize lists to store sensor data
red_data, green_data, blue_data, index_no = [], [], [], []

try:
    while True:
        data_read = ser.readline().decode().strip()
        values = data_read.split(',')[:-1]

        if len(values) == 3:
            r, g, b = map(int, values)

            red_data.append(r)
            green_data.append(g)
            blue_data.append(b)
            index_no.append(len(index_no))

except KeyboardInterrupt:
    pass  # Exit the loop gracefully when Ctrl+C is pressed

# Create a DataFrame from the collected data
sensor_df = {"Index": index_no, "Red": red_data, "Green": green_data, "Blue": blue_data}
df = pd.DataFrame(sensor_df)

# Save the DataFrame to a CSV file
df.to_csv(dataset_path, index=False)

# Close the serial connection
ser.close()

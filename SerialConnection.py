import serial
import pandas as pd

# define my port and baud rate
port_addr = "/dev/cu.usbmodem14101"
baud_rate = 9600
dataset_path = "data/sensor_data.csv"

no_of_bytes = 11
read_upto = 100

red_data = []  # create empty list to store sensor data
green_data = []  # create empty list to store sensor data
blue_data = []  # create empty list to store sensor data
index_no = []

ser = serial.Serial(port=port_addr, baudrate=baud_rate)

for i in range(read_upto):
    data_read = ser.readline().decode().strip()
    values = data_read.split(',')[:-1]

    if len(values) == 3:
        r, g, b = map(int, values)

        red_data.append(r)
        green_data.append(g)
        blue_data.append(b)
        index_no.append(i)

sensor_df = {"Index": index_no, "Red": red_data, "Green": green_data, "Blue": blue_data}
df = pd.DataFrame(sensor_df)
df.to_csv(dataset_path, index=False)

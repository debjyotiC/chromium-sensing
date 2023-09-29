import serial
import pandas as pd

# define my port and baud rate
port_addr = "/dev/cu.usbmodem14101"
dataset_path = "data/sensor_data_white.csv"
baud_rate = 9600


no_of_bytes = 11
read_upto = 100

index_no, red_data, green_data, blue_data = [], [], [], []

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

        print(".", end="")

sensor_df = {"Index": index_no, "Red": red_data, "Green": green_data, "Blue": blue_data}
df = pd.DataFrame(sensor_df)
df.to_csv(dataset_path, index=False)

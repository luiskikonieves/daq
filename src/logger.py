import csv
import time

class Logger:
    def __init__(self):
        # Generate filename based on the current date and time in ISO 8601 format
        current_time = time.strftime("%Y-%m-%dT%H-%M-%S")
        self.filename = f'ina219_data_{current_time}.csv'
        # Open the file in append mode with newline='' to avoid blank lines in CSV
        self.file = open(self.filename, 'a', newline='')
        self.writer = csv.writer(self.file)
        # Write the header only if the file is empty (i.e., newly created)
        if self.file.tell() == 0:
            self.writer.writerow(["Timestamp", "Shunt Voltage (mV)", "Bus Voltage (V)", "Current (mA)", "Power (W)"])

    def log_data(self, shunt_voltage, bus_voltage, current, power):
        # Get the current time as a readable string
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        # Write a row of data
        self.writer.writerow([timestamp, shunt_voltage, bus_voltage, current, power])

    def close(self):
        self.file.close()

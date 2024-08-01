from logger import Logger
from ina219 import INA219
import time

# Initialize the INA219 sensor and Logger
# We currently only get data from a single channel
ina1 = INA219(addr=0x40)
logger = Logger()

try:
    while True:
        # Read sensor data
        shunt_voltage = ina1.getShuntVoltage_mV()
        bus_voltage = ina1.getBusVoltage_V()
        current = ina1.getCurrent_mA()
        power = ina1.getPower_W()

        # Log data
        logger.log_data(shunt_voltage, bus_voltage, current, power)

        print(f"Logged data at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(0.02) # 20 milliseconds, or 50 Hz
except KeyboardInterrupt:
    print("Logging stopped by user.")
finally:
    logger.close()
    print("File closed.")

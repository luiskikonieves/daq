# daq

Welcome to a poor-man's data acquisition (DAQ) device.

This repo utilizes a Raspberry Pi and
[Waveshare Current/Power Monitor HAT](https://www.waveshare.com/wiki/Current/Power_Monitor_HAT)
to monitor power draw and loads. It's designed to log the data read from a 
Plettenberg NOVA 15 motor and save it to EEPROM.

That's it, nothing fancy.

## Dependencies

After flashing RPi OS install the following on the Raspberry Pi: 

`sudo apt-get install python3-smbus`

## Running / Installation

Copy over all relevant files to the RPi. Remember to make all files executable `chmod +x *.py`. 

If you want to daemonize the application, run the following commands: 

This will make the application start at boot and start logging. Logs are rotated at boot,
and eventually deleted if running out of disk space. 
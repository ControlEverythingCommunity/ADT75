# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# ADT75
# This code is designed to work with the ADT75_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Temperature?sku=ADT75_I2CS#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# ADT75 address, 0x48(72)
# Read data back from 0x00(00), 2 bytes
# temp MSB, temp LSB
data = bus.read_i2c_block_data(0x48, 0x00, 2)

# Convert the data to 12-bits
temp = ((data[0] * 256) + data[1]) / 16
cTemp = temp * 0.0625
fTemp = (temp * 0.1125) + 32

# Output data to screen
print "Temperature in Celsius : %.2f C" %cTemp
print "Temperature in Fahrenheit : %.2f F" %fTemp

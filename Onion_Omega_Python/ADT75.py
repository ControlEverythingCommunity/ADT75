# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# ADT75
# This code is designed to work with the ADT75_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Temperature?sku=ADT75_I2CS#tabs-0-product_tabset-2

from OmegaExpansion import onionI2C
import time

# Get I2C bus
i2c = onionI2C.OnionI2C()

# ADT75 address, 0x48(72)
# Read data back from 0x00(00), 2 bytes
# temp MSB, temp LSB
data = i2c.readBytes(0x48, 0x00, 2)

# Convert the data to 12-bits
temp = ((data[0] * 256) + data[1]) / 16
if temp > 2047 :
    temp -= 4096	
cTemp = temp * 0.0625
fTemp = (cTemp * 1.8) + 32

# Output data to screen
print "Temperature in Celsius : %.2f C" %cTemp
print "Temperature in Fahrenheit : %.2f F" %fTemp

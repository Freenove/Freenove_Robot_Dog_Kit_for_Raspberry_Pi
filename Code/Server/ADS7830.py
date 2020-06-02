import smbus
import time
class ADS7830:
	def __init__(self):
		# Get I2C bus
		self.bus = smbus.SMBus(1)
		# I2C address of the device
		self.ADS7830_DEFAULT_ADDRESS			= 0x48
		# ADS7830 Command Set
		self.ADS7830_CMD				= 0x84 # Single-Ended Inputs
	def readAdc(self,channel):
		"""Select the Command data from the given provided value above"""
		COMMAND_SET = self.ADS7830_CMD | ((((channel<<2)|(channel>>1))&0x07)<<4)
		self.bus.write_byte(self.ADS7830_DEFAULT_ADDRESS, COMMAND_SET)
		data = self.bus.read_byte(self.ADS7830_DEFAULT_ADDRESS)
		return data
	def power(self,channel):
		data=['','','','','','','','','']
		for i in range(9):
			data[i]=self.readAdc(channel)
		data.sort()
		battery_voltage=data[4]/255.0*5.0*3
		return battery_voltage
if __name__ == '__main__':
	a=ADS7830()
	print(a.power(0))

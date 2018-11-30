# BME280 - a cheap measure of temperature, pressure and humidity in the environment

import board
import digitalio
import busio
from time import time, strftime, sleep
import adafruit_bme280
import matplotlib.pyplot as plt

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL,board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25



x = []
y = []

def write_temp(temp):
    start_time = strftime("%Y-%m-%d %H:%M:%S")
    print(start_time)
    with open("/home/pi/cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()

def main():
    start_time = strftime("%Y-%m-%d %H:%M:%S")
    print(start_time)
    while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    time.sleep(2)

if __name__ == '__main__':
    main()


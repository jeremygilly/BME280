# BME280 - a cheap measure of temperature, pressure and humidity in the environment

import board
import digitalio
import busio
from time import time, strftime, sleep
import adafruit_bme280
#import matplotlib.pyplot as plt

# Create library object using our Bus I2C port
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, cs)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25



x = []
y = []

#def graph(temp):
#   y.append(temp)
#    x.append(time())
#    plt.clf()
#    plt.scatter(x,y)
#    plt.plot(x,y)
#    plt.draw()

def main():
    start_time = strftime("%Y-%m-%d %H:%M:%S")
    print(start_time)
    filename = "/home/pi/Desktop/BME280data_" + str(start_time) + ".csv"
    with open(filename, "a") as log:
        log.write("BME280 data on (yyyy-mm-dd hh:mm:ss) " + start_time+"\n")
        log.write("{0}, {1}, {2}, {3}, {4}\n".format("Time","Seconds from Start (s)", "Temperature (C)", "Humidity (%)", "Pressure (hPa)"))
    seconds_from_start = 0
    interval = 1
    while True:
        time = strftime("%H:%M:%S")
        temperature = bme280.temperature
        humidity = bme280.humidity
        pressure = bme280.pressure
        with open(filename, "a") as log:
          log.write("{0}, {1}, {2}, {3}, {4}\n".format(time, seconds_from_start, temperature,humidity,pressure))
        print(time, seconds_from_start, temperature, humidity, pressure)
        sleep(interval)
        seconds_from_start = seconds_from_start + interval

if __name__ == "__main__":
    main()


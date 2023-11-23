import adafruit_dht
from board import D4

dht_device = adafruit_dht.DHT22(D4)


temperature = dht_device.temperature
humidity = dht_device.humidity


print(f"Temperature: {temperature} deg C")
print(f"Humidity: {humidity} %")
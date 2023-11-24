import datetime as dt
from pathlib import Path

import adafruit_dht
from board import D4  # This is the physical GPIO pin I used

# Intiailaise the device.
dht_device = adafruit_dht.DHT22(D4)


def get_current_data() -> tuple[dt.datetime, float, float]:
    time = dt.datetime.now()  # time now UTC

    try:
        temperature = dht_device.temperature
    except:
        # It's extremely unlikely to reach negative where I live, so this is ok
        temperature = -1.0

    try:
        humidity = dht_device.humidity
    except:
        humidity = -1.0

    return time, temperature, humidity


def generate_filename() -> Path:
    timenow = dt.datetime.now()
    hour_string = timenow.strftime("%Y%m%d_%H")
    file_string = f"./output/{hour_string}.csv"
    filename = Path(file_string)

    return filename


time, temperature, humidity = get_current_data()
output_file = generate_filename()
Path("./output").mkdir(parents=True, exist_ok=True)
output_file.touch(exist_ok=True)

with open(output_file, "a+") as f:
    outstring = f"{time}, {temperature}, {humidity}\n"
    f.write(outstring)

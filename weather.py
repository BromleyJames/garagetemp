""" Extract weather data for the Perth observation station from BOM.
This should extract the last 72 hours of data, at 30 min intervals.
Running this once daily should be more than enough.
"""
import datetime as dt
import tarfile
from ftplib import FTP
from pathlib import Path

ftp = FTP("ftp2.bom.gov.au")

ftp.login()

ftp.cwd("anon/gen")


Path("./weather/temp").mkdir(parents=True, exist_ok=True)


def generate_filename() -> Path:
    timenow = dt.datetime.now()
    date_string = timenow.strftime("%Y%m%d")
    file_string = f"./weather/{date_string}"
    filename = Path(file_string)

    return filename


with open("./weather/README_weather_ftp", "wb") as fp:
    ftp.retrbinary("RETR README", fp.write)

ftp.cwd("fwo")

with open("./weather/weather.xml", "wb") as fp:
    ftp.retrbinary("RETR IDW60920.xml", fp.write)

with open("./weather/weather2.tgz", "wb") as fp:
    ftp.retrbinary("RETR IDW60910.tgz", fp.write)

with tarfile.open("./weather/weather2.tgz") as tar:
    pathname = generate_filename()
    pathname.mkdir(parents=True, exist_ok=True)

    # Extract only the Perth data
    print("Attempting to extract")
    tar.extract("IDW60910.94608.json", path=pathname)

    print("Done!")

# with open('weatherlist', 'w') as file:
#     ftp.dir(file.write)

ftp.quit()

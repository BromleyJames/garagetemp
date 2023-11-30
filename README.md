# garagetemp
Logging the temperature of my garage with a Raspberry Pi

# Setup

Create the python env by running:


```python3 -m pip install -r requirements.txt```


Run `crontab -e` and add the following:


```* * * * * cd /home/pi/Programming/garagetemp && . venv/bin/activate && python temperature.py```

# Weather data

Weather data is dowloaded from the BOM FTP server.

To get 72 hours worth of observations we need to download a GZIP archive and then extract the json file we want: `IDW60910.94608.json`

Since it's 72 hours of data, once daily should be more than enough. Use the following cron job:

```0 4 * * * cd /home/pi/Programming/garagetemp && . venv/bin/activate && python weather.py```

This runs once a day at 4am UTC (so midday Perth).

## TODO

Import weather data from BOM FTP
Also import data from weather.com 

Cron jobs to

    - Restart the raspberry pi weekly
    
    - Save weather data every 30 minutes (?)
    
    - Load data to an S3 bucket hourly, and archive the data in another folder

    
# garagetemp
Logging the temperature of my garage with a Raspberry Pi

# Setup

Run `crontab -e` and add the following:


```* * * * * cd /home/pi/Programming/garagetemp && . venv/bin/activate && python temperature.py```

## TODO

Import weather data from bom FTB
Also import data from weather.com 

Cron jobs to

    - Restart the raspberry pi weekly
    
    - Save weather data every 30 minutes (?)
    
    - Load data to an S3 bucket hourly, and archive the data in another folder

    
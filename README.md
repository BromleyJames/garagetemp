# garagetemp
Logging the temperature of my garage with a Raspberry Pi


## TODO

Import weather data from bom FTB
Also import data from weather.com 

Cron jobs to
    - Restart the raspberry pi weekly
    - Save the temperature to a csv or parquet every minute
    - Save weather date every 30 minutes (?)
    - Load data to an S3 bucket hourly, and archive the data in another folder
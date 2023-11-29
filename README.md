# garagetemp
Logging the temperature of my garage with a Raspberry Pi

# Setup

Create the python env by running:


```python3 -m pip install -r requirements.txt```


Run `crontab -e` and add the following:


```* * * * * cd /home/pi/Programming/garagetemp && . venv/bin/activate && python temperature.py```

## TODO

Import weather data from BOM FTP
Also import data from weather.com 

Cron jobs to

    - Restart the raspberry pi weekly
    
    - Save weather data every 30 minutes (?)
    
    - Load data to an S3 bucket hourly, and archive the data in another folder

    
from ftplib import FTP


ftp = FTP("ftp2.bom.gov.au")

ftp.login()

ftp.cwd('anon/gen') 

with open('README_weather_ftp', 'wb') as fp:
    ftp.retrbinary('RETR README', fp.write) 

ftp.cwd('fwo')

with open('weather.xml', 'wb') as fp:
    ftp.retrbinary('RETR IDW60920.xml', fp.write)

with open('weather2.tgz', 'wb') as fp:
    ftp.retrbinary('RETR IDW60910.tgz', fp.write) 

# with open('weatherlist', 'w') as file:
#     ftp.dir(file.write)

ftp.quit()
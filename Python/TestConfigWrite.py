import configparser
import getpass
import logging

logging.basicConfig(filename='LoggingConfigWrite.log', encoding='utf-8', level=logging.ERROR)

try:
    config = configparser.ConfigParser() 
    username = getpass.getuser()
    
except Exception as ex:
    logging.ERROR(ex)


config['DEFAULT'] = {'PARTH': f'/var/spool/cron/crontabs/{username}',
                     'USER': username}
try:
    with open('/home/igor/Документы/Config/ConfigCrontab.ini', 'w') as file:
        config.write(file)

except Exception as ex:
    logging.ERROR(ex)

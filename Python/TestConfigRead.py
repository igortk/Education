import configparser
import logging

config = configparser.ConfigParser()

logging.basicConfig(filename='LoggingConfigRead.log', 
                    level=logging.ERROR)

try:
     config.read('/home/igor/Документы/Config/ConfigCrontab.ini')

     for key in config['DEFAULT']:  
          print(key +': '+config['DEFAULT'][key])
except Exception as ex:
     logging.error('Problem with file path or file does not exist\n'+ex)

def get_user():
     try:
          return config['DEFAULT']['user']
     except Exception as ex:
          logging.error(ex)

def get_parth():
     try:
          return config['DEFAULT']['parth']
     except Exception as ex:
          logging.error(ex)

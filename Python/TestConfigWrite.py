import getpass
import logging
import json
import os

try:
    dir_name, f_name = os.path.split(__file__)
    logging.basicConfig(filename=dir_name+'/LoggingConfigWrite.log',
                    level=logging.ERROR)
except Exception as ex:
    logging.ERROR(ex)

try:
    username = getpass.getuser()   
except Exception as ex:
    logging.ERROR(ex)

def make_config():
    config_data = {'PATH': f'/var/spool/cron/crontabs/{username}',
                    'LOG_PATH':dir_name+'/LoggingConfigWrite.log',
                    'USER': username,
                    'ENCODING':'utf-8',
                    'LEVEL':logging.ERROR}
    logging.error('Problem with file path or file does not exist\n')
    try:
        with open(dir_name+"/data_file.json", "w") as write_file:
            json.dump(config_data, write_file)

    except Exception as ex:
        logging.ERROR(ex)

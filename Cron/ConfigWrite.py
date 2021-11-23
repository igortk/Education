import logging
import json
import os

log_format = '%(asctime)s - %(filename)s - %(message)s'
log_level = logging.INFO
logging.basicConfig(format=log_format, 
                    level=log_level,
                    filename="logging.log")

try:
    dir_name, f_name = os.path.split(__file__)
except Exception as ex:
    logging.error("Problem with parth.split: "+ex)
    quit()

logging.info('Path was splitted')

try:
    config_data = {'CRON_PATH': dir_name+'/crontab',
                    'LOG_FORMAT': log_format,
                    'LOG_LEVEL':log_level}
    logging.info('Config_data was created')
except Exception as ex:
    logging.error("Problem with create config_data: "+ex)
    quit()

def create_config():
    with open(dir_name+"/data_file.json", "w") as write_file:
        json.dump(config_data, write_file, indent=2)
        logging.info('data_file.json was created')
    return config_data

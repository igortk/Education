import ConfigWrite
import logging
import json
import os

try:
     dir_name, f_name = os.path.split(__file__)
except Exception as ex:
    logging.ERROR("Problem with parth.split: "+ex)
    quit()

logging.info("Path was splitted")

try:
     if(os.path.isfile(dir_name+"/data_file.json")):
          file = open('data_file.json')
          logging.info("Path was opened")
          data = json.loads(file.read())
          logging.info("Json file was loaded to data value")
     else:
          data = ConfigWrite.create_config()
except Exception as ex:
    logging.error("The problem is in the instrument 'if-else': "+ex)
    quit()

logging.debug(data)
logging.info('Path was splitted')

def get_data():
     return data

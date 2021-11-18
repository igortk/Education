import logging
import json
import datetime
import os
import TestConfigWrite

dir_name, f_name = os.path.split(__file__)

if(os.path.isfile(dir_name+"/data_file.json")):
     with open(dir_name+'/data_file.json', 'r') as f:
      data = json.load(f)
else:
     TestConfigWrite.make_config()
     with open(dir_name+'/data_file.json', 'r') as f:
          data = json.load(f)

logging.basicConfig(filename=data['LOG_PATH'],
                    level=data['LEVEL'])

def get_data():
     try:
          return data
     except Exception as ex:
          logging.error('Time: '+datetime.date.today+'\nLog: '+ex)

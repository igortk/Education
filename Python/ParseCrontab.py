from crontab import CronTab
from croniter import croniter
from datetime import datetime
import logging
import TestConfigRead
import os

cron = CronTab(TestConfigRead.get_data()['USER'])
date_today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
logging.basicConfig(filename=TestConfigRead.get_data()['LOG_PATH'],
                    level=TestConfigRead.get_data()['LEVEL'])

for item in cron:
    try:
        item_time=str(item[0])+" "+str(item[1])+" "+str(item[2])+" "+str(item[3])+" "+str(item[4])
        if croniter.match(item_time, date_today):
            os.system(item.command)
    except Exception as ex:
        logging.error('Time: '+datetime.date.today+'\nLog: '+ex)


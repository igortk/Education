from crontab import CronTab
from croniter import croniter
from datetime import datetime
import ConfigRead
import logging
import os

json_data = ConfigRead.get_data()
logging.info(json_data)

try:
    cron = CronTab(tabfile=json_data['CRON_PATH'])
    logging.info("The cron-file has been read")
except Exception as ex:
    logging.error("The file does not exist or the path to the file is not correct: "+str(ex))
    quit()

date_today = datetime.now()

try:
    for cron_str in cron:
        logging.info("Cron time: "+str(cron_str.slices))
        logging.info("Cron command: "+cron_str.command)
        if croniter.match(str(cron_str.slices), date_today):
            pid = os.fork()
            logging.info("Fork was created")
            if(pid==0):
                os.system(cron_str.command)
                logging.info("The command(fork) has been completed")
                exit()
except Exception as ex:
    logging.error("The problem is in the instrument (for): "+str(ex))
    quit()
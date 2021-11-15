from crontab import CronTab
import TestParseRead

cron = CronTab(tabfile=TestParseRead.get_parth(), user=False)

for cronitem in cron:
    cronitemstr = str(cronitem)
    time_cron = cronitemstr.split()
    time_cron = time_cron[0]+" "+time_cron[1]+" "+time_cron[2]+" "+time_cron[3]+" "+time_cron[4]
    print("Time: "+time_cron)
    print("Command: "+cronitemstr[len(time_cron):].lstrip())
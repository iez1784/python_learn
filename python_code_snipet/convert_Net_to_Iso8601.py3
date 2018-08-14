# import datetime
# import time
# ticks = u'/Date(1526785274000-0700)/'


# ticks_int = ticks.encode()
# lenght = len(ticks_int)
# print lenght

# timestamp = ticks_int[6:-10]

# print timestamp
# print type(timestamp)

# int_timestamp = int(timestamp)
# print int_timestamp
# print type(int_timestamp)

# #ISFORMAT="%Y-%m-%d %H:%M:%S"
# #star_time = time.localtime(int_timestamp)
# #times =  time.strftime(ISFORMAT,star_time)
# #print times
# #print time.time()
# dateArray = datetime.datetime.utcfromtimestamp(int_timestamp)
# otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
# print otherStyleTime


import datetime

def parse_date(datestring):
    timepart = datestring.split('(')[1].split(')')[0]
    milliseconds = int(timepart[:-5])
    hours = int(timepart[-5:]) / 100
    time = milliseconds / 1000

    dt = datetime.datetime.utcfromtimestamp(time + hours * 3600)
    return dt.strftime("%Y-%m-%dT%H:%M:%S") + '%02d:00' % hours

ScheduleDate = "\/Date(1374811200000-0400)\/"
StartTime = "\/Date(-2208931200000-0500)\/"

print(parse_date(ScheduleDate))
print(parse_date(StartTime))

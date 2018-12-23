import datetime

launch_date=datetime.date(2017,3,30)
launch_time=datetime.time(22,27,0)
launch_datetime=datetime.datetime(2017,3,30,22,27,0)

message="Spacex was launch on {:%A,%B,%d,%Y}"
print(message.format(launch_date))

#Date access to individual components

print(launch_date.year)
print(launch_date.month)
print(launch_date.day)

#Time access to individual components

print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)

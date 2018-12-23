# Datetime object
import datetime

Shri=datetime.date(1997,3,13)

message="Shri was born on {:%A,%B,%d,%Y}."
print(message.format(Shri))

dt=datetime.timedelta(4)
print(Shri+dt)
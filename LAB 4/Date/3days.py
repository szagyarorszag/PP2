import datetime as dt
print(f"yesterday - {dt.date.today() - dt.timedelta(days=1)}")
print(f"today - {dt.date.today()}")
print(f"tomorrow - {dt.date.today() - dt.timedelta(days=-1)}")
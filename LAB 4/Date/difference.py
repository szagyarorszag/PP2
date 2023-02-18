import datetime as dt
def difference(day , month , year ):
    date = dt.datetime.now() -  dt.datetime(2018,7 , 1 ) 
    print(date.total_seconds())
difference(5 , 5 , 2022)


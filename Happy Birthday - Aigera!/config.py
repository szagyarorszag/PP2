def some_math(datetime_age) :
    total_days = ""
    for i in str(datetime_age):
        if i != " " :
            total_days+=i
        else : break
    return round (int(total_days)/365) 
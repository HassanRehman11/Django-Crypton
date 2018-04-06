import datetime

    
class time:
    @staticmethod
    def date():
        a = (datetime.datetime.now())
        lala =int(a.hour)
        if (lala>=0 and lala<=12):
            date = str(datetime.datetime.today()-datetime.timedelta(days=1))
            return(date.split(' ')[0])
        else:
            date = str(datetime.datetime.today())
            return(date.split(' ')[0])   

x = time
a = x.date()
print(a)

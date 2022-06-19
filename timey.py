import time 

import datetime

class TimingClass:

    def __init__(self):

        self.YEAR        = datetime.date.today().year
        self.MONTH       = datetime.date.today().month
        self.DATE        = datetime.date.today().day
        self.HOUR        = datetime.datetime.now().hour
        self.MINUTE      = datetime.datetime.now().minute
        self.SECONDS     = datetime.datetime.now().second
        
        self.TODAY       = datetime.date.today()
        self.YESTERDAY   = datetime.datetime.strftime( (self.TODAY - datetime.timedelta(days = 1)) , '%Y-%m-%d')
        self.TOMORROW   = datetime.datetime.strftime( (self.TODAY + datetime.timedelta(days = 1)) , '%Y-%m-%d')
        
        self.TODAY_datetime = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())
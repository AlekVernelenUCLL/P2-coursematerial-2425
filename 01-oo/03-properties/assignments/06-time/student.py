class Time():
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, value):
        if isinstance(value, int) and 0 <= value <= 23:
            self.__hours = value
        else:
            raise ValueError("not correct hour")
        
    @property
    def minutes(self):
        return self.__minutes
    
    @minutes.setter
    def minutes(self, value):
        if isinstance(value, int) and 0 <= value <= 59:
            self.__minutes = value
        else:
            raise ValueError("Not correct minute")
        
    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    def seconds(self, value):
        if isinstance(value, int) and 0 <= value <= 59:
            self.__seconds = value
        else:
            raise ValueError("Not correct second")
        

time = Time(0,0,0)
time.hours = 8
time.minutes = 6
time.seconds = 3
print(time.hours, time.minutes, time.seconds)
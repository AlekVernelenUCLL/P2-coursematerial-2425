class LengthConverter:
    def __init__(self):
        self.distance_in_meter = 0

    @property
    def meter(self):
        return self.__distance_in_meter
    
    @meter.setter
    def meter(self, value):
        self.__distance_in_meter = value

    @property
    def feet(self):
        return self.__distance_in_meter * 3.281
    
    @feet.setter
    def feet(self, value):
        self.__distance_in_meter = value / 3.281

    @property
    def inch(self):
        return self.__distance_in_meter * 39.370
    
    @inch.setter
    def inch(self, value):
        self.__distance_in_meter = value / 39.370
    

converter = LengthConverter()
converter.inch = 50
print(converter.meter)
print(converter.feet)
print(converter.inch)
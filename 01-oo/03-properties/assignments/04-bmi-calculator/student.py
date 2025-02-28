class BMICalculator():
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.bmi = self.calc_bmi()
        self.category = self.category()

    def calc_bmi(self):
        return round(self.weight/(self.height**2), 2)
    
    def category(self):
        if 18.5 <= self.bmi <= 25:
            return "normal"
        elif self.bmi < 18.5:
            return "underweight"
        else:
            return "overweight"
    

calc = BMICalculator(weight=80, height=1.80)
print(calc.bmi)
print(calc.category)
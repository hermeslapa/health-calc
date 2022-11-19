
class Imc:
    """Object tha will be used to calculete the IMC of a person"""
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    
    def calc_imc(self):
        """"Method to calculate the current IMC"""
        return round((self.weight/(self.height**2)),2)
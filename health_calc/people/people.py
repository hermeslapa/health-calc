import uuid
from datetime import date, datetime
from dataclasses import dataclass

@dataclass
class People:
    serial = uuid.uuid1()
    """Class to define a person who'll calculate the imc"""

    def __init__(
        self,
        name: str,
        sex: str,
        birth: date,
        height: float,
        weight: float,
        imc=None,
        last_calc=None
    ):
        self.id = str(People.serial)
        self.name = name
        self.sex = sex
        self.birth = birth
        self.height = height
        self.weight = weight
        self.imc = imc
        self.last_calc = last_calc

from datetime import datetime
from health_calc.imc.imc import Imc
from health_calc.people.people import People


def test__calc_imc():
    imc=Imc(1.80,123)
    assert imc.calc_imc() == 37.96

def test__person():
    assert People('Hermes','Masculino',datetime(1992,6,15),1.80,100) == People('Hermes','Masculino',datetime(1992,7,14),1.80,100)

def test__values():
    p1= People('Hermes','Masculino',datetime(1992,6,15),1.80,100) 
    p2=People('Hermes','Masculino',datetime(1992,7,14),1.90,115)
    assert p1.height != p2.height
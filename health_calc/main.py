from datetime import datetime
from people.people import People
from imc.imc import Imc


def test_data(data,typ):
    if isinstance(data,typ):
        return data
    else:
        raise TypeError

def create_person(name,sex,birth,height,weight)->People:
    name=test_data(name,str)
    sex=test_data(sex,str)
    birth=test_data(birth,datetime)
    height=test_data(height,float)
    weight=test_data(weight,float)
    return People(name,sex,birth,height,weight)

def calc_imc(person):
    imc=Imc(person.height,person.weight)
    return imc.calc_imc()

def get_data_from_console():
    name = input("\nDigite seu nome: ")
    sex=input("\nDigite seu sexo (M,S ou O): ")
    birth=datetime.strptime(input("\nDigite sua data de nascimento(DD-MM-AAAA): "),"%d-%m-%Y")
    height=float(input("\nDigite seu altura(em m e use . ): "))
    weight=float(input("\nDigite seu peso (kg): "))
    return name,sex,birth,height,weight

if __name__ == "__main__":
    print("Bem vindo á calculadora de IMC !!!")
    print("Por favor, entre com os seus dados para o calculo:")
    name,sex,birth,height,weight= get_data_from_console()
    people=create_person(name,sex,birth,height,weight)
    result=calc_imc(people)
    print(f"Seu IMC é: {result}")
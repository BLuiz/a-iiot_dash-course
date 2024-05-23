"""Projeto de jogo: Simulador de caos na academia"""
from time import sleep
from os import system
from M11_CaosAcademias.Gym_Class import Gym
from M11_CaosAcademias.Athlete_Class import Proactive, Reactive

nomes = [
    "Ana","Carlos","Maria","João","Camila","Lucas","Amanda","Pedro","Mariana",
    "Gabriel","Juliana","Diego","Patrícia","Rafael","Isabela","Felipe","Fernanda",
    "Bruno","Larissa", "Vinícius","Carolina","Gustavo","Tatiane","Thiago","Natália",
    "Luciano","Letícia","Rodrigo","Renata","Fábio","Vanessa","Daniel","Lívia",
    "Leonardo","Michelle","Luiz","Talita","Eduardo","Jessica","André","Débora",
    "Ricardo","Aline","Marcelo","Bianca","Cristiano","Priscila","Alexandre","Poliana"]

# Definição de constantes para pesos da academia e quantidade de atletas
LIGHTER = 10
HEAVIER = 32
REACTIVE = 2
PROACTIVE = 6

def gymsim():
    # Inicializando academia
    acad = Gym(LIGHTER, HEAVIER)
    print(acad)

    # Inicializando atletas
    for i, nome in enumerate(nomes):
        print(i, end=' ')
        if 0<=i<REACTIVE:           atleta = Reactive(name=nome)
        elif i<REACTIVE+PROACTIVE:  atleta = Proactive(name=nome)
        else: break
        acad.athletes.append(atleta)

    print('Academia aberta')
    sleep(2.5)

    cont = 1
    # Iniciando treinos
    while True:
        system('cls')
        print(f'{f"{cont}° Simulação":^50}')
        print('-'*50)

        for atleta in acad.athletes:
            atleta.practice(acad.weight_rack)
        print('-'*50)

        for atleta in acad.athletes:
            atleta.rest(acad.weight_rack)
            sleep(0.5)
        print('-'*50)

        print('\n')
        print(acad)

        # Se a academia estiver muito desorganizada, há auto destruição
        organizados = 0
        for k,v in acad.weight_rack.items(): 
            if k == v: organizados+=1
        print(f'Restam {organizados} peso(s) em seu(s) respectivo(s) lugar(es)')
        
        if not organizados: 
            del(acad)
            break
        elif not bool(int(input('\nContinuar simulação? [0-Não | 1-Sim]:'))): break
        else: cont+=1
    else:
        system('cls') 
        print('Academia fechada')

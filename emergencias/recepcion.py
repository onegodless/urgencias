# -*- coding: latin-1 -*-
'''
Created on May 31, 2018

@author: Jes�s Molina
'''

import random

from faker import Faker

from pacientes import Pacientes
from cola_pacientes import ColaPacientes



class Recepcion(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.instancia_faker = Faker('en_GB')
    
    
    def generar_especialista(self,diccionario_medicos):
        '''
        Genera m�dicos y los a�ade a diccionario_medicos, asignado a cada m�dico una cola de la clase ColaPacientes.
        '''
        nombre_medico = self.instancia_faker.name() #Nombre de m�dicos generados con faker.
        diccionario_medicos[nombre_medico] = ColaPacientes()
    
    
    def nuevo_paciente(self):
        '''
        Llama a la clase pacientes para generar un nuevo paciente con datos aleatorios;
        '''
        instancia_pacientes = Pacientes()
        instancia_pacientes.generar_paciente() #genera un paciente con datos aleatorios.
        return instancia_pacientes
    
    
    def llegada_paciente(self):
        '''
        Determina de forma aleator�a si nuevo paciente llega a urgencias para ser atendido.
        '''
        chance = random.randint(1,4)
        if chance > 2: 
            paciente = self.nuevo_paciente()
            print "Un nuevo paciente " + str(paciente.getNombre()) + " entra en urgencias."
            print "Sus datos: " 
            print paciente  #Imprime los datos del paciente reci�n llegado invocado la funcion str de Paciente.
            print "\n"
            return paciente
    
    
    def asignar_medico(self,cola_vestibulo,diccionario_medicos):
        '''
        Asigna el primer paciente de la cola del vest�bulo a uno de los m�dicos libre, si no hay m�dicos libres se elige el m�dico de forma aleatoria.
        '''
        chance = random.randint(1,3) #1 en 4 posobilidades de que un paciente sea asignado a un m�dico.
        if chance <= 2:
            if cola_vestibulo.primero_cola(): #Si hay alg�n paciente en la cola del vest�bulo:
                paciente = cola_vestibulo.primero_cola()
                for medico in diccionario_medicos:
                    if len(diccionario_medicos[medico].lista_pacientes) == 0: #Comprueba si alguno de los m�dicos no tiene a algun paciente en su cola particular.
                        diccionario_medicos[medico].nuevo_paciente(paciente) #Se asigna el paciente a ese m�dico libre.
                        cola_vestibulo.proximo_paciente()
                        self.mostrar_asignacion_paciente_a_medico(medico,paciente.getNombre(),diccionario_medicos) #Muestra por pantalla la operaci�n.
                        return None
                    
                    ####Si no hay m�dico libre, el paciente se asignara a un m�dico al azar:

                    else:
                        lista_nombre_medicos = []
                
                        for key in diccionario_medicos:
                            lista_nombre_medicos.append(key) #llena la lista lista_nombre_medicos con los nombres de los m�dicos.
                        
                        indice_random = random.randint(0,len(lista_nombre_medicos)-1)
                        medico_random = lista_nombre_medicos[indice_random] #Se elige uno de los m�dicos al azar.
                    
                        diccionario_medicos[medico_random].nuevo_paciente(paciente)
                        cola_vestibulo.proximo_paciente()
                        self.mostrar_asignacion_paciente_a_medico(medico_random,paciente.getNombre(),diccionario_medicos) #Muestra por pantalla la operaci�n.
                        return None
        
    
    def mostrar_asignacion_paciente_a_medico(self,medico,paciente,diccionario_medicos):   
        '''
        Muestra por pantalla qu� paciente ha sido asignado a qu� m�dico.
        '''
        print "El paciente " + str(paciente) + " ha sido asignado al doctor " + str(medico) + ". \n" \
        + "Lista de pacientes esperando a ser atendidos por el Dr." + str(medico)  + ":" 
        for paciente in diccionario_medicos[medico].lista_pacientes:
            print paciente.getNombre()                  
           
        
    def print_cola(self,cola_vestibulo):
        '''
        Imprime los pacientes esperando en la sala de espera a ser atendidos por recepci�n.
        '''
        if len(cola_vestibulo.lista_pacientes) > 0:
            print "Lista de pacientes esperando a ser asignados a un m�dico: "
            for paciente in cola_vestibulo.lista_pacientes:
                if paciente:
                    print paciente.getNombre()
            print "\n"
        else:
            print "No hay pacientes esperando a ser atendidos por recepci�n."
            
            
    def medico_atiende_paciente(self,diccionario_medicos):
        '''
        Determina de forma aleatoria si los m�dicos curan al primer paciente de sus respectivas listas.
        '''
        chance = random.randint(1,6)
        for x in diccionario_medicos:
            if chance < 2:
                paciente_curado = diccionario_medicos[x].proximo_paciente()
                if paciente_curado:
                    print "El paciente " + str(paciente_curado.getNombre()) + " ha sido curado por el Dr." + str(x)
                    
    
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
        #self.instancia_cola = ColaPacientes() #Cola de pacientes en recepci�n.
        #self.diccionario_medicos = {} #Diccionario que contiene los m�dicos.
    
    
    def generar_especialista(self):
        '''
        Genera m�dicos y los a�ade a diccionario_medicos, asignado a cada m�dico una cola de la clase ColaPacientes.
        '''
        nombre_medico = self.instancia_faker.name() #Nombre de m�dicos generados con faker.
        self.diccionario_medicos[nombre_medico] = ColaPacientes() 
    
    
    def nuevo_paciente(self):
        '''
        Llama a la clase pacientes para generar un nuevo paciente con datos aleatorios;
        Llama a la clase cola_pacientes para encolar el nuevo paciente.
        '''
        instancia_pacientes = Pacientes()
        instancia_pacientes.generar_paciente() #genera un paciente con datos aleatorios.
        self.instancia_cola.nuevo_paciente(instancia_pacientes) #Encola al paciente en la cola de recepci�n.   
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
    
    
    def asignar_medico(self):
        '''
        Asigna el primer paciente de la cola del vest�bulo a uno de los m�dicos libre, si no hay m�dicos libres se elige el m�dico de forma aleatoria.
        '''
        chance = random.randint(1,4) #1 en 4 posobilidades de que un paciente sea asignado a un m�dico.
        if chance >= 2:
            paciente = self.instancia_cola.proximo_paciente() #Se asigna a la variable paciente el primer paciente de la cola en el vest�bulo.
            if paciente: #Si hay alg�n paciente en la cola del vest�bulo:
                for medico in self.diccionario_medicos:
                    if len(self.diccionario_medicos[medico].lista_pacientes) == 0: #Comprueba si alguno de los m�dicos no tiene a algun paciente en su cola particular.
                        self.diccionario_medicos[medico].nuevo_paciente(paciente) #Se asigna el paciente a ese m�dico libre.
                        self.mostrar_asignacion_paciente_a_medico(medico, paciente) #Muestra por pantalla la operaci�n.
                        return None
                    
                    ####Si no hay m�dico libre, el paciente se asignara a un m�dico al azar:

                    lista_nombre_medicos = []
                
                    for key in self.diccionario_medicos:
                        lista_nombre_medicos.append(key) #llena la lista lista_nombre_medicos con los nombres de los m�dicos.
                    
                    indice_random = random.randint(0,len(lista_nombre_medicos)-1)
                    medico_random = lista_nombre_medicos[indice_random] #Se elige uno de los m�dicos al azar.
                
                    self.diccionario_medicos[medico_random].nuevo_paciente(paciente)
                    self.mostrar_asignacion_paciente_a_medico(medico_random, paciente) #Muestra por pantalla la operaci�n.
                    return None
        
    
    def mostrar_asignacion_paciente_a_medico(self,medico,paciente):   
        '''
        Muestra por pantalla qu� paciente ha sido asignado a qu� m�dico.
        '''
        print "El paciente " + str(paciente.getNombre()) + " ha sido asignado al doctor " + str(medico) + ". \n" \
        + "Lista de pacientes esperando a ser atendidos por el Dr." + str(medico)  + ":" 
        for x in self.diccionario_medicos[medico].lista_pacientes:
            print x.getNombre()                   
           
        
    def print_cola(self):
        '''
        Imprime los pacientes esperando en la sala de espera a ser atendidos por recepci�n.
        '''
        if len(self.instancia_cola.lista_pacientes) > 0:
            print "Lista de pacientes esperando a ser asignados a un m�dico: "
            for x in self.instancia_cola.lista_pacientes:
                print x.getNombre()
            print "\n"
        else:
            print "No hay pacientes esperando a ser atendidos por recepci�n."
            
            
    def medico_atiende_paciente(self):
        '''
        Determina de forma aleatoria si los m�dicos curan al primer paciente de sus respectivas listas.
        '''
        chance = random.randint(1,4)
        for x in self.diccionario_medicos:
            if chance > 2:
                paciente_curado = self.diccionario_medicos[x].proximo_paciente()
                if paciente_curado:
                    print "El paciente " + str(paciente_curado.getNombre()) + " ha sido curado por el Dr." + str(x)
                    
    
    def devolver_lista_vestibulo(self):
        
        return self.instancia_cola.lista_pacientes
    
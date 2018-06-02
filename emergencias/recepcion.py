# -*- coding: latin-1 -*-
'''
Created on May 31, 2018

@author: Jesús Molina
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
        #self.instancia_cola = ColaPacientes() #Cola de pacientes en recepción.
        #self.diccionario_medicos = {} #Diccionario que contiene los médicos.
    
    
    def generar_especialista(self):
        '''
        Genera médicos y los añade a diccionario_medicos, asignado a cada médico una cola de la clase ColaPacientes.
        '''
        nombre_medico = self.instancia_faker.name() #Nombre de médicos generados con faker.
        self.diccionario_medicos[nombre_medico] = ColaPacientes() 
    
    
    def nuevo_paciente(self):
        '''
        Llama a la clase pacientes para generar un nuevo paciente con datos aleatorios;
        Llama a la clase cola_pacientes para encolar el nuevo paciente.
        '''
        instancia_pacientes = Pacientes()
        instancia_pacientes.generar_paciente() #genera un paciente con datos aleatorios.
        self.instancia_cola.nuevo_paciente(instancia_pacientes) #Encola al paciente en la cola de recepción.   
        return instancia_pacientes
    
    
    def llegada_paciente(self):
        '''
        Determina de forma aleatoría si nuevo paciente llega a urgencias para ser atendido.
        '''
        chance = random.randint(1,4)
        if chance > 2: 
            paciente = self.nuevo_paciente()
            print "Un nuevo paciente " + str(paciente.getNombre()) + " entra en urgencias."
            print "Sus datos: " 
            print paciente  #Imprime los datos del paciente recién llegado invocado la funcion str de Paciente.
            print "\n"
            return paciente
    
    
    def asignar_medico(self):
        '''
        Asigna el primer paciente de la cola del vestíbulo a uno de los médicos libre, si no hay médicos libres se elige el médico de forma aleatoria.
        '''
        chance = random.randint(1,4) #1 en 4 posobilidades de que un paciente sea asignado a un médico.
        if chance >= 2:
            paciente = self.instancia_cola.proximo_paciente() #Se asigna a la variable paciente el primer paciente de la cola en el vestíbulo.
            if paciente: #Si hay algún paciente en la cola del vestíbulo:
                for medico in self.diccionario_medicos:
                    if len(self.diccionario_medicos[medico].lista_pacientes) == 0: #Comprueba si alguno de los médicos no tiene a algun paciente en su cola particular.
                        self.diccionario_medicos[medico].nuevo_paciente(paciente) #Se asigna el paciente a ese médico libre.
                        self.mostrar_asignacion_paciente_a_medico(medico, paciente) #Muestra por pantalla la operación.
                        return None
                    
                    ####Si no hay médico libre, el paciente se asignara a un médico al azar:

                    lista_nombre_medicos = []
                
                    for key in self.diccionario_medicos:
                        lista_nombre_medicos.append(key) #llena la lista lista_nombre_medicos con los nombres de los médicos.
                    
                    indice_random = random.randint(0,len(lista_nombre_medicos)-1)
                    medico_random = lista_nombre_medicos[indice_random] #Se elige uno de los médicos al azar.
                
                    self.diccionario_medicos[medico_random].nuevo_paciente(paciente)
                    self.mostrar_asignacion_paciente_a_medico(medico_random, paciente) #Muestra por pantalla la operación.
                    return None
        
    
    def mostrar_asignacion_paciente_a_medico(self,medico,paciente):   
        '''
        Muestra por pantalla qué paciente ha sido asignado a qué médico.
        '''
        print "El paciente " + str(paciente.getNombre()) + " ha sido asignado al doctor " + str(medico) + ". \n" \
        + "Lista de pacientes esperando a ser atendidos por el Dr." + str(medico)  + ":" 
        for x in self.diccionario_medicos[medico].lista_pacientes:
            print x.getNombre()                   
           
        
    def print_cola(self):
        '''
        Imprime los pacientes esperando en la sala de espera a ser atendidos por recepción.
        '''
        if len(self.instancia_cola.lista_pacientes) > 0:
            print "Lista de pacientes esperando a ser asignados a un médico: "
            for x in self.instancia_cola.lista_pacientes:
                print x.getNombre()
            print "\n"
        else:
            print "No hay pacientes esperando a ser atendidos por recepción."
            
            
    def medico_atiende_paciente(self):
        '''
        Determina de forma aleatoria si los médicos curan al primer paciente de sus respectivas listas.
        '''
        chance = random.randint(1,4)
        for x in self.diccionario_medicos:
            if chance > 2:
                paciente_curado = self.diccionario_medicos[x].proximo_paciente()
                if paciente_curado:
                    print "El paciente " + str(paciente_curado.getNombre()) + " ha sido curado por el Dr." + str(x)
                    
    
    def devolver_lista_vestibulo(self):
        
        return self.instancia_cola.lista_pacientes
    
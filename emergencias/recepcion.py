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
        self.instancia_cola = ColaPacientes()
        self.diccionario_medicos = {}
    
    
    def __str__(self):
        
        for x in self.diccionario_medicos:
            print "Medico: " + str(x)
            print "Pacientes: "
            for y in self.diccionario_medicos[x]:
                print str(y)
                print "\n"
            print "\n"
        return ""
    
    def generar_especialista(self):
        '''
        Genera médicos y los añade al diccionario.
        '''
        nombre_medico = self.instancia_faker.name()
        self.diccionario_medicos[nombre_medico] = ColaPacientes()
    
    def nuevo_paciente(self):
        '''
        Llama a la clase pacientes para generar un nuevo paciente con datos aleatorios;
        Llama a la clase cola_pacientes para encolarlo.
        '''
        instancia_pacientes = Pacientes()
        instancia_pacientes.generar_paciente()
        self.instancia_cola.nuevo_paciente(instancia_pacientes)        
        return instancia_pacientes
    def asignar_medico(self):
        '''
        Genera una lista con todos los médicos disponibles y asigna el paciente a uno de 
        ellos de forma aleatoría.
        '''
        chance = random.randint(1,3)
        if chance >= 1:
            paciente = self.instancia_cola.proximo_paciente()
            if paciente:
                lista_nombre_medicos = []
                
                for key in self.diccionario_medicos:
                    lista_nombre_medicos.append(key)
                    
                indice_random = random.randint(0,len(lista_nombre_medicos)-1)
                medico_random = lista_nombre_medicos[indice_random]
                
                self.diccionario_medicos[medico_random].nuevo_paciente(paciente)
                print "El paciente " + str(paciente.getNombre()) + " ha sido asignado al médico " + str(medico_random) + ". \n" \
                    + "Lista de pacientes esperando a ser atendidos por el Dr." + str(medico_random)  + ": \n" 
                for x in self.diccionario_medicos[medico_random].lista_pacientes:
                    print x.getNombre()
                return medico_random
        
    
    def llegada_paciente(self):
        '''
        Determina de forma aleatoría si nuevo paciete llega a urgencias.
        '''
        chance = random.randint(0,5)
        if chance > 2: 
            paciente = self.nuevo_paciente()
            print "Un nuevo paciente " + str(paciente.getNombre()) + "entra en urgencias."
            return paciente
        
    
    def print_cola(self):
        
        if len(self.instancia_cola.lista_pacientes) > 0:
            print "Lista de pacientes esperando a ser asignados a un médico: "
            for x in self.instancia_cola.lista_pacientes:
                print x.getNombre()
            print "\n"
        else:
            print "No hay pacientes esperando a ser atendidos por recepción."

            
    def medico_atiende_paciente(self):
        chance = random.randint(0,5)
        if chance > 2: 
            for x in self.diccionario_medicos:
                paciente_curado = self.diccionario_medicos[x].proximo_paciente()
                if paciente_curado:
                    print "El paciente " + str(paciente_curado.getNombre()) + " ha sido curado por el Dr." + str(x)
    
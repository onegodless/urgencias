# -*- coding: latin-1 -*-
'''
Created on May 31, 2018

@author: Jesus Molina
'''

from faker import Faker
import random
from random import randint

class Pacientes(object):
    
    def __init__(self,nss=0,nombre="",edad=0,id_historial=0):
        
        self.__nss = nss
        self.__nombre = nombre
        self.__edad = edad
        self.__id_historial = id_historial
        self.instancia_faker = Faker('en_GB')
    
    
    def __str__(self):
        
        cadena = "Numero de la Seguridad Social: " + str(self.getIdHistorial()) \
        + "\n" \
        + "Nombre: " + str(self.getNombre()) \
        + "\n" \
        +"Edad: " + str(self.getEdad()) \
        + "\n" \
        +"Id Historial: " + str(self.getIdHistorial())
        return str(cadena) 
    
    #############Getters y Setters#######################
    def getNss(self):
        return self.__nss
    def setNss(self,nss):
        self.__nss = nss
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getEdad(self):
        return self.__edad
    def setEdad(self,edad):
        self.__edad = edad
    def getIdHistorial(self):
        return self.__id_historial
    def setIdHistorial(self,id_historial):
        self.__id_historial = id_historial
    ######################################################    
        
    def generar_paciente(self): #Generación automática de datos del paciente.
        
        self.setNss(self.instancia_faker.ssn())
        self.setNombre(self.instancia_faker.name())
        self.setEdad(random.randint(18,130))
        self.setIdHistorial(randint(1000,9999))  
        
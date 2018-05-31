# -*- coding: latin-1 -*-
'''
Created on May 31, 2018

@author: Jesús Molina
'''

from pacientes import Pacientes

class ColaPacientes(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.lista_pacientes = []
        
    
    def __str__(self):
        
        for x in self.lista_pacientes:
            
            cadena = "Numero de la Seguridad Social: " + str(x.getNss()) \
            + "\n" \
            + "Nombre: " + str(x.getNombre()) \
            + "\n" \
            +"Edad: " + str(x.getEdad()) \
            + "\n" \
            +"Id Historial: " + str(x.getIdHistorial()) \
            +"\n"
        
            print str(cadena) 
            
        return "" 
    
    def nuevo_paciente(self,paciente):
        '''
        La clase paciente genera un nuevo paciente y nuevo_paciente lo encola.
        '''
        self.lista_pacientes.append(paciente)
        
    def proximo_paciente(self):
        '''
        Se desencola el primer paciente de la cola.
        '''
        if len(self.lista_pacientes) > 0:
            paciente_saliente = self.lista_pacientes.pop(0)
            return paciente_saliente
        else:
            pass
        
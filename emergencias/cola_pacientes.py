# -*- coding: latin-1 -*-
'''
Created on May 31, 2018

@author: Jesús Molina
'''

class ColaPacientes(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.lista_pacientes = []
        
    
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
        
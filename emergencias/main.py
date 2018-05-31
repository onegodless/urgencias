# -*- coding: latin-1 -*-
'''
Created on May 31, 2018

@author: Jesús Molina
'''

import time

from faker import Faker

from recepcion import Recepcion

if __name__ == '__main__':
    
    instancia_faker = Faker()
    instancia_recepcion = Recepcion()
    #hora = instancia_faker.time(pattern="%H:%M", end_datetime=None)
    
    ########################################################
    
    for x in range(2):
        instancia_recepcion.generar_especialista()
    
    for x in range(5):
           
        instancia_recepcion.nuevo_paciente()
    
    #####################################################
    
    while True:
        
        instancia_recepcion.print_cola()
        instancia_recepcion.llegada_paciente()
        asignado_paciente = instancia_recepcion.asignar_medico()
        print "\n"
        instancia_recepcion.medico_atiende_paciente()
            
        time.sleep(2)
        
# -*- coding: latin-1 -*-
'''
Created on May 31, 2018

@author: Jesús Molina
'''

import time

from faker import Faker

from recepcion import Recepcion

if __name__ == '__main__':
    
    hora = 0
    instancia_faker = Faker()
    instancia_recepcion = Recepcion()    
    ########################################################
    
    for x in range(2):
        instancia_recepcion.generar_especialista()
    
    for x in range(5):
           
        instancia_recepcion.nuevo_paciente()
    
    #####################################################
    while True:
        
        print str(hora) + ":00"
        print "###########################"
        instancia_recepcion.print_cola()
        instancia_recepcion.llegada_paciente()
        instancia_recepcion.asignar_medico()
        instancia_recepcion.medico_atiende_paciente()
        time.sleep(3)
        hora += 1
        if hora > 23:
            hora = 0
        print "########################### \n"
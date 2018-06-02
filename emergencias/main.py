# -*- coding: latin-1 -*-
'''
Created on May 31, 2018

@author: Jesús Molina
'''

import time

from faker import Faker
import Tkinter as Tk

from recepcion import Recepcion
from cola_pacientes import ColaPacientes
from pacientes import Pacientes



if __name__ == '__main__':
    
    hora = 0
    instancia_faker = Faker()
    instancia_recepcion = Recepcion() 
    cola_vestibulo = ColaPacientes()   
    diccionario_medicos = {}
    ########################################################
    
    for x in range(2):
        
        instancia_recepcion.generar_especialista(diccionario_medicos)
    
    for x in range(5):
        
        instancia_paciente = Pacientes()
        instancia_paciente.generar_paciente()
        cola_vestibulo.nuevo_paciente(instancia_paciente)
    
    #####################################################
    while True:
         
        print str(hora) + ":00"
        print "###########################"
        instancia_recepcion.print_cola(cola_vestibulo)
        nuevo_paciente = instancia_recepcion.llegada_paciente()
        cola_vestibulo.nuevo_paciente(nuevo_paciente)
        instancia_recepcion.asignar_medico(cola_vestibulo,diccionario_medicos)
        instancia_recepcion.medico_atiende_paciente(diccionario_medicos)
        time.sleep(3)
        hora += 1
        if hora > 23:
            hora = 0
        print "########################### \n"
    
    '''
    ventana = Tk.Tk()
    
    vestibulo_label = Tk.Label(ventana, text="Lista de pacientes en la sala de espera:")
    vestibulo_label.grid(row=0, column=0)
    lista_vestibulo = instancia_recepcion.devolver_lista_vestibulo()
    
    diccionario_botones = {}
    posicion_boton = 0
    for paciente in lista_vestibulo:
        
        diccionario_botones[paciente.getNombre] = Tk.Button(ventana, text=paciente.getNombre())
        diccionario_botones[paciente.getNombre].grid(row=1, column=posicion_boton, command=)
        posicion_boton += 1

    Tk.ainloop()
    '''
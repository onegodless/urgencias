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

hora = 0
instancia_faker = Faker()
instancia_recepcion = Recepcion() 
cola_vestibulo = ColaPacientes()   
diccionario_medicos = {}


def enlazar_boton_con_paciente(paciente):
    
    datos_pacientes = Tk.StringVar()
    datos_pacientes.set(paciente)
    label_datos = Tk.Label(ventana,textvar=datos_pacientes)
    label_datos.grid(row=2, column=0)


def main_loop():

    #print str(hora) + ":00"
    print "###########################"
    instancia_recepcion.print_cola(cola_vestibulo)
    nuevo_paciente = instancia_recepcion.llegada_paciente()
    cola_vestibulo.nuevo_paciente(nuevo_paciente)
    instancia_recepcion.asignar_medico(cola_vestibulo,diccionario_medicos)
    instancia_recepcion.medico_atiende_paciente(diccionario_medicos)
    time.sleep(3)
    #hora += 1
    #if hora > 23:
        #hora = 0
    print "########################### \n"
    return

if __name__ == '__main__':
    
    ########################################################
    
    for x in range(2):
        
        instancia_recepcion.generar_especialista(diccionario_medicos)
    
    for x in range(8):
        
        instancia_paciente = Pacientes()
        instancia_paciente.generar_paciente()
        cola_vestibulo.nuevo_paciente(instancia_paciente)
    
    #####################################################
    '''
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
    
    
        
    lista_vestibulo = cola_vestibulo.lista_pacientes     
    diccionario_botones = {}         
    
    ventana = Tk.Tk()

    datos_pacientes = Tk.StringVar()
    
    vestibulo_label = Tk.Label(ventana, text="Lista de pacientes en la sala de espera:")     
    vestibulo_label.grid(row=0, column=0)
    
    posicion_boton = 0
    
    for paciente in lista_vestibulo:
        
        diccionario_botones[paciente.getNombre()] = Tk.Button(ventana, text=paciente.getNombre(),command = lambda aux=paciente: enlazar_boton_con_paciente(aux)).grid(row=1, column=posicion_boton)
        posicion_boton += 1
        
    label_datos = Tk.Label(ventana,textvar=datos_pacientes)
    label_datos.grid(row=2, column=0)
    
    label_medicos_titulo = Tk.Label(ventana,text="Los médicos en servicio son: ").grid(row=3, column=0)
    posicion_boton = 0
    
    for medico in diccionario_medicos:
        
        Tk.Label(ventana,text=str(medico)).grid(row=4, column=posicion_boton)
        Tk.Label(ventana,text="Pacientes de este médico: ").grid(row=5, column=posicion_boton)
        posicion_boton += 1
    
    posicion_boton = 0
    
    for medico in diccionario_medicos:
        for paciente in diccionario_medicos[medico].lista_pacientes:
            Tk.Button(ventana,text=paciente.getNombre(),command = lambda aux=paciente: enlazar_boton_con_paciente(aux)).grid(row=1, column=posicion_boton)
            posicion_boton += 1
    
    main_loop()
    Tk.mainloop()
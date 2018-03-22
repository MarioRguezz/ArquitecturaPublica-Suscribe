#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: simulador.py
# Capitulo: 3 Patrón Publica-Subscribe
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 2.0.1 Mayo 2017
# Descripción:
#
#   Esta clase define el rol de un set-up, es decir, simular el funcionamiento de los wearables del caso de estudio.
#
#   Las características de ésta clase son las siguientes:
#
#                                          simulador.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Iniciar el entorno   |  - Define el id inicial|
#           |        set-up         |    de simulación.       |    a partir del cuál se|
#           |                       |                         |    iniciarán los weara-|
#           |                       |                         |    bles.               |
#           +-----------------------+-------------------------+------------------------+
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                               Métodos:
#           +-------------------------+--------------------------+-----------------------+
#           |         Nombre          |        Parámetros        |        Función        |
#           +-------------------------+--------------------------+-----------------------+
#           |                         |                          |  - Inicializa los     |
#           |                         |                          |    publicadores       |
#           |     set_up_sensors()    |          Ninguno         |    necesarios para co-|
#           |                         |                          |    menzar la simula-  |
#           |                         |                          |    ción.              |
#           +-------------------------+--------------------------+-----------------------+
#           |                         |                          |  - Ejecuta el método  |
#           |                         |                          |    publish de cada    |
#           |     start_sensors()     |          Ninguno         |    sensor para publi- |
#           |                         |                          |    car los signos vi- |
#           |                         |                          |    tales.             |
#           +----------------------------------------------------------------------------
#           |set_up_lista_medicamentos|                          | - Da información de la|
#          |                          |         Ninguno          |   medicina disponible |
#           +-------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
import sys
import progressbar
from time import sleep
sys.path.append('publicadores')
from xiaomi_my_band import XiaomiMyBand
from temporizador import Temporizador
from pyfiglet import figlet_format
from medicamento import Medicamento
from prettytable import PrettyTable
import random
import threading
import time


class Simulador:
    sensores = []
    id_inicial = 39722608
    lista_medicamento = []
    personas_grupo = []





    def set_up_sensors(self):
        print('cargando')
        self.draw_progress_bar(10)
        print(figlet_format('Bienvenido'))
        print('Tarea 1: arquitecturas Publica - Suscribe')
        print('Cargando simulador')
        self.draw_progress_bar(20)
        print('+---------------------------------------------+')
        print('|        CONFIGURACIÓN DE LA SIMULACIÓN       |')
        print('+---------------------------------------------+')
        adultos_mayores = raw_input('|ingresa el número de adultos mayores: ')
        print('+---------------------------------------------+')
        raw_input('presiona enter para continuar: ')
        print('+---------------------------------------------+')
        print('|            ASIGNACIÓN DE SENSORES           |')
        print('+---------------------------------------------+')
        for x in xrange(0, int(adultos_mayores)):
            s = XiaomiMyBand(self.id_inicial)
            self.sensores.append(s)
            print('| wearable Xiaomi My Band asignado, id: ' + str(self.id_inicial))
            print('+---------------------------------------------+')
            self.id_inicial += 1
        for element in self.sensores:
            self.personas_grupo.append([element.id, random.randint(0, 6)])
        print('+---------------------------------------------+')
        print('|        LISTO PARA INICIAR SIMULACIÓN            |')
        print('+---------------------------------------------+')
        print('')
        print('*Nota: Se enviarán 1000 mensajes como parte de la simulación')
        raw_input('presiona enter para iniciar: ')
        thread_temporizador = threading.Thread(target=self.start_temporizador)
        thread_temporizador.daemon = True
        thread_sensores = threading.Thread(target=self.start_sensors)
        thread_sensores.daemon = True
        thread_temporizador.start()
        thread_sensores.start()
        while True:
            time.sleep(1)
    def start_sensors(self):
        for x in xrange(0, 1):
            for s in self.sensores:
                s.publish()

    def start_temporizador(self):
        t = Temporizador(self.lista_medicamento, self.personas_grupo)
        t.publish()


    def draw_progress_bar(self, value):
        bar = progressbar.ProgressBar(maxval=value, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        for i in xrange(value):
            bar.update(i+1)
            sleep(0.2)
        bar.finish()


    def set_up_lista_medicamentos(self):
        self.lista_medicamento.append(Medicamento(1,"paracetamol","15:30","1 pastilla"))
        self.lista_medicamento.append(Medicamento(2,"ibuprofeno","16:30","10 miligramos"))
        self.lista_medicamento.append(Medicamento(3,"insulina","17:30","10 mililitros"))
        self.lista_medicamento.append(Medicamento(4,"furosemida","18:30","15 miligramos"))
        self.lista_medicamento.append(Medicamento(5,"piroxicam","19:30", "10 miligramos"))
        self.lista_medicamento.append(Medicamento(6,"tolbutamida","1:02","20 mililitros"))
        table = PrettyTable([
            'Medicamentos ID',
            'Nombre',
            'Horario',
            'Dosis'
        ])
        for element in self.lista_medicamento:
            table.add_row([element.id_medicamento, element.nombre, element.horario, element.dosis])
        print("Medicamentos disponibles")
        print(table)

   

if __name__ == '__main__':
    simulador = Simulador()
    simulador.set_up_lista_medicamentos()
    simulador.set_up_sensors()

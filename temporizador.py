#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: temporizador.py
# Capitulo: 3 Patrón Publica-Subscribe
# Autor(es): Equipo AlFeLuMa.
# Version: 2.0.3 Marzo 2018
# Descripción:
#
#   Esta clase define temporizador que se estara ejecutando para saber la dosis de medicamento
#
#   Las características de ésta clase son las siguientes:
#
#                                          temporizador.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |- Inicia el temporizador |- Define las condiciones|
#           |        Producer       |    y su configuración.  |    para asignar        |
#           |                       |                         |    medicina            |
#           |                       |                         |                        |
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
#           |      |          Ninguno         |    necesarios para co-|
#           |                         |                          |    menzar la simula-  |
#           |                         |                          |    ción.              |
#           +-------------------------+--------------------------+-----------------------+
#           |                         |                          |  - Ejecuta el método  |
#           |                         |                          |    publish de cada    |
#           |        |          Ninguno         |    sensor para publi- |
#           |                         |                          |    car los signos vi- |
#           |                         |                          |    tales.             |
#           +-------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------

import pika
import random
import progressbar
import schedule
import time
class Temporizador:
    producer = "Temporizador"
    personas_grupo = []
    lista_medicamento = []
    
    def __init__(self, lista_medicamento, personas_grupo):
        self.lista_medicamento = lista_medicamento
        self.personas_grupo = personas_grupo

    def publish(self):
        for x in xrange(0,len(self.lista_medicamento)):
            schedule.every(1).minutes.do(job)
            schedule.every().day.at(self.lista_medicamento[x].horario).do(job)

        while True:
            schedule.run_pending()
            time.sleep(1)

def job():
        #Aqui se publica
        print("I'm working...") 
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
#           |                         |                          |  - compara la hora    |
#           |                         |                          | del medicamento con   |
#           |      |      Publish     |     ninguno              | la hora actual y si
#           |                         |                          | coincide ejecuta una  |
#           |                         |                          |   acción              |
#           +-------------------------+--------------------------+-----------------------+
#           |                         |                          |  - muestra el id de   |
#           |                         |          grupo           | los ancianos que      |
#           |        |     job        |     medicamento          | necesitan la medicina |
#           |                         |         id               | la medicina y el grupo|
#           |                         |                          |                       |
#           +-------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------

import pika
import random
import progressbar
import schedule
import time
class Temporizador:
    personas_grupo = []
    lista_medicamento = []
    
    def __init__(self, lista_medicamento, personas_grupo):
        self.lista_medicamento = lista_medicamento
        self.personas_grupo = personas_grupo

    def publish(self):
        for grupo in xrange(0,len(self.lista_medicamento)):
            schedule.every(1).minutes.do(job)
            schedule.every().day.at(self.lista_medicamento[grupo].horario).do(job,self.lista_medicamento[grupo].nombre,self.personas_grupo, grupo )

        while True:
            schedule.run_pending()
            time.sleep(1)

def job(medicamento, grupo, id):
        n = str(id)
        for x in xrange(0,len(grupo)): 
           if id == grupo[x][1]:
            y = str( grupo[x][0])
            print("El id de cada anciano del grupo es"+ y)
        print("La medicina que se debe tomar ahorita es "+ medicamento + " del grupo de adultos mayores "+ n   ) 
       
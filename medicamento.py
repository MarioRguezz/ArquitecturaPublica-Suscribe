#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: medicamento.py
# Capitulo: 3 Patrón Publica-Subscribe
# Autor(es): Equipo AlFeLuMa.
# Version: 2.0.3 Marzo 2018
# Descripción:
#
#   Esta clase define un objeto del tipo medicamento
#
#   Las características de ésta clase son las siguientes:
#   Permite el manejo de medicamentos además de dejar escalabilidad para el posterior uso de CRUD
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                               Métodos:
#           +-------------------------+--------------------------+-----------------------+
#           |         Nombre          |        Parámetros        |        Función        |
#           +-------------------------+--------------------------+-----------------------+
#           |                         |                          |  - Inicializa un      |
#           |                         |                          |    medicamento        |
#           |     Constructor()       |          Ninguno         |                       |
#           |                         |                          |                       |
#           |                         |                          |                       |
#           +-------------------------+--------------------------+-----------------------+
#           |                         |                          |  - Genera un medicame |
#           |                         |   dosis                  |    nto cargado        |
#           |  Constructor_cargado()  |   id medicamento         |                       |
#           |                         |   nombre                 |                       |
#           |                         |   horario                |                       |
#           +-------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------

class Medicamento():
    id_medicamento = 0
    nombre = ""
    horario = ""
    
    def __init__(self):
        pass

    def __init__(self, id_medicamento, nombre, horario, dosis):
        self.id_medicamento = id_medicamento
        self.nombre = nombre
        self.horario = horario
        self.dosis = dosis

    
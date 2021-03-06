# Arquitecturas Publica - Suscribe

## Tarea 1

### Prerequisitos

Antes de ejecutar el código de la tarea 1 se requiere instales [RabbitMQ](https://www.rabbitmq.com/download.html).

### Ejecutar simulador de la tarea 1

La tarea 1 cuenta con un simulador que ofrece una situación más realista acerca de una arquitectura Publica - Suscribe. Para ejecutar el simulador y los monitores sigue los siguientes pasos.  
1. Abrir terminal.  
2. Clonar el repositorio:   `git clone https://github.com/MarioRguezz/ArquitecturaPublica-Suscribe.git`  
3. Ingresar a la carpeta que descargamos:   `cd Arquitecturas-Publica-Suscribe/`
4. Instalar las librerías de python del archivo [requirements.txt]
```
sudo pip install -r requirements.txt
```
5. Ejecutar el simulador: `python simulador.py`  
6. Ejecutar los monitores de los sensores:
```
python suscriptores/procesador_de_posicion.py
python suscriptores/procesador_de_presion.py
python suscriptores/procesador_de_ritmo_cardiaco.py
python suscriptores/procesador_de_temperatura.py
```

El simulador implementa una versión funcional del Sistema de Monitore de Adultos Mayores (SMAM). A continuación se muestra un diagrama de contenedores del SMAM.

![Diagrama de contenedores del SMAM](imagenes/diagrama.png)

## Versión

2.0.3 - Marzo 2018

## Autores

* **Alfredo Sánchez Martínez**
* **José Fernando González Herrera**
* **Luis Antonio Ibarra González**
* **Mario Alberto Negrete Rodríguez**

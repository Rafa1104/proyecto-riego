#import RPi.GPIO as GPIO
import time
from datetime import date, datetime
import os


class Riego:  
  def lectura_sensor(self):
    
      tierra = 1    # Sensor de Tierra: Tierra seca 1 - Tierra humeda = 0
      estacion = 1  # Estacion de año: verano = 1, invierno = 0
      agua = 0      # Sensor de la Reserva: Reserva llena 0 - Reserva vacia = 1

      return(tierra, agua, estacion)

  def control_riego(self, tierra, dias, agua, estacion):

        # s = tierra
        # r = estacion
        # d = dia noche
        # v = agua
        
        fechaActual = datetime.now()
        fechaActualFormato = datetime.strftime(fechaActual, '%d/%m/%Y %H:%M:%S')

        estado = ""
        
        if tierra == 1: # seca
            if estacion == 1: # Verano
                if agua == 0: # lleno
                    #GPIO.output(32, GPIO.HIGH)
                    estado = "BOMBA ACTIVADA"
                else:
                  
                    #GPIO.output(32, GPIO.LOW)
                    print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")

            else:

                if agua == 1: # Reserva vacia
                    print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")
                    estado = "BOMBA DESACTIVADA"
                    #GPIO.output(32, GPIO.LOW)


                else:
                  
                    if agua == 0:  # lleno
                        #GPIO.output(32, GPIO.HIGH)
                        estado = "BOMBA ACTIVADA"


                    else:
                        print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")
                        estado = "BOMBA DESACTIVADA"
                        #GPIO.output(32, GPIO.LOW)

        else:
          
            print("-NO NECESITA RIEGO-")
            if estacion == 1: # Verano
                if agua == 1: # Reserva vacia
                    print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")

            else:
              
                if agua == 1: # Reserva vacia
                    print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")
            estado = "BOMBA DESACTIVADA"
            #GPIO.output(32, GPIO.LOW)

            
        if dias == 3:
            #GPIO.output(32, GPIO.HIGH)
            print("-Dia 3, la bomba siempre se activa")
            #GPIO.output(32, GPIO.HIGH)
            estado = "BOMBA ACTIVADA"
            if agua == 1: # Reserva vacia
                  print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")
                  #GPIO.output(32, GPIO.LOW)
                  estado = "BOMBA DESACTIVADA"

        return(fechaActualFormato, estado)




riego = Riego()


dias = 0

##for i in range(3): dias +=1
##
##  print("Dia: ", dias)
##  print("***************************************")
##  tierra, agua, estacion = riego.lectura_sensor()
##  fechaActualFormato, estado = riego.control_riego(tierra, dias, agua, estacion)
##  print("\n", fechaActualFormato, "\n", estado , "\n")
##  print("***************************************\n")
##  if dias == 3:
##    dias = 0
##  time.sleep(3)

tierra, agua, estacion = riego.lectura_sensor()
fechaActualFormato, estado = riego.control_riego(tierra, dias, agua, estacion)

data = {'Hora': fechaActualFormato, 'Tierra': tierra, 'Agua': agua, 'Estacion': estacion, 'Estado': estado}
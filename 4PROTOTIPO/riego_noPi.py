#import RPi.GPIO as GPIO
import time
import os

##GPIO.setmode(GPIO.BOARD)
##
##GPIO.setup(8, GPIO.IN)  # Dias (incrementa los dias, si llega a 3 se activa)
##GPIO.setup(24, GPIO.IN)  # Tierra
##GPIO.setup(26, GPIO.IN)  # Reserva
##GPIO.setup(28, GPIO.IN)  # Estacion
##
##GPIO.setup(32, GPIO.OUT)  # Bomba

# 1: Seca
# 2: Humeda
# 3: Dias = 3
# 4: Dias < 3
# 5: Con agua
# 6: Sin agua
# 7: Verano
# 8: Invierno

##class Riego:
##  
##  def lectura_sensor(self):
##    tierra = 0
##    agua = 0
##    estacion = 0
##    return(tierra, agua, estacion)
##
##        # Sensor de Tierra: Tierra seca 1 - Tierra humeda = 0
##        if GPIO.input(24) == 1:
##            tierra = 1
##        else:
##            tierra = 0
##
##        # Sensor de la Reserva: Reserva llena 0 - Reserva vacia = 1
##        if GPIO.input(26) == 1:
##            agua = 1
##        else:
##            agua = 0
##
##        # Estacion de año: verano = 1, invierno = 0
##        if GPIO.input(28) == 1:
##            estacion = 1
##        else:
##            estacion = 0
##        return(tierra, agua, estacion)

class Riego:  
  def lectura_sensor(self):
    
      tierra = 1    # Sensor de Tierra: Tierra seca 1 - Tierra humeda = 0
      agua = 1      # Sensor de la Reserva: Reserva llena 0 - Reserva vacia = 1
      estacion = 0  # Estacion de año: verano = 1, invierno = 0
      return(tierra, agua, estacion)

  def control_riego(self, tierra, dias, agua, estacion):

        # s = tierra
        # r = estacion
        # d = dia noche
        # v = agua

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

        return(estado)




riego = Riego()
dias = 0

##for i in range(2):
##  dias +=1
##
##  print("Dia: ", dias)
##  print("***************************************")
##  tierra, agua, estacion = riego.lectura_sensor()
##  print("\n", riego.control_riego(tierra, dias, agua, estacion), "\n")
##  print("***************************************\n")
##  if dias == 3:
##    dias = 0
##  time.sleep(3)


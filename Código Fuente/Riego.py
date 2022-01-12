import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.IN) # Dias (incrementa los dias, si llega a 3 se hace el riego)
#GPIO.setup(22, GPIO.IN) # Sensor de Humedad de Riego
GPIO.setup(24, GPIO.IN) # Tierra
GPIO.setup(26, GPIO.IN) # Reserva
GPIO.setup(28, GPIO.IN) # Estacion
#GPIO.setup(8, GPIO.IN) # Dias
 
GPIO.setup(32, GPIO.OUT) #Bomba


Class Riego:
  
  def lectura_sensor(self):
    
    # Sensor de Tierra: Tierra seca 1 - Tierra humeda = 0
    if GPIO.input(24) == 1:
      tierra = 1
    else:
      tierra = 0
      
    # Sensor de la Reserva: Reserva llena 1 - Reserva vacia = 0
    if GPIO.input(26) == 1:
      agua = 1
    else:
      agua = 0
    
    return(tierra, agua)

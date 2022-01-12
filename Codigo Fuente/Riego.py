import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.IN) # Dias (incrementa los dias, si llega a 3 se hace el riego)
#GPIO.setup(22, GPIO.IN) # Sensor de Humedad de Riego
GPIO.setup(24, GPIO.IN) # Humedad
GPIO.setup(26, GPIO.IN) # Reserva
GPIO.setup(28, GPIO.IN) # Estacion
#GPIO.setup(8, GPIO.IN) # Dias
 
GPIO.setup(32, GPIO.OUT) #Bomba



#Class Riego:
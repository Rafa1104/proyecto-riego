import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.IN)  # Dias (incrementa los dias, si llega a 3 se activa)
GPIO.setup(24, GPIO.IN)  # Tierra
GPIO.setup(26, GPIO.IN)  # Reserva
GPIO.setup(28, GPIO.IN)  # Estacion

GPIO.setup(32, GPIO.OUT)  # Bomba

# 1: Seca
# 2: Humeda
# 3: Dias = 3
# 4: Dias < 3
# 5: Con agua
# 6: Sin agua

class Riego:
  def lectura_sensor(self):

        # Sensor de Tierra: Tierra seca 1 - Tierra humeda = 0
        if GPIO.input(24) == 1:
            tierra = 1
        else:
            tierra = 0

        # Sensor de la Reserva: Reserva llena 0 - Reserva vacia = 1
        if GPIO.input(26) == 1:
            agua = 1
        else:
            agua = 0

        # Estacion de año: verano = 1, invierno = 0
        if GPIO.input(28) == 1:
            estacion = 1
        else:
            estacion = 0
        return(tierra, agua, estacion)


  def control_riego(self, tierra, agua, estacion):

        # s = tierra
        # r = estacion
        # d = dia noche
        # v = agua
        # 5: Con agua
        # 6: Sin agua

        estado = ""

        if tierra == 1:
            if estacion == 1:
                if agua == 0:
                    print("\n")
                    print("Activando Bomba...")
                    GPIO.output(32, GPIO.HIGH)
                    estado = "BOMBA ACTIVADA"
                    print("\n" + "***************************")
                    print("\n")
                else:
                    GPIO.output(32, GPIO.LOW)
                    print("\n")
                    print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")

            else:

                if agua == 1:
                    print("\n")
                    print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")
                    estado = "BOMBA DESACTIVADA"
                    GPIO.output(32, GPIO.LOW)
                    print("\n" + "***************************")
                    print("\n")

                else:
                    if agua == 0:  # lleno
                        print("\n")
                        print("Activando Bomba...")
                        GPIO.output(32, GPIO.HIGH)
                        estado = "BOMBA ACTIVADA"
                        print("\n" + "***************************")
                        print("\n")

                    else:
                        print("\n")
                        print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")
                        estado = "BOMBA DESACTIVADA"
                        GPIO.output(32, GPIO.LOW)
                        print("\n" + "***************************")
                        print("\n")

        else:
            print("\n" + "-NO NECESITA RIEGO-")
            if estacion == 1:
                if agua == 1:
                    print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")

            else:
                if agua == 1:
                    print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")
            estado = "BOMBA DESACTIVADA"
            GPIO.output(32, GPIO.LOW)
            print("\n" + "***************************")
            print("\n")

        return(estado)




riego = Riego()

while True:

  tierra, agua, estacion = riego.lectura_sensor()
  riego.control_riego(tierra, agua, estacion)
  time.sleep(15)

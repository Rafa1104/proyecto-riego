import unittest

from riego_copy import Riego as riego

#import mycode
# 1: Seca
# 2: Humeda
# 3: Dias = 3
# 4: Dias < 3
# 5: Con agua
# 6: Sin agua
# 7: Verano
# 8: Invierno

# Sensor de Tierra: Tierra seca 1 - Tierra humeda = 0
# Sensor de la Reserva: Reserva llena 0 - Reserva vacia = 1
# Estacion de año: verano = 1, invierno = 0

class TestRiego(unittest.TestCase):

    def test_caso_1(self):
      
      #estado =""
                #riego.control_riego(tierra, dias, agua, estacion)
                # 1 - 4 - 5 - 8
      estado = riego.control_riego(self, 1, 1, 0, 0)
      self.assertEqual(estado, "BOMBA ACTIVADA")

if __name__ == '__main__':
    unittest.main()

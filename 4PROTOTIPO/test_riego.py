import unittest

from riego_noPi import Riego as riego

#import mycode
# 1: Seca
# 2: Humeda
# 3: Dias = 3
# 4: Dias < 3
# 5: Con agua
# 6: Sin agua
# 7: Verano
# 8: Invierno

# Tierra seca 1 - Tierra humeda = 0
# Reserva llena 0 - Reserva vacia = 1
# verano = 1, invierno = 0

class TestRiego(unittest.TestCase):

    def test_caso_1 (self):
        estado = ""
                #riego.control_riego(self, tierra, dias, agua, estacion)
                # 1 - 4 - 5 - 8 dias:2
        estado = riego.control_riego(self, 1, 1, 0, 0)
        self.assertEqual(estado, "BOMBA ACTIVADA")

    def test_caso_2 (self):
        estado =""
                #riego.control_riego(self, tierra, dias, agua, estacion)
                # 1 - 4 - 5 - 7     dias:2
        estado = riego.control_riego(self, 1, 1, 0, 1)
        self.assertEqual(estado, "BOMBA ACTIVADA")
        
    def test_caso_3 (self):
        estado =""
                #riego.control_riego(self, tierra, dias, agua, estacion)
                # 1 - 4 - 5     dias:2
        estado = riego.control_riego(self, 1, 2, 0, 0)
        self.assertEqual(estado, "BOMBA ACTIVADA")

    def test_caso_4 (self):
        estado =""
                #riego.control_riego(self, tierra, dias, agua, estacion)
                # 2 - 4 - 5     dias:1
        estado = riego.control_riego(self, 0, 2, 0, 0)
        self.assertEqual(estado, "BOMBA DESACTIVADA")

    def test_caso_5 (self):
        estado =""
                #riego.control_riego(self, tierra, dias, agua, estacion)
                # 5 - 3     dias:3
        estado = riego.control_riego(self, 0, 3, 0, 0)
        self.assertEqual(estado, "BOMBA ACTIVADA")
        
    def test_caso_6 (self):
        estado =""
                #riego.control_riego(self, tierra, dias, agua, estacion)
                # 6     dias:0
        estado = riego.control_riego(self, 0, 0, 1, 0)
        self.assertEqual(estado, "BOMBA DESACTIVADA")
        

if __name__ == '__main__':
    unittest.main()

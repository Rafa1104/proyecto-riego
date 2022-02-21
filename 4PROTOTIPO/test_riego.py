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
                        # CASO 1: 1-4-5-8 [dias:1]
        tierra = 1      # 1: Seca
        dias = 0        # 4: Dias < 3 -> Dias:1
        agua = 0        # 5: Con agua
        estacion = 0    # 8: Invierno

        print("Dia: ", dias)
        print("***************************************")
        fechaActualFormato, estado = riego.control_riego(self, tierra, dias, agua, estacion)
        print("\n", fechaActualFormato, "\n", estado, "\n")
        print("***************************************\n")
        
        self.assertEqual(estado, "BOMBA ACTIVADA")
        self.assertTrue(fechaActualFormato)
        
##SEGUNDO ESCENARIO DE POSIBILIDADES
    def test_caso_1_1 (self):
        estado = ""
                        # CASO 1: 1-4-5-8 [dias:1]
        tierra = 1      # 1: Seca
        dias = 1        # 4: Dias < 3 -> Dias:1
        agua = 1        # 5: Con agua
        estacion = 1    # 8: Invierno

        print("Dia: ", dias)
        print("***************************************")
        fechaActualFormato, estado = riego.control_riego(self, tierra, dias, agua, estacion)
        print("\n", fechaActualFormato, "\n", estado, "\n")
        print("***************************************\n")
        
        self.assertEqual(estado, "-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")
        self.assertTrue(fechaActualFormato)

    def test_caso_2 (self):
        estado =""
                        # CASO 2: 1-4-5-7 [dias:1]
        tierra = 0      # 1: Seca
        dias = 3        # 4: Dias < 3 -> Dias:1
        agua = 0        # 5: Con agua
        estacion = 0    # 7: Verano

        print("Dia: ", dias)
        print("***************************************")
        fechaActualFormato, estado = riego.control_riego(self, tierra, dias, agua, estacion)
        print("\n", fechaActualFormato, "\n", estado, "\n")
        print("***************************************\n")
        
        self.assertEqual(estado, "BOMBA ACTIVADA")
        self.assertTrue(fechaActualFormato)
        
##SEGUNDO ESCENARIO DE POSIBILIDADES
    def test_caso_2_1 (self):
        estado =""
                        # CASO 2: 1-4-5-7 [dias:1]
        tierra = 0      # 1: Seca
        dias = 2        # 4: Dias < 3 -> Dias:1
        agua = 0        # 5: Con agua
        estacion = 0    # 7: Verano

        print("Dia: ", dias)
        print("***************************************")
        fechaActualFormato, estado = riego.control_riego(self, tierra, dias, agua, estacion)
        print("\n", fechaActualFormato, "\n", estado, "\n")
        print("***************************************\n")
        
        self.assertEqual(estado, "BOMBA DESACTIVADA")
        self.assertTrue(fechaActualFormato)

##TERCER ESCENARIO DE POSIBILIDADES
    def test_caso_2_2 (self):
        estado =""
                        # CASO 2: 1-4-5-7 [dias:1]
        tierra = 0      # 1: Seca
        dias = 1        # 4: Dias < 3 -> Dias:1
        agua = 0        # 5: Con agua
        estacion = 0    # 7: Verano

        print("Dia: ", dias)
        print("***************************************")
        fechaActualFormato, estado = riego.control_riego(self, tierra, dias, agua, estacion)
        print("\n", fechaActualFormato, "\n", estado, "\n")
        print("***************************************\n")
        
        self.assertEqual(estado, "BOMBA DESACTIVADA")
        self.assertTrue(fechaActualFormato)
        
        
    def test_caso_3 (self):
        estado =""
                        # CASO 3: 1-4-5 [dias:2]
        tierra = 1      # 1: Seca
        dias = 2        # 4: Dias < 3 -> Dias:2
        agua = 0        # 5: Con agua
        estacion = 0    # 8: Invierno

        print("Dia: ", dias)
        print("***************************************")
        fechaActualFormato, estado = riego.control_riego(self, tierra, dias, agua, estacion)
        print("\n", fechaActualFormato, "\n", estado, "\n")
        print("***************************************\n")
        
        self.assertEqual(estado, "BOMBA ACTIVADA")
        self.assertTrue(fechaActualFormato)
        
##SEGUNDO ESCENARIO DE POSIBILIDADES
    def test_caso_3_1 (self):
        estado =""
                        # CASO 3: 1-4-5 [dias:2]
        tierra = 0      # 1: Seca
        dias = 0        # 4: Dias < 3 -> Dias:2
        agua = 0        # 5: Con agua
        estacion = 0    # 8: Invierno

        print("Dia: ", dias)
        print("***************************************")
        fechaActualFormato, estado = riego.control_riego(self, tierra, dias, agua, estacion)
        print("\n", fechaActualFormato, "\n", estado, "\n")
        print("***************************************\n")
        
        self.assertEqual(estado, "BOMBA DESACTIVADA")
        self.assertTrue(fechaActualFormato)

    def test_caso_4 (self):
        estado =""
                        # CASO 4: 2-4-5 [dias:1]
        tierra = 0      # 2: Humeda
        dias = 1        # 4: Dias < 3 -> Dias:1
        agua = 0        # 5: Con agua
        estacion = 1    # 8: Invierno
        
        print("Dia: ", dias)
        print("***************************************")
        fechaActualFormato, estado = riego.control_riego(self, tierra, dias, agua, estacion)
        print("\n", fechaActualFormato, "\n", estado, "\n")
        print("***************************************\n")
        
        self.assertNotEqual(estado, "BOMBA ACTIVADA POR LA MAÑANA")
        self.assertTrue(fechaActualFormato)
        
##SEGUNDO ESCENARIO DE POSIBILIDADES
    def test_caso_4_1 (self):
        estado =""
                        # CASO 4: 2-4-5 [dias:1]
        tierra = 0      # 2: Humeda
        dias = 1        # 4: Dias < 3 -> Dias:1
        agua = 0        # 5: Con agua
        estacion = 0    # 8: Invierno
        
        print("Dia: ", dias)
        print("***************************************")
        fechaActualFormato, estado = riego.control_riego(self, tierra, dias, agua, estacion)
        print("\n", fechaActualFormato, "\n", estado, "\n")
        print("***************************************\n")
        
        self.assertNotEqual(estado, "BOMBA ACTIVADA POR LA NOCHE")
        self.assertTrue(fechaActualFormato)

##    def test_caso_5 (self):
##        estado =""
##                        # CASO 5: 3-5 [dias:3]
##        tierra = 1      # 1: Seca
##        dias = 3        # 3: Dias = 3 
##        agua = 0        # 5: Con agua
##        estacion = 0    # 8: Invierno
        
        
##        print("Dia: ", dias)
##        print("***************************************")
##        fechaActualFormato, estado = riego.control_riego(self, tierra, dias, agua, estacion)
##        print("\n", fechaActualFormato, "\n", estado, "\n")
##        print("***************************************\n")
        
##        self.assertEqual(estado, "BOMBA ACTIVADA")
##        self.assertTrue(fechaActualFormato)
        
##    def test_caso_6 (self):
##        estado =""
##                        # CASO 6: 6 [dias:0]
##        tierra = 0      # 1: Seca
##        dias = 0        # 4: Dias < 3 -> Dias:0
##        agua = 1        # 6: Sin agua
##        estacion = 0    # 8: Invierno
        
##        print("Dia: ", dias)
##        print("***************************************")
##        fechaActualFormato, estado = riego.control_riego(self, tierra, dias, agua, estacion)
##        print("\n", fechaActualFormato, "\n", estado, "\n")
##        print("***************************************\n")
##        self.assertEqual(estado, "BOMBA DESACTIVADA")
        
    
        

if __name__ == '__main__':
    unittest.main()

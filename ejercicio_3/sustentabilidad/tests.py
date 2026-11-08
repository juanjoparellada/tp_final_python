import unittest
from .services import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_nominal_default(self):
        """Valida la exactitud númerica del cálculo de emisiones."""
        resultado = calcular_emisiones_carbono(100)
        self.assertEqual(resultado, 40.0)

    def test_calculo_factor_personalizado(self):
        """Valida la exactitud númerica del cálculo de emisiones con un factor personalizado."""
        resultado = calcular_emisiones_carbono(250, factor_emision=0.5)
        self.assertEqual(resultado, 125)

    def test_consumo_cero(self):
        """Valida el cálculo de emisiones para consumo cero."""
        resultado = calcular_emisiones_carbono(0)
        self.assertEqual(resultado, 0)

    def test_consumo_negativo(self):
        """Valida que se levante ValueError si el consumo es negativo."""
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-15.5)

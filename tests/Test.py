import sys
import os
dir = os.path.dirname(os.path.dirname(__file__))
print(dir)
sys.path.append(r''+dir)
import unittest
from unittest import mock
from unittest.mock import patch
from application.tistory import checkRegEx, nameChanger, generar_cadena, playStory
from application.tistory import gic, S
from application.tistory import estados_perdedores,dfa, estados_ganadores, estados_aceptacion, gic ,q0


class storyTests(unittest.TestCase):

    def testRegEx(self):
        regex = rf"\buber\b"
        self.assertTrue(checkRegEx(regex,"Buscar uber"))

        regex = rf"\bamigo"
        self.assertFalse(checkRegEx(regex,"Irte con fiestero"))

    @mock.patch('builtins.input', side_effect=["Luis", "a", "Buscar transporte", "esperar un cupo", "dormir en el cupo", "caminar hasta casa", "no"])
    def test_run(self, input):
        # You can leave this line for capturing the output, but don't call playStory here.
        output = playStory(dfa, q0, estados_ganadores, estados_aceptacion, estados_perdedores, gic)

        expected_output = "A_3_3_Caminar"

        self.assertEqual(output, expected_output)

    def testGrammar(self):
        grammar_phrases = [
        "un gato juega sobre un juguete",
        "un gato juega bajo un juguete",
        "un gato juega cerca de un juguete",
        "un gato juega junto a un juguete",
        "un gato juega con un juguete",
        "un gato juega sobre un arbol",
        "un gato juega bajo un arbol",
        "un gato juega cerca de un arbol",
        "un gato juega junto a un arbol",
        "un gato juega con un arbol",
        "un gato juega sobre un carro",
        "un gato juega bajo un carro",
        "un gato juega cerca de un carro",
        "un gato juega junto a un carro",
        "un gato juega con un carro",
        "un gato juega sobre un juguete",
        "un gato juega bajo un juguete",
        "un gato juega cerca de un juguete",
        "un gato juega junto a un juguete",
        "un gato juega con un juguete",
        "un gato juega sobre un arbol",
        "un gato juega bajo un arbol",
        "un gato juega cerca de un arbol",
        "un gato juega junto a un arbol",
        "un gato juega con un arbol",
        "un gato juega sobre un carro",
        "un gato juega bajo un carro",
        "un gato juega cerca de un carro",
        "un gato juega junto a un carro",
        "un gato juega con un carro",
        "un gato corre sobre un juguete",
        "un gato corre bajo un juguete",
        "un gato corre cerca de un juguete",
        "un gato corre junto a un juguete",
        "un gato corre con un juguete",
        "un gato corre bajo un arbol",
        "un gato corre cerca de un arbol",
        "un gato corre junto a un arbol",
        "un gato corre con un arbol",
        "un gato corre sobre un carro",
        "un gato corre bajo un carro",
        "un gato corre cerca de un carro",
        "un gato corre junto a un carro",
        "un gato corre con un carro",
        "un gato duerme sobre un juguete",
        "un gato duerme bajo un juguete",
        "un gato duerme cerca de un juguete",
        "un gato duerme junto a un juguete",
        "un gato duerme con un juguete",
        "un gato duerme sobre un arbol",
        "un gato duerme bajo un arbol",
        "un gato duerme cerca de un arbol",
        "un gato duerme junto a un arbol",
        "un gato duerme con un arbol",
        "un gato duerme sobre un carro",
        "un gato duerme bajo un carro",
        "un gato duerme cerca de un carro",
        "un gato duerme junto a un carro",
        "un gato duerme con un carro",
        "un gato salta sobre un juguete",
        "un gato salta bajo un juguete",
        "un gato salta cerca de un juguete",
        "un gato salta junto a un juguete",
        "un gato salta con un juguete",
        "un gato salta sobre un arbol",
        "un gato salta bajo un arbol",
        "un gato salta cerca de un arbol",
        "un gato salta junto a un arbol",
        "un gato salta con un arbol",
        "un gato salta sobre un carro",
        "un gato salta bajo un carro",
        "un gato salta cerca de un carro",
        "un gato salta junto a un carro",
        "un gato salta con un carro",
        "un gato juega sobre un balon",
        "un gato juega bajo un balon",
        "un gato juega cerca de un balon",
        "un gato juega junto a un balon",
        "un gato juega con un balon",
        "un gato corre sobre un balon",
        "un gato corre bajo un balon",
        "un gato corre cerca de un balon",
        "un gato corre junto a un balon",
        "un gato corre con un balon",
        "un gato duerme sobre un botellon",
        "un gato duerme bajo un botellon",
        "un gato duerme cerca de un botellon",
        "un gato duerme junto a un botellon",
        "un gato duerme con un botellon",
        "un gato salta sobre un botellon",
        "un gato salta bajo un botellon",
        "un gato salta cerca de un botellon",
        "un gato salta junto a un botellon",
        "un gato salta con un botellon",
        "un gato juega sobre un colchon",
        "un gato juega bajo un colchon",
        "un gato juega cerca de un colchon",
        "un gato juega junto a un colchon",
        "un gato juega con un colchon",
        "un gato corre sobre un colchon",
        "un gato corre bajo un colchon",
        "un gato corre cerca de un colchon",
        "un gato corre junto a un colchon",
        "un gato corre con un colchon",
        "un gato duerme sobre un colchon",
        "un gato duerme bajo un colchon",
        "un gato duerme cerca de un colchon",
        "un gato duerme junto a un colchon",
        "un gato duerme con un colchon",
        "un gato salta sobre un colchon",
        "un gato salta bajo un colchon",
        "un gato salta cerca de un colchon",
        "un gato salta junto a un colchon",
        "un gato salta con un colchon",
        "un gato duerme bajo un botellon",
        "un gato duerme cerca de un botellon",
        "un gato duerme junto a un botellon",
        "un gato duerme con un botellon",
        "un gato salta sobre un botellon",
        "un gato salta bajo un botellon",
        "un gato salta cerca de un botellon",
        "un gato salta junto a un botellon",
        "un gato salta con un botellon",
        "un gato juega sobre un botellon",
        "un gato juega bajo un botellon",
        "un gato juega cerca de un botellon",
        "un gato juega junto a un botellon",
        "un gato juega con un botellon",
        "un gato corre sobre un botellon",
        "un gato corre bajo un botellon",
        "un gato corre cerca de un botellon",
        "un gato corre junto a un botellon",
        "un gato corre con un botellon",
        "un gato duerme sobre un colchon",
        "un gato duerme bajo un colchon",
        "un gato duerme cerca de un colchon",
        "un gato duerme junto a un colchon",
        "un gato duerme con un colchon",
        "un gato salta sobre un colchon",
        "un gato salta bajo un colchon",
        "un gato salta cerca de un colchon",
        "un gato salta junto a un colchon",
        "un gato salta con un colchon",
        "un niño juega sobre un juguete",
        "un niño juega bajo un juguete",
        "un niño juega cerca de un juguete",
        "un niño juega junto a un juguete",
        "un niño juega con un juguete",
        "un niño juega sobre un arbol",
        "un niño juega bajo un arbol",
        "un niño juega cerca de un arbol",
        "un niño juega junto a un arbol",
        "un niño juega con un arbol",
        "un niño juega sobre un carro",
        "un niño juega bajo un carro",
        "un niño juega cerca de un carro",
        "un niño juega junto a un carro",
        "un niño juega con un carro",
        "un niño corre sobre un juguete",
        "un niño corre bajo un juguete",
        "un niño corre cerca de un juguete",
        "un niño corre junto a un juguete",
        "un niño corre con un juguete",
        "un niño corre sobre un arbol",
        "un niño corre bajo un arbol",
        "un niño corre cerca de un arbol",
        "un niño corre junto a un arbol",
        "un niño corre con un arbol",
        "un niño corre sobre un carro",
        "un niño corre bajo un carro",
        "un niño corre cerca de un carro",
        "un niño corre junto a un carro",
        "un niño corre con un carro",
        "un niño duerme sobre un juguete",
        "un niño duerme bajo un juguete",
        "un niño duerme cerca de un juguete",
        "un niño duerme junto a un juguete",
        "un niño duerme con un juguete",
        "un niño duerme sobre un arbol",
        "un niño duerme bajo un arbol",
        "un niño duerme cerca de un arbol",
        "un niño duerme junto a un arbol",
        "un niño duerme con un arbol",
        "un niño duerme sobre un carro",
        "un niño duerme bajo un carro",
        "un niño duerme cerca de un carro",
        "un niño duerme junto a un carro",
        "un niño duerme con un carro",
        "un niño salta sobre un balon",
        "un niño salta bajo un balon",
        "un niño salta cerca de un balon",
        "un niño salta junto a un balon",
        "un niño salta con un balon",
        "un niño salta sobre un botellon",
        "un niño salta bajo un botellon",
        "un niño salta cerca de un botellon",
        "un niño salta junto a un botellon",
        "un niño salta con un botellon",
        "un niño juega sobre un colchon",
        "un niño juega bajo un colchon",
        "un niño juega cerca de un colchon",
        "un niño juega junto a un colchon",
        "un niño juega con un colchon",
        "un niño corre sobre un colchon",
        "un niño corre bajo un colchon",
        "un niño corre cerca de un colchon",
        "un niño corre junto a un colchon",
        "un niño corre con un colchon",
        "un niño duerme sobre un colchon",
        "un niño duerme bajo un colchon",
        "un niño duerme cerca de un colchon",
        "un niño duerme junto a un colchon",
        "un niño duerme con un colchon",
        "un niño salta sobre un colchon",
        "un niño salta bajo un colchon",
        "un niño salta cerca de un colchon",
        "un niño salta junto a un colchon",
        "un niño salta con un colchon",
        "un niño duerme bajo un botellon",
        "un niño duerme cerca de un botellon",
        "un niño duerme junto a un botellon",
        "un niño duerme con un botellon",
        "un niño salta sobre un botellon",
        "un niño salta bajo un botellon",
        "un niño salta cerca de un botellon",
        "un niño salta junto a un botellon",
        "un niño salta con un botellon",
        "un niño juega sobre un botellon",
        "un niño juega bajo un botellon",
        "un niño juega cerca de un botellon",
        "un niño juega junto a un botellon",
        "un niño juega con un botellon",
        "un niño corre sobre un botellon",
        "un niño corre bajo un botellon",
        "un niño corre cerca de un botellon",
        "un niño corre junto a un botellon",
        "un niño corre con un botellon",
        "un niño duerme sobre un colchon",
        "un niño duerme bajo un colchon",
        "un niño duerme cerca de un colchon",
        "un niño duerme junto a un colchon",
        "un niño duerme con un colchon",
        "un niño salta sobre un colchon",
        "un niño salta bajo un colchon",
        "un niño salta cerca de un colchon",
        "un niño salta junto a un colchon",
        "un niño salta con un colchon"]

        self.assertIn("un gato salta sobre un colchon", grammar_phrases)
        self.assertFalse("Un tigre corre sobre un avion" in grammar_phrases)

    def testTranducer(self):
        result = nameChanger("Luis","jugador123456789101112131415161718192021222324252627282930")
        
        self.assertEqual(result, "Luis")

        result = nameChanger("Juan","jugador123456789101112131415161718192021222324252627282930")
        
        self.assertEqual(result, "Juan")

if __name__== '__main__':
    unittest.main()
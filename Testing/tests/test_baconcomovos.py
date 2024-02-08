'''
TDD - Test Driven Development (Desenvolvimento Orientado a Testes)

Red
Parte 1 - Criar o teste e ver falhar

Green
Parte 2 - Criar o código e ver o teste passar

Refactor
Parte 3 - Melhorar meu código
'''
import unittest
from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertionerror_caso_nao_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')

    def test_bacon_com_ovos_mostra_bacon_com_ovos_numero_multiplo_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'{entrada} não retornou "{saida}"'
                )

    def test_bacon_com_ovos_mostra_passar_fome_numero_nao_multiplo_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'{entrada} não retornou "{saida}"'
                )

    def test_bacon_com_ovos_mostra_bacon_numero_multiplo_apenas_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'{entrada} não retornou "{saida}"'
                )

    def test_bacon_com_ovos_mostra_ovos_numero_multiplo_apenas_de_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'{entrada} não retornou "{saida}"'
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)

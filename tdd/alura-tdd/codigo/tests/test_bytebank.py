import pytest
from pytest import mark
import sys
sys.path.append("/Users/daianeklein/Documents/DS/python-development/tdd/alura-tdd/codigo")
from bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        #given-context
        entrada = '13/03/2000'
        esperado = 22

        funcionario_test = Funcionario('teste', entrada, 1159)

        #when-acao
        resultado = funcionario_test.idade()

        #then-desfecho
        assert resultado == esperado


    def test_quando_sobrenome_recebe_lucas_Carvalho_deve_retornar_apenas_carvalho(self):
        entrada = ' Lucas Carvalho ' #given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 20183)
        
        resultado = lucas.sobrenome() #when
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_10000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()

        resultado = funcionario_teste.salario
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('test', '11/11/2000', entrada)

        resultado = funcionario_teste.calcular_bonus()
        assert resultado == esperado
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000

            funcionario_teste = Funcionario('test', '11/11/2000', entrada)

            resultado = funcionario_teste.calcular_bonus()
            assert resultado


    def test_retorno_str(self):
        nome, data_nascimento, salario = 'Test', '13/09/2000', 1000
        esperado = 'Funcionario(Test, 13/09/2000, 1000)'

        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__()
        
        assert resultado == esperado

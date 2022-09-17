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

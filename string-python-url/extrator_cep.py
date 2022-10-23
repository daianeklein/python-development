import re

endereco = 'rua das laranjeiras, 514, bairro flores, Rio de Janeiro, RJ, 23440-010'

#padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
#padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")
#padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") #hifen pode aparecer de 0 a 1 vez


busca = padrao.search(endereco) #match

if busca:
    cep = busca.group()
    print(cep)
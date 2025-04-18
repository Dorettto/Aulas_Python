PH = float(input('Digite o valor do PH: '))
Resposta = ''

if PH < 6.0:
    Resposta = 'ácida' 
elif PH < 7.0:
    Resposta = 'levemente ácida'
elif PH == 7.0:
    Resposta = 'neutra'
elif PH < 8.0:
    Resposta = 'levemente alcalina'
else:
    Resposta = 'alcalina'

print(f'Se o PH é {PH}, então a solução é {Resposta}.\n')
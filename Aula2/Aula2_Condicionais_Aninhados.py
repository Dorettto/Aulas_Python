Valor = float(input('Insira o valor: '))
Risco = input('Digite BX(baixo) ou AL(alto), em relação ao risco: \n')
Tipo = ''

if Risco != 'BX' and Risco != 'AL':
    print(f'{Risco} é um valor inválido para grau de risco.\n')
else:
    if Risco == 'BX':
        if Valor < 1000.00:
            Tipo = 'poupança'
        else:
            Tipo = 'renda fixa' 
    else:
        if Valor < 1000.00:
            Tipo = 'bitcoins'
        else:
            Tipo = 'ações'

    print(f'Considerando o risco {Risco} e o valor {Valor}, você deve investir em {Tipo}.\n')
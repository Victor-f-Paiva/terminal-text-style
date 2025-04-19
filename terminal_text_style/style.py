'''
O código para mudar cores padrão é \033...\033[m
Estilo de fonte: 0(none); 1(bold); 4(underline); 7(negative/troca cor de fundo com a fonte)
texto: 30(branco) 31(vermelho); 32(verde); 33(amarelo); 34(azul); 35(roxo); 36(anil); 37(cinza)
fundo: 40(branco) 41(vermelho); 42(verde); 43(amarelo); 44(azul); 45(roxo); 46(anil); 47(cinza)

nome = 'Victor'
print(f'Hello, \033[4;33;44m{nome}\033[m!!!')
'''

def cor(type, text, back, message):
    estilo = {'bold' : 1, 'italic' : 3, 'underline' : 4, 'negative': 7}
    fonte = {'branco' : 30, 'vermelho' : 31, 'verde' : 32, 'amarelo' : 33, 'azul' : 34,
    'roxo' : 35, 'ciano' : 36, 'cinza' : 37}
    fundo = {'preto' : 40, 'vermelho' : 41, 'verde' : 42, 'amarelo' : 43, 'azul' : 44,
    'roxo' : 45, 'ciano' : 46, 'cinza' : 47}
    return f'\033[{estilo[type]};{fonte[text]};{fundo[back]}m{message}\033[m'

if __name__ == '__main__':
    print(cor('italic', 'ciano', 'roxo', 'Olá, mundo!'))
    print(cor(text='verde', message='Abacaxi com goiaba')) #deu erro
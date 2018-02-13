from random import randint
from time import sleep

repetir = True
dado_ataque = []
dado_defesa = []
tropas_perdidas_atacante = 0
tropas_perdidas_defensor = 0

while repetir:
    ataque = int(input('\nQuantas tropas atacantes? '))
    defesa = int(input('Quantas tropas defensoras? '))
    sleep(1)

    if 0 < ataque <= 3 and 0 < defesa <= 3:
        for i in range(0, ataque): #Sorteando os valores dos dados do jogador atacante
            dado_ataque.append(randint(1,6))

        for i1 in range(0, defesa): #Sorteando os valores dos dados do jogador defensor
            dado_defesa.append(randint(1,6))

        dado_ataque = sorted(dado_ataque, reverse=True) #Ordenando do maior para o menor os valores do atacante
        dado_defesa = sorted(dado_defesa, reverse=True) #Ordenando do maior para o menor os valores do defensor

        lista = sorted([len(dado_defesa), len(dado_ataque)]) # Criando uma lista e ordenando pelo jogador que tem menos tropas

        for i2 in range(0, lista[0]): # Varrendo os dados no tamanho do jogador que tem menos tropas, pois quem tem mais não vai usar o/os menor/menores valor(es)
            if dado_ataque[i2] > dado_defesa[i2]:
                tropas_perdidas_defensor += 1
            else:
                tropas_perdidas_atacante += 1

        print('\nAtacante tirou: {}'.format(dado_ataque))
        sleep(1)
        print('Defensor tirou: {}'.format(dado_defesa))
        sleep(1)

        print('\nO Atacante perdeu {} tropa(s)'.format(tropas_perdidas_atacante))
        sleep(1)
        print('O Defensor perdeu {} tropa(s)'.format(tropas_perdidas_defensor))
        sleep(1)

    else:
        print('O valor de tropas atacantes e/ou defensoras está fora do intervalo permitido!')
        sleep(1)

    dado_ataque = []
    dado_defesa = []
    tropas_perdidas_atacante = 0
    tropas_perdidas_defensor = 0
    repeticao = input('\nQuer jogar novamente? [S para Sim ou qualquer tecla para sair!] ').upper().strip()

    if repeticao != 'S':
        print('Obrigado por jogar!')
        repetir = False









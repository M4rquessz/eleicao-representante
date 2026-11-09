#Projeto - Sistema de eleição para a representância

va=0
vb=0
vc=0
vw=0
r1=0
vt=0
win=0

while r1!=6:
    print('===== ELEIÇÃO DO REPRESENTANTE =====\n')
    print('1 - Votar em Ana')
    print('2 - Votar em Bruno')
    print('3 - Votar em Carlos ')
    print('4 - Votar em branco ')
    print('5 - Consultar resultado parcial ')
    print('6 - Encerrar votação\n')

    r1=int(input('Escolha uma opção: \n'))

    if r1==1:
        va=va+1
        print('Voto em Ana registrado!')
        vt=vt+1
        if va == vb:
            print(f'Agora Ana está empatada com Bruno, com {va} votos!')
        if va == vc:
            print(f'Agora Ana está empatada com Carlos, com {va} votos!')

    elif r1==2:
        vb=vb+1
        print('Voto em Bruno registrado!')
        vt = vt + 1
        if vb == va:
            print(f'Agora Bruno está empatado com Ana, com {vb} votos!')
        if vb == vc:
            print(f'Agora Bruno está empatado com Carlos, com {vb} votos!')

    elif r1==3:
        vc=vc+1
        print('Voto em Carlos registrado!')
        vt = vt + 1
        if vc == va:
            print(f'Agora Carlos está empatado com Ana, com {vc} votos!')
        if vc == vb:
            print(f'Agora Carlos está empatado com Bruno, com {vc} votos!')

    elif r1==4:
        vw=vw+1
        print('Voto em branco registrado!')
        vt = vt + 1

    elif r1==5:
        print(f'Até o momento, os resultados da eleição são: {va} votos em Ana, {vb} votos em Bruno, {vc} votos em Carlos e {vw} votos em branco.')
        print(f'Totalizando {vt} votos no total.')

    elif r1==6:
        print('===== RESULTADO FINAL =====\n')
        print(f'A votação terminou em: {va} votos em Ana, {vb} votos em Bruno, {vc} votos em Carlos e {vw} votos em branco. Totalizando {vt} votos.\n')

        if va > vb and va>vc:
            win='Ana'
            print(f'Sendo assim, o vencedor(a) é: {win}!')
            if vw>va or va==vw:
                print(f'Sendo assim, o vencedor(a) é: {win}!')

        elif vb > va and vb>vc:
            win='Bruno'
            print(f'Sendo assim, o vencedor(a) é: {win}!')
            if vw>vb or vb==vw:
                print(f'Sendo assim, o vencedor(a) é: {win}!')

        elif vc > va and vc>vb:
            win='Carlos'
            print(f'Sendo assim, o vencedor(a) é: {win}!')
            if vw>vc or vc==vw:
                print(f'Sendo assim, o vencedor(a) é: {win}!')

        elif vb == 0 and va == 0 and vc == 0 and vw>0:
            print('A eleição acabou com todos os votos em Branco.')

        elif va==vb and va !=0 and vb!=0:
            print(f'Houve um empate na eleição entre Ana e Bruno!')

        elif va==vc and va !=0 and vc!=0:
            print(f'Houve um empate na eleição entre Ana e Carlos!')

        elif vc==vb and vc !=0 and vb!=0:
            print(f'Houve um empate na eleição entre Carlos e Bruno!')

        else:
            print('Não houve nenhum voto registrado, ou ocorreu um erro na eleição... desligando programa.')
            break

        print('Finalizando programa...')

    else:
        print('Digite um número listado!')


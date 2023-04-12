
from time import sleep



peças_escolhidas = []
nomepecas = []
carrinho = []
carrinho.append(nomepecas)

def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(f'{txt}'.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro valido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuario preferiu não informar o número.\033[m')
        else:
            return n

def menuprocessador():
    processadoresamd = {'[1]RYZEN 5600X': 800,
                        '[2]RYZEN 5600 ': 720,
                        '[3]RYZEN 5600G ': 649.71,
                        '[4]RYZEN 5500  ': 479.66}
    processadoresintel = {'[1]Intel core I9-11900K': 4900,
                          '[2]Intel Core i9-10900K': 3860,
                          '[3]Intel Core i7-11700K': 4400,
                          '[4]Intel Core i3-10100 ': 1900,
                          '[5]Intel core i5-3470 ': 300}

    while True:
        print('\033[33mMARCA DO PROCESSADOR\n'
              '[1]AMD\n'
              '[2]INTEL')
        print(linha())
        amd_ou_intel = leiaInt('\033[97mSelecione a marca: \033[m')
        print(linha())

        while amd_ou_intel != 1 and amd_ou_intel != 2:
            print('ERRO! por favor digite um número inteiro valido!')
            amd_ou_intel = leiaInt('\033[97mSelecione a marca: \033[m')

        if amd_ou_intel == 1:
            print('\033[97;40mPROCESSADORES AMD DISPONIVEIS:\033[m')
            for item, preco in processadoresamd.items():
                print(f'\033[97m{item}:\033[m', end='')
                print(f'\033[97mR${preco}\033[m'.center(26))
            print('\033[97m[5]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('\033[97mDigite uma opção: \033[m')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('\033[97mDigite uma opção: \033[m')

            if opcao == 1:
                peças_escolhidas.append(processadoresamd['[1]RYZEN 5600X'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("RYZEN 5600X: R$800")
            if opcao == 2:
                peças_escolhidas.append(processadoresamd['[2]RYZEN 5600 '])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("RYZEN 5600: R$720")
            if opcao == 3:
                peças_escolhidas.append(processadoresamd['[3]RYZEN 5600G '])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("RYZEN 5600G: R$649.71")
            if opcao == 4:
                peças_escolhidas.append(processadoresamd['[4]RYZEN 5500  '])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("RYZEN 5500 R$479.66")
            if opcao == 5:
                return inicio()

            print(linha())
            return inicio()

        if amd_ou_intel == 2:
            print(linha())
            print('\033[97;40mPROCESSADORES INTEL DISPONIVEIS:\033[m')
            for item, preco in processadoresintel.items():
                print(f'\033[97m{item}:\033[m', end='')
                print(f'\033[97mR${preco}\033[m'.rjust(18))
            print('\033[97m[6]VOLTAR AO INICIO\033[m')
            opcao = leiaInt('Digite uma opção: ')
            print(linha())
            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')
                print(linha())
            if opcao == 1:
                peças_escolhidas.append(processadoresintel['[1]Intel core I9-11900K'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Intel core I9-11900K: R$4900")
            if opcao == 2:
                peças_escolhidas.append(processadoresintel['[2]Intel Core i9-10900K'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Intel core I9-10900K: R$3860")
            if opcao == 3:
                peças_escolhidas.append(processadoresintel['[3]Intel Core i7-11700K'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Intel core I7-11700K: R$4400")
            if opcao == 4:
                peças_escolhidas.append(processadoresintel['[4]Intel Core i3-10100 '])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Intel core I3-10100: R$1900")
            if opcao == 5:
                peças_escolhidas.append(processadoresintel['[5]Intel core i5-3470 '])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Intel core I5-3470: R$300")
            if opcao == 6:
                return inicio()

            print(linha())
            return inicio()

def menuplacaMae():
    placamaeasus = {'[1]ASUS ROG Maximus XIII Hero:': 3500,
                    '[2]ASUS Prime Z590-A:': 1500,
                    '[3]ASUS ROG Strix Z590-E Gaming WiFi:': 2250,
                    '[4]ASUS Prime B550M-A:': 739,
                    '[5]ASUS tuf gaming b550m-plus:': 1878}

    placamaeamd = {'[1]Gigabyte AORUS B550 Pro AC:': 1000,
                   '[2]ASUS TUF Gaming X570-PRO (Wi-Fi):': 1450,
                   '[3]ASUS ROG Crosshair VIII Hero:': 2300,
                   '[4]MSI B450 Tomahawk MAX:': 600,
                   '[5]ASUS Prime B550M-A:': 700}
    while True:
        print(f'\033[33mMARCA DA PLACA MÃE\n'
              '[1]ASUS\n'
              '[2]AMD\n\033[m')

        print(linha())
        amd_ou_asus = leiaInt('\033[97mSelecione a marca: \033[m')
        print(linha())

        while amd_ou_asus != 1 and amd_ou_asus != 2:
            print('\033[31mERRO! por favor digite um número inteiro valido!\033[m')
            amd_ou_asus = leiaInt('\033[97mSelecione a marca: \033[m')

        if amd_ou_asus == 1:
            print('\033[97mPLACAS MÃES DISPONIVEIS\033[m')
            for item, preco in placamaeasus.items():
                print(f'\033[97m{item:<38}\033[m', end='')
                print(f'\033[97mR${preco}\033[m')
            print('\033[97m[6]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('\033[97mDigite o codigo do pedido: \033[m')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('\033[97mDigite o codigo do pedido: \033[m')

            if opcao == 1:
                peças_escolhidas.append(placamaeasus['[1]ASUS ROG Maximus XIII Hero:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("ASUS ROG Maximus XIII Hero: R$3500")
            if opcao == 2:
                peças_escolhidas.append(placamaeasus['[2]ASUS Prime Z590-A:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("ASUS Prime Z590-A: R$1500")
            if opcao == 3:
                peças_escolhidas.append(placamaeasus['[3]ASUS ROG Strix Z590-E Gaming WiFi:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("ASUS ROG Strix Z590-E Gaming WiFi: R$2250")
            if opcao == 4:
                peças_escolhidas.append(placamaeasus['[4]ASUS Prime B550M-A:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("ASUS Prime B550-A: R$739")
            if opcao == 5:
                peças_escolhidas.append(placamaeasus['[5]ASUS tuf gaming b550m-plus:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("ASUS tuf gaming b550m-plus: R$1878")
            if opcao == 6:
                return inicio()

            print(linha())
            return inicio()

        if amd_ou_asus == 2:
            print('\033[97;40mPLACAS MÃES DISPONIVEIS\033[m')
            for item, preco in placamaeamd.items():
                print(f'\033[97m{item:<38}\033[m', end='')
                print(f'\033[97mR${preco}\033[m'.rjust(18))
            print('\033[97m[6]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('\033[97mDigite o codigo do pedido: \033[m')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('\033[97mDigite uma opção: \033[m')

            if opcao == 1:
                peças_escolhidas.append(placamaeamd['[1]Gigabyte AORUS B550 Pro AC:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Gigabyte AORUS B550 Pro AC: R$1000")
            if opcao == 2:
                peças_escolhidas.append(placamaeamd['[2]ASUS TUF Gaming X570-PRO (Wi-Fi):'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("ASUS TUF Gaming X570-PRO (Wi-Fi): R$1450")
            if opcao == 3:
                peças_escolhidas.append(placamaeamd['[3]ASUS ROG Crosshair VIII Hero:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("ASUS ROG Crosshair VIII Hero: R$2300")
            if opcao == 4:
                peças_escolhidas.append(placamaeamd['[4]MSI B450 Tomahawk MAX:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("MSI B450 Tomahawk MAX: R$600")
            if opcao == 5:
                peças_escolhidas.append(placamaeamd['[5]ASUS Prime B550M-A:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("ASUS Prime B550M-A: R$700")
            if opcao == 6:
                return inicio()

            print(linha())
            return inicio()

def menumemoriaram():
    memoria_ram_asgard = {'[1]Memoria Ram ASGARD 8gb 3200MHz': 180,
                          '[2]Memoria Ram ASGARD 16gb 3200MHz': 300,
                          '[3]Memoria Ram ASGARD 32gb 3200MHz': 500}
    memoria_ram_corsair = {'[1]Memoria Ram Corsair 8gb 3600MHz': 150,
                           '[2]Memoria Ram Corsair 16gb 3600MHz': 300,
                           '[3]Memoria Ram Corsair 3600MHz': 566}
    memoria_ram_hyperx = {'[1]Memoria Ram HyperX 8b 2666MHz': 170,
                          '[2]Memoria Ram HyperX 16gb 3200MHz': 300,
                          '[3]Memoria Ram HyperX 32gb 3600Mhz': 688}
    while True:
        print('\033[33mMARCA DA MEMORIA RAM\n'
              '[1]ASGARD\n'
              '[2]CORSAIR\n'
              '[3]HYPERX\033[m')

        print(linha())
        asgard_corsair_hyperx = leiaInt('\033[97mSelecione a marca: \033[m')
        print(linha())

        while asgard_corsair_hyperx != 1 and asgard_corsair_hyperx != 2 and asgard_corsair_hyperx != 3:
            print('ERRO! por favor digite um número inteiro valido!')
            asgard_corsair_hyperx = leiaInt('\033[97mSelecione a marca: \033[m')

        if asgard_corsair_hyperx == 1:
            print('\033[97;40mMEMORIAS RAM ASGARD DISPONVEIS\033[m')
            for item, preco in memoria_ram_asgard.items():
                print(f'\033[97m{item:<38}', end='')
                print(f'\033[mR${preco}')
            print('\033[97m[4]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('\033[97mDigite o codigo do pedido: \033[m')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('\033[97mDigite uma opção: \033[m')

            if opcao == 1:
                peças_escolhidas.append(memoria_ram_asgard['[1]Memoria Ram ASGARD 8gb 3200MHz'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Memoria Ram ASGARD 8gb 3200MHz: R$180")
            if opcao == 2:
                peças_escolhidas.append(memoria_ram_asgard['[2]Memoria Ram ASGARD 16gb 3200MHz'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Memoria Ram ASGARD 16gb 3200MHz: R$300")
            if opcao == 3:
                peças_escolhidas.append(memoria_ram_asgard['[3]Memoria Ram ASGARD 32gb 3200MHz'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Memoria Ram ASGARD 32gb 3200MHz: R$500")
            if opcao == 4:
                return inicio()

            print(linha())
            return inicio()

        if asgard_corsair_hyperx == 2:
            print('\033[97;40mMEMORIAS RAM CORSAIR DISPONVEIS\033[m')
            for item, preco in memoria_ram_corsair.items():
                print(f'\033[97m{item:<38}', end='')
                print(f'R${preco}\033[m')
            print('\033[97m[4]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('\033[97mDigite o codigo do pedido: \033[m')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('\033[97mDigite uma opção: \033[m')

            if opcao == 1:
                peças_escolhidas.append(memoria_ram_corsair['[1]Memoria Ram Corsair 8gb 3600MHz'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Memoria Ram Corsair 8gb 3600MHz: R$150")
            if opcao == 2:
                peças_escolhidas.append(memoria_ram_corsair['[2]Memoria Ram Corsair 16gb 3600MHz'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Memoria Ram Corsair 16gb 3600MHz: R$300")
            if opcao == 3:
                peças_escolhidas.append(memoria_ram_corsair['[3]Memoria Ram Corsair 3600MHz'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Memoria Ram Corsair 32gb 3600MHz: R$566")
            if opcao == 4:
                return inicio()

            print(linha())
            return inicio()

        if asgard_corsair_hyperx == 3:
            print('\033[97;40mMEMORIAS RAM DISPONVEIS\033[m')
            for item, preco in memoria_ram_hyperx.items():
                print(f'\033[m{item:<38}\033[m', end='')
                print(f'\033[mR${preco}\033[m')
            print('[4]VOLTAR AO INICIO')

            print(linha())
            opcao = leiaInt('Digite o codigo do produto: ')
            print(linha())

            if opcao == 1:
                peças_escolhidas.append(memoria_ram_hyperx['[1]Memoria Ram HyperX 8b 2666MHz'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Memoria Ram HyperX 8gb 2666MHz: R$170")

            if opcao == 2:
                peças_escolhidas.append(memoria_ram_hyperx['[2]Memoria Ram HyperX 16gb 3200MHz'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Memoria Ram HyperX 16gb 3200MHz: R$300")

            if opcao == 3:
                peças_escolhidas.append(memoria_ram_hyperx['[3]Memoria Ram HyperX 32gb 3600Mhz'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Memoria Ram HyperX 32gb 3600MHz: R$688")

            if opcao == 4:
                return inicio()

            print(linha())
            return inicio()


def menuplacadeVideo():
    placa_de_video_nvidia = {'[1]NVIDIA GeForce RTX 3090': 9300,
                             '[2]NVIDIA GeForce RTX 3080 Ti': 6500,
                             '[3]NVIDIA GeForce RTX 3070 Ti': 4100,
                             '[4]NVIDIA GeForce GTX 2060 Super': 2000,
                             '[5]NVIDIA GeForce GTX 1660 Super': 1500,
                             '[6]NVIDIA GeForce GTX 1050 Ti': 1000}
    placa_de_video_amd = {'[1]AMD Radeon RX 6900 XT': 6500,
                          '[2]AMD Radeon RX 6800 XT': 4200,
                          '[3]AMD Radeon RX 5700 XT': 2000,
                          '[4]AMD Radeon RX 5600 XT': 800,
                          '[5]AMD Radeon RX 580': 500}

    while True:
        print('\033[33mMARCA DA PLACA DE VIDEO\033[m')
        print('[1]NVIDIA GeForce\n'
              '[2]AMD Radeon\033[m')

        print(linha())
        nvidia_ou_amd = leiaInt('Selecione a marca: ')
        print(linha())

        while nvidia_ou_amd != 1 and nvidia_ou_amd != 2:
            print('ERRO! por favor digite um número inteiro valido!')
            nvidia_ou_amd = leiaInt('Selecione a marca: ')

        if nvidia_ou_amd == 1:
            print('\033[97;40mPLACAS DE VIDEOS DA NVIDIA DISPONIVEIS:\033[m')
            for item, preco in placa_de_video_nvidia.items():
                print(f'\033[m{item:<38}\033[m', end='')
                print(f'\033[mR${preco}\033[m')
            print('[7]VOLTAR AO INICIO')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 7:
                print('ERRO! por favor digite um número inteiro valido!')

                print(linha())
                opcao = leiaInt('Digite uma opção: ')
                print(linha())

            if opcao == 1:
                peças_escolhidas.append(placa_de_video_nvidia['[1]NVIDIA GeForce RTX 3090'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("NVIDIA GeForce RTX 3090: R$9300")

            if opcao == 2:
                peças_escolhidas.append(placa_de_video_nvidia['[2]NVIDIA GeForce RTX 3080 Ti'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("NVIDIA GeForce RTX 3080 Ti: R$6500")

            if opcao == 3:
                peças_escolhidas.append(placa_de_video_nvidia['[3]NVIDIA GeForce RTX 3070 Ti'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("NVIDIA GeForce RTX 3070 Ti: R$4100")

            if opcao == 4:
                peças_escolhidas.append(placa_de_video_nvidia['[4]NVIDIA GeForce GTX 2060 Super'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("NVIDIA GeForce GTX 2060 Super: R$2000")

            if opcao == 5:
                peças_escolhidas.append(placa_de_video_nvidia['[5]NVIDIA GeForce GTX 1660 Super'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("NVIDIA GeForce GTX 1660 Super: R$1500")

            if opcao == 6:
                peças_escolhidas.append(placa_de_video_nvidia['[6]NVIDIA GeForce GTX 1050 Ti'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("NVIDIA GeForce GTX 1050 Ti: R$1000")

            if opcao == 7:
                return inicio()

            print(linha())
            return inicio()

        if nvidia_ou_amd == 2:
            print('\033[97;40mPLACAS DE VIDEOS DA AMD DISPONVEIS:\033[m')
            for item, preco in placa_de_video_amd.items():
                print(f'\033[m{item:<38}\033[m', end='')
                print(f'\033[mR${preco}\033[m')
            print('[6]VOLTAR AO INICIO')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido: ')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(placa_de_video_amd['[1]AMD Radeon RX 6900 XT'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("AMD Radeon RX 6900 XT: R$6500")

            if opcao == 2:
                peças_escolhidas.append(placa_de_video_amd['[2]AMD Radeon RX 6800 XT'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("AMD Radeon RX 6800 XT: R$4200")

            if opcao == 3:
                peças_escolhidas.append(placa_de_video_amd['[3]AMD Radeon RX 5700 XT'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("AMD Radeon RX 5700 XT: R$2000")

            if opcao == 4:
                peças_escolhidas.append(placa_de_video_amd['[4]AMD Radeon RX 5600 XT'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("AMD Radeon RX 5600 XT: R$800")

            if opcao == 5:
                peças_escolhidas.append(placa_de_video_amd['[5]AMD Radeon RX 580'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("AMD Radeon RX 580: R$500")

            if opcao == 6:
                return inicio()

            print(linha())
            return inicio()


def menuSsdHd():
    ssdpc = {'[1]SSD 120gb': 90,
           '[2]SSD 240gb': 150,
           '[3]SSD 480gb': 250,
           '[4]SSD 1tb': 500,
           '[5]SSD 2TB': 900}
    ssdnotebook = {'[1]SSD 120gb': 72,
                   '[2]SSD 240gb': 120,
                   '[3]SSD 480gb': 210,
                   '[4]SSD 1tb': 400,
                   '[5]SSD 2tb': 700}
    hd = {'[1]HD p/Desktop 250gb': 120,
          '[2]HD p/Desktop 500gb': 209.99,
          '[3]HD p/Desktop 1tbgb': 399.99,
          '[4]HD p/Desktop 2tb': 659.99}

    while True:
        print('\033[33mSSD E HD PARA DESKTOP E NOTEBOOK')
        print('[1]SSD PARA DESKTOP\n'
              '[2]SSD PARA NOTEBOOK\n'
              '[3]HD PARA DESKTOP\033[m')

        print(linha())
        ssdpc_ssdnote_hd = leiaInt('Selecione o modelo: ')
        print(linha())

        while ssdpc_ssdnote_hd != 1 and ssdpc_ssdnote_hd != 2 and ssdpc_ssdnote_hd != 3:
            print('ERRO! por favor digite um número inteiro valido!')
            ssdpc_ssdnote_hd = leiaInt('Selecione o modelo: ')

        if ssdpc_ssdnote_hd == 1:
            print('\033[97;40mSSD PARA DESKTOPS DISPONIVEIS:\033[m')
            for item, preco in ssdpc.items():
                print(f'\033[m{item:<38}\033[m', end='')
                print(f'\033[mR${preco}\033[m')
            print('[6]VOLTAR AO INICIO')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(ssdpc['[1]SSD 120gb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("SSD 120gb: R$90")

            if opcao == 2:
                peças_escolhidas.append(ssdpc['[2]SSD 240gb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("SSD 240gb: R$150")

            if opcao == 3:
                peças_escolhidas.append(ssdpc['[3]SSD 480gb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("SSD 480gb: R$250")

            if opcao == 4:
                peças_escolhidas.append(ssdpc['[4]SSD 1tb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("SSD 1tb: R$500")

            if opcao == 5:
                peças_escolhidas.append(ssdpc['[5]SSD 2TB'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("SSD 2TB: R$900")

            if opcao == 6:
                return inicio()

            print(linha())
            return inicio()

        if ssdpc_ssdnote_hd == 2:
            print('\033[97;40mSSD PARA NOTEBOOKS DISPONIVEIS:\033[m')
            for item, preco in ssdnotebook.items():
                print(f'\033[m{item:<38}\033[m', end='')
                print(f'\033[mR${preco}\033[m')
            print('[6]VOLTAR AO INICIO')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(ssdnotebook['[1]SSD 120gb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("SSD 120gb/Notebook: R$72")

            if opcao == 2:
                peças_escolhidas.append(ssdnotebook['[2]SSD 240gb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("SSD 240gb/Notebook: R$120")

            if opcao == 3:
                peças_escolhidas.append(ssdnotebook['[3]SSD 480gb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("SSD 480gb/Notebook: R$210")

            if opcao == 4:
                peças_escolhidas.append(ssdnotebook['[4]SSD 1tb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("SSD 1tb/Notebook: R$400")

            if opcao == 5:
                peças_escolhidas.append(ssdnotebook['[5]SSD 2tb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("SSD 2tb/Notebook: R$700")

            if opcao == 6:
                return inicio()

            print(linha())
            return inicio()

        if ssdpc_ssdnote_hd == 3:
            print('\033[97;40mHDS DISPONIVEIS:\033[m')
            for item, preco in hd.items():
                print(f'\033[m{item:<38}\033[m', end='')
                print(f'\033[mR${preco}\033[m')
            print('[5]VOLTAR AO INICIO')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(hd['[1]HD p/Desktop 250gb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("HD p/Desktop 250gb: 120")

            if opcao == 2:
                peças_escolhidas.append(hd['[2]HD p/Desktop 500gb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("HD p/Desktop 500gb: R$209.99")

            if opcao == 3:
                peças_escolhidas.append(hd['[3]HD p/Desktop 1tb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("HD p/Desktop 1tb: R$399.99")

            if opcao == 4:
                peças_escolhidas.append(hd['[4]HD p/Desktop 2tb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("HD p/Desktop 2tb: R$659.99")

            if opcao == 5:
                return inicio()

            print(linha())
            return inicio()


def menuAircoolerWatercooler():
    aircooler = {'[1]Noctua NH-D15': 1104,
                 '[2]Cooler Master Hyper 212 EVO V2': 374.99,
                 '[3]Deepcool Assassin III': 879.99,
                 '[4]Intel Amd Redragon Thor Rainbow CC-9103': 177.99,
                 '[5]Intel Amd Redragon Tyr': 129.99}
    watercooler = {'[1]SilverStone Tundra TD03-RGB': 259.99,
                   '[2]Corsair H150i Elite Capellix': 1220,
                   '[3]Asus ROG Ryuo 240': 839.99,
                   '[4]Deepcool Castle 360EX': 839,
                   '[5]EVGA CLC 280mm': 589.99}

    while True:
        print('\033[33mSELECIONE O MODELO, WATER COOLER / AIRCOOLER\n'
              '[1]AIRCOOLER\n'
              '[2]WATERCOOLER\n')

        print(linha())
        air_water = leiaInt('Selecione uma opção: ')
        print(linha())

        while air_water != 1 and air_water != 2:
            print('ERRO! por favor digite um número inteiro valido!')
            air_water = leiaInt('Selecione uma opção: ')

        if air_water == 1:
            print('\033[97mAIRCOOLERS DISPONIVEIS\033[m')
            for item, preco in aircooler.items():
                print(f'\033[97m{item:<45}\033[m', end='')
                print(f'\033[97mR${preco}\033[m')
            print('\033[97;40m[6]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido: ')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(aircooler['[1]Noctua NH-D15'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Aircooler Noctua NH-D15: R$1.104")

            if opcao == 2:
                peças_escolhidas.append(aircooler['[2]Cooler Master Hyper 212 EVO V2'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Cooler Master Hyper 212 EVO V2: R$374.99")

            if opcao == 3:
                peças_escolhidas.append(aircooler['[3]Deepcool Assassin III'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Deepcool Assassin III : R$879.99")

            if opcao == 4:
                peças_escolhidas.append(aircooler['[4]Intel Amd Redragon Thor Rainbow CC-9103'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Intel Amd Redragon Thor Rainbow CC-9103: R$179.99")

            if opcao == 5:
                peças_escolhidas.append(aircooler['[5]Intel Amd Redragon Tyr'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Intel Amd Redragon Tyr: R$129.99")

            if opcao == 6:
                return inicio()

            print(linha())
            return inicio()

        if air_water == 2:
            print('\033[97mWATERCOOLERS DISPONIVEIS\033[m')
            for item, preco in watercooler.items():
                print(f'\033[97m{item:<38}\033[m', end='')
                print(f'\033[97mR${preco}\033[m')
            print('\033[97;40m[6]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido: ')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(watercooler['[1]SilverStone Tundra TD03-RGB'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("SilverStone Tundra TD03-RGB: R$259.99")

            if opcao == 2:
                peças_escolhidas.append(watercooler['[2]Corsair H150i Elite Capellix'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Corsair H150i Elite Capellix: R$1220")

            if opcao == 3:
                peças_escolhidas.append(watercooler['[3]Asus ROG Ryuo 240'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Asus ROG Ryuo 240: R$839.99")

            if opcao == 4:
                peças_escolhidas.append(watercooler['[4]Deepcool Castle 360EX'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Deepcool Castle 360EX: R$839")

            if opcao == 5:
                peças_escolhidas.append(watercooler['[5]EVGA CLC 280mm'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("EVGA CLC 280mm: 589.99")

            if opcao == 6:
                return inicio()

            print(linha())
            return inicio()


def menuFontes():
    fontespcgamemax = {'[1]Fonte Gamemax Gamer ATX, 800W, 80 Plus Bronze:': 789.99,
                       '[2]Fonte Gamemax GS600, 600W, 80 Plus White:': 299.99,
                       '[3]Fonte 750W Gamemax GP750 80 Plus Bronze Pfc Ativo:': 368.99,
                       '[4]Fonte Gamemax Gm550 550W, 80 Plus Bronze, Pfc Ativo:': 259.99}
    fontespcxpg = {'[1]Fonte 550W 80 Plus Bronze XPG:': 564.99,
                   '[2]XPG Fonte Core Reactor 650W 80 Plus Gold Modular:': 639.99,
                   '[3]Fonte XPG Core Reactor 750W 80 Plus Gold Modular:': 889.99,
                   '[4]Fonte ATX 850W REAL XPG 80 Plus Gold Core Reactor:': 956.70}

    fontespccorsair = {'[1]Fonte Atx 550W Corsair CV550 80 Plus Bronze:': 422.99,
                       '[2]FONTE ATX 650W - CV650-80 PLUS BRONZE:': 639.99,
                       '[3]FONTE CORSAIR CX750M 750W CERTIFICADO 80 PLUS:': 819.99,
                       '[4]Fonte Corsair RMx Series, RM850x, 850W, 80 Plus:': 999.99}
    while True:
        print('\033[33mSELECIONE A MARCA\n'
              '[1]GAMEMAX\n'
              '[2]XPG\n'
              '[3]CORSAIR\n\033[m')
        print(linha())
        gamemax_xpg_corsair = leiaInt('Selecione uma opção: ')
        print(linha())

        while gamemax_xpg_corsair != 1 and gamemax_xpg_corsair != 2 and gamemax_xpg_corsair != 3:
            print('ERRO! por favor digite um número inteiro valido!')
            gamemax_xpg_corsair = leiaInt('Selecione uma opção: ')

        if gamemax_xpg_corsair == 1:
            print('\033[97mFONTES GAMEMAX DISPONIVEIS\033[m')
            for item, preco in fontespcgamemax.items():
                print(f'\033[97m{item:<55}\033[m', end='')
                print(f'\033[97mR${preco}\033[m')
            print('\033[97m[5]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido: ')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')


            if opcao == 1:
                peças_escolhidas.append(fontespcgamemax['[1]Fonte Gamemax Gamer ATX, 800W, 80 Plus Bronze:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Fonte Gamemax Gamer ATX, 800W, 80 Plus Bronze: R$789.99")

            if opcao == 2:
                peças_escolhidas.append(fontespcgamemax['[2]Fonte Gamemax GS600, 600W, 80 Plus White:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Fonte Gamemax GS600, 600W, 80 Plus White: R$299.99")

            if opcao == 3:
                peças_escolhidas.append(fontespcgamemax['[3]Fonte 750W Gamemax GP750 80 Plus Bronze Pfc Ativo:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Fonte 750W Gamemax GP750 80 Plus Broze Pfc Ativo: R$368.99")

            if opcao == 4:
                peças_escolhidas.append(fontespcgamemax['[4]Fonte Gamemax Gm550 550W, 80 Plus Bronze, Pfc Ativo:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Fonte Gamemax Gm550, 80 Plus Bronze, Pfc Ativo: R$259.99")

            if opcao == 5:
                return inicio()

            print(linha())
            return inicio()

        if gamemax_xpg_corsair == 2:
            print('\033[97mFONTES XPG DISPONIVEIS\033[m')
            for item, preco in fontespcxpg.items():
                print(f'\033[97m{item:<55}\033[m', end='')
                print(f'\033[97mR${preco}\033[m')
            print('\033[97m[5]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido: ')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(fontespcxpg['[1]Fonte 550W 80 Plus Bronze XPG:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Fonte Gamemax Gamer ATX, 800W, 80 Plus Bronze: R$564.99")

            if opcao == 2:
                peças_escolhidas.append(fontespcxpg['[2]XPG Fonte Core Reactor 650W 80 Plus Gold Modular:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("XPG Fonte Core Reactor 650W 80 Plus Gold Modular: R$639.99")

            if opcao == 3:
                peças_escolhidas.append(fontespcxpg['[3]Fonte XPG Core Reactor 750W 80 Plus Gold Modular:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("XPG Fonte Core Reactor 750W 80 Plus Gold Modular: R$889.99")

            if opcao == 4:
                peças_escolhidas.append(fontespcxpg['[4]Fonte ATX 850W REAL XPG 80 Plus Gold Core Reactor:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Fonte ATX 850W REAL XPG 80 Plus Gold Core Reactor: R$956.70")

            if opcao == 5:
                return inicio()

            print(linha())
            return inicio()

        if gamemax_xpg_corsair == 3:
            print('\033[97mFONTES CORSAIR DISPONIVEIS\033[m')
            for item, preco in fontespccorsair.items():
                print(f'\033[97m{item:<55}\033[m', end='')
                print(f'\033[97mR${preco}\033[m')
            print('\033[97m[5]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido: ')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(fontespccorsair['[1]Fonte Atx 550W Corsair CV550 80 Plus Bronze:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Fonte Atx 550W Corsair CV550 80 Plus Bronze: R$422.99")

            if opcao == 2:
                peças_escolhidas.append(fontespccorsair['[2]FONTE ATX 650W - CV650-80 PLUS BRONZE:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("FONTE ATX 650W - CV650-80 PLUS BRONZE: R$639.99")

            if opcao == 3:
                peças_escolhidas.append(fontespccorsair['[3]FONTE CORSAIR CX750M 750W CERTIFICADO 80 PLUS:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("FONTE CORSAIR CX750M 750W CERTIFICADO 80 PLUS: R$819.99")

            if opcao == 4:
                peças_escolhidas.append(fontespccorsair['[4]Fonte Corsair RMx Series, RM850x, 850W, 80 Plus:'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Fonte Corsair RMx Series, RM850x, 850W, 80 Plus: R$999.99")

            if opcao == 5:
                return inicio()

            print(linha())
            return inicio()


def menuGabinete():
    gabinetecorsair = {'[1]Gabinete Atx Mid Tower 4000 4000d Airflow ': 799.99,
                       '[2]Gabinete Gamer Corsair Carbide Series Spec Delta Rgb': 465.79,
                       '[3]Gabinete Gamer H7 Flow NZXT, Flow Edition': 1399.99,
                       '[4]Gabinete Atx Mid Tower 4000x Rgb White': 939.99}

    gabinetereddragon = {'[1]Gabinete Gamer Redragon Wideload Mid Tower': 749.99,
                         '[2]Gabinete Gamer Redragon Grapple, Mid Tower': 399.99,
                         '[3]Gabinete Gamer Redragon Grapple Branco Gc-607wh': 612.99,
                         '[4]Gabinete Gamer Redragon Diamond Storm Pro': 429.99}

    gabinetenzxt = {'[1]Gabinete Gamer H7 Flow NZXT, Flow Edition': 1399.99,
                    '[2]GABINETE ATX MID-TOWER - H510 BLACK': 549.89,
                    '[3]Gabinete H510 White - Ca-H510B-W1, Nzxt': 589.79,
                    '[4]Gabinete Gamer H5 Flow NZXT, Flow Edition': 999.99}
    while True:
        print('\033[33mSELECIONE A MARCA DO GABINETE\n'
              '[1]CORSAIR\n'
              '[2]RED DRAGON\n'
              '[3]NZXT\n\033[m')

        print(linha())
        corsair_reddragon_nzxt = leiaInt('Selecione a marca: ')
        print(linha())

        while corsair_reddragon_nzxt != 1 and corsair_reddragon_nzxt != 2 and corsair_reddragon_nzxt != 3:
            print('ERRO! por favor digite um número inteiro valido!')
            corsair_reddragon_nzxt = leiaInt('Selecione a marca: ')

        if corsair_reddragon_nzxt == 1:
            print('\033[97mGABINETES CORSAIR DISPONIVEIS\033[m')
            for item, preco in gabinetecorsair.items():
                print(f'\033[97m{item:<57}\033[m', end='')
                print(f'\033[97mR${preco}\033[m')
            print('\033[97m[5]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido: ')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(gabinetecorsair['[1]Gabinete Atx Mid Tower 4000 4000d Airflow '])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Gabinete Atx Mid Tower 4000 4000d Airflow: R$799.99")

            if opcao == 2:
                peças_escolhidas.append(gabinetecorsair['[2]Gabinete Gamer Corsair Carbide Series Spec Delta Rgb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Gabinete Gamer Corsair Carbide Series Spec Delta Rgb: R$465.79")

            if opcao == 3:
                peças_escolhidas.append(gabinetecorsair['[3]Gabinete Gamer H7 Flow NZXT, Flow Edition'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Gabinete Gamer H7 Flow NZXT, Flow Edition: R$1399.99")

            if opcao == 4:
                peças_escolhidas.append(gabinetecorsair['[4]Gabinete Atx Mid Tower 4000x Rgb White'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Gabinete Atx Mid Tower 4000x Rgb White: R$939.99")

            if opcao == 5:
                return inicio()

            print(linha())
            return inicio()

        if corsair_reddragon_nzxt == 2:
            print('\033[97mGABINETES RED DRAGON DISPONIVEIS\033[m')
            for item, preco in gabinetereddragon.items():
                print(f'\033[97m{item:<55}\033[m', end='')
                print(f'\033[97mR${preco}\033[m')
            print('\033[97m[5]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido: ')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(gabinetereddragon['[1]Gabinete Gamer Redragon Wideload Mid Tower'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Gabinete Gamer Redragon Wideload Mid Tower: R$749.99")

            if opcao == 2:
                peças_escolhidas.append(gabinetereddragon['[2]Gabinete Gamer Redragon Grapple, Mid Tower'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Gabinete Redragon Grapple, Mid Tower: R$399.99")

            if opcao == 3:
                peças_escolhidas.append(gabinetereddragon['[3]Gabinete Gamer Redragon Grapple Branco Gc-607wh'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Gabinete Redragon Grapple Branco Gc-607wh: R$612.99")

            if opcao == 4:
                peças_escolhidas.append(gabinetereddragon['[4]Gabinete Gamer Redragon Diamond Storm Pro'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Gabinete Redragon Diamond Storm Pro: R$429.99")

            if opcao == 5:
                return inicio()

            print(linha())
            return inicio()

        if corsair_reddragon_nzxt == 3:
            print('\033[97mGABINETES NZXT DISPONIVEIS\033[m')
            for item, preco in gabinetenzxt.items():
                print(f'\033[97m{item:<55}\033[m', end='')
                print(f'\033[97mR${preco}\033[m')
            print('\033[97m[5]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('Digite o codigo do pedido: ')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(gabinetenzxt['[1]Gabinete Gamer H7 Flow NZXT, Flow Edition'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Gabinete Gamer H7 Flow NZXT, Flow Edition: R$1399.99")

            if opcao == 2:
                peças_escolhidas.append(gabinetenzxt['[2]GABINETE ATX MID-TOWER - H510 BLACK'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("GABINTE ATX MID-TOWER - H510 BLACK: R$549.99")

            if opcao == 3:
                peças_escolhidas.append(gabinetenzxt['[3]Gabinete H510 White - Ca-H510B-W1, Nzxt'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Gabinete H510 White - Ca-H510B-W1, Nzxt: R$589.79")

            if opcao == 4:
                peças_escolhidas.append(gabinetenzxt['[4]Gabinete Gamer H5 Flow NZXT, Flow Edition'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Gabinete Gamer H5 Flow NZXT, Flow Edition: R$999.99")

            if opcao == 5:
                return inicio()

            print(linha())
            return inicio()


def menuFans():
    fansdepcool = {'[1]Kit com 3 Fans DeepCool CF120 Plus Preto RGB 120mm': 249.99,
                   '[2]Fan Cooler Deepcool RF120 Fs, 120mm, Rgb': 34.99,
                   '[3]Kit Cooler Fan Deepcool RF120M, 5 Unidades, 120mm': 364.99}

    fansrisemode = {'[1]Kit Cooler FAN Rise Mode RGB Aura, 3x120mm': 149.99,
                    '[2]Fan Individual Gamer Rise Mode Black Sem Led 80mm': 15.99,
                    '[3]Cooler Fan Rise Mode Wind W1, 120mm, Led Azul': 25.99}
    while True:
        print('\033[33mMARCAS DE VENTOINHA/FANS DISPONIVEIS\n'
              '[1]DEEPCOOL\n'
              '[2]RISE MODE\n')

        print(linha())
        deepcool_ou_risemode = leiaInt('Selecione uma marca: ')
        print(linha())

        while deepcool_ou_risemode != 1 and deepcool_ou_risemode != 2:
            print('ERRO! por favor digite um número inteiro valido!')
            deepcool_ou_risemode = leiaInt('Selecione uma marca: ')

        if deepcool_ou_risemode == 1:
            print('\033[97mVENTOINHAS/FANS DISPONIVEIS\033[m')
            for item, preco in fansdepcool.items():
                print(f'\033[97m{item:<55}\033[m', end='')
                print(f'\033[97mR${preco}\033[m')
            print('\033[97m[4]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('Selecione uma opção: ')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(fansdepcool['[1]Kit com 3 Fans DeepCool CF120 Plus Preto RGB 120mm'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Kit com 3 Fans DeepCool CF120 Plus Preto RGB 120mm: R$249")

            if opcao == 2:
                peças_escolhidas.append(fansdepcool['[2]Fan Cooler Deepcool RF120 Fs, 120mm, Rgb'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Fan Cooler Deepcool RF120 Fs, 120mm, Rgb: R$34.99")

            if opcao == 3:
                peças_escolhidas.append(fansdepcool['[3]Kit Cooler Fan Deepcool RF120M, 5 Unidades, 120mm'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Kit Cooler Fan Deepcool RF120M, 5 Unidades, 120mm: R$364.99")

            if opcao == 4:
                return inicio()

            print(linha())
            return inicio()

        if deepcool_ou_risemode == 2:
            print('\033[97mFONTES CORSAIR DISPONIVEIS\033[m')
            for item, preco in fansrisemode.items():
                print(f'\033[97m{item:<55}\033[m', end='')
                print(f'\033[97mR${preco}\033[m')
            print('\033[97m[4]VOLTAR AO INICIO\033[m')

            print(linha())
            opcao = leiaInt('Selecione uma opção: ')
            print(linha())

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                print('ERRO! por favor digite um número inteiro valido!')
                opcao = leiaInt('Digite uma opção: ')

            if opcao == 1:
                peças_escolhidas.append(fansrisemode['[1]Kit Cooler FAN Rise Mode RGB Aura, 3x120mm'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Kit Cooler FAN Rise Mode RGB Aura, 3x120mm: R$149.99")

            if opcao == 2:
                peças_escolhidas.append(fansrisemode['[2]Fan Individual Gamer Rise Mode Black Sem Led 80mm'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Fan Individual Gamer Rise Mode Black Sem Led 80mm: R$15.99")

            if opcao == 3:
                peças_escolhidas.append(fansrisemode['[3]Cooler Fan Rise Mode Wind W1, 120mm, Led Azul'])
                print('\033[32mAdicionado ao carrinho com sucesso!🛒\033[m')
                nomepecas.append("Cooler Fan Rise Mode Wind W1, 120mm, Led Azul: R$25.99")

            if opcao == 4:
                return inicio()

            print(linha())
            return inicio()



def VerCarrinho():
    cabecalho('🛒CARRINHO DE COMPRA🛒')
    print('\033[97mPROCURANDO ITENS NO CARRINHO...\033[m')
    sleep(5)
    indice = 0
    for item in nomepecas:
        print(f'\033[97mItem: {item} / COD:{indice}\033[m')
        indice += 1
    if not peças_escolhidas:
        print('\033[31mNENHUM ITEM ENCONTRADO\033[m')

    return inicio()


def Removeritens():
    codigo = leiaInt('\033[97mDigite o codigo do produto que deseja remover: \033[m')
    sair = False
    for i, pecas in enumerate(peças_escolhidas):
        if codigo == i:
            del peças_escolhidas[i]
            sair = True
    for i, pecas in enumerate(nomepecas):
        if codigo == i:
            del nomepecas[i]
            sair = True
    if sair:
        print('ITEM REMOVIDO DO CARRINHO COM SUCESSO.')

    else:
        print('\033[31mNENHUM ITEM ENCONTRADO\033[m')

    return inicio()

def inicio():
    while True:
        cabecalho('SELECIONE A PEÇA')
        print('\033[97m[1]PLACA MÃE\n'
              '[2]PROCESSADOR\n'
              '[3]MEMORIA RAM\n'
              '[4]PLACA DE VIDEO\n'
              '[5]SSD\n'
              '[6]COLLER PARA PROCESSADOR\n'
              '[7]FONTE\n'
              '[8]GABINETE\n'
              '[9]VENTOINHAS [FANS]\n'
              '[10]VER CARRINHO DE COMPRAS\n'
              '[11]REMOVER ITENS DO CARRINHO\n'
              '[12]SAIR\033[m')
        print(linha())
        opc = leiaInt('\033[97mDigite sua opção: ')
        print(linha())
        if opc == 1:
            menuplacaMae()
        elif opc == 2:
            menuprocessador()
        elif opc == 3:
            menumemoriaram()
        elif opc == 4:
            menuplacadeVideo()
        elif opc == 5:
            menuSsdHd()
        elif opc == 6:
            menuAircoolerWatercooler()
        elif opc == 7:
            menuFontes()
        elif opc == 8:
            menuGabinete()
        elif opc == 9:
            menuFans()
        elif opc == 10:
            VerCarrinho()
        elif opc == 11:
            Removeritens()
        elif opc == 12:
            print('Muito Obrigado por comprar em nossa loja! Volte sempre!')
            print(f'Total a pagar R${sum(peças_escolhidas):.2f}')
            name = nomepecas
            if len(name) == 0:
                print('Nenhuma Compra efetuada')
            else:
                print(f'Itens comprados {nomepecas}')
        else:
            print('Essa opção não existe, por favor digite uma opção valida!!')
            return inicio()

        break


#programa principal
cabecalho('<<<MONTE SEU PC>>>')

inicio()


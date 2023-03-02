from colorama import init, Fore, Back
import rotas, matem, funcweb, os, time


def cmd():
    print(Back.BLACK + Fore.GREEN + '>> LINHA DE COMANDO <<' + Back.RESET + '\n')
    print(Back.BLACK + Fore.BLUE + '[PRIC] - Menu Principal' + Back.RESET)
    print(Back.BLACK + Fore.BLUE + '[MATE] - Menu Matemático' + Back.RESET)
    print(Back.BLACK + Fore.BLUE + '[WEBR] - Menu Web' + Back.RESET + '\n\n')
    
    print(Back.BLUE + Fore.BLACK + '[BHAS] - Função Bhaskara' + Back.RESET)
    print(Back.BLUE + Fore.BLACK + '[FIBO] - Função Fibonacci' + Back.RESET)
    print(Back.BLUE + Fore.BLACK + '[PESQ] - Função Pesquisa' + Back.RESET)
    print(Back.BLUE + Fore.BLACK + '[YTBE] - Função Youtube' + Back.RESET)
    print(Back.BLUE + Fore.BLACK + '[GGLE] - Função Google' + Back.RESET)
    print(Back.BLUE + Fore.BLACK + '[CGPT] - Função ChatGPT' + Back.RESET)
    print(Back.BLUE + Fore.BLACK + '[SYST] - Integridade Sistema' + Back.RESET)
    print(Back.BLUE + Fore.BLACK + '[COTA] - Função contação' + Back.RESET + '\n\n')

    print(Back.BLACK + Fore.RED + '[SAIR] - SAIR CMD > (menu principal)' + Back.RESET)
    
    resp = input('Esperando Comando\n>>> ').upper()
    try:
        if resp == 'PRIC':
            rotas.rotas4()
        if resp == 'MATE':
            rotas.rotas()
        if resp == 'WEBR':
            rotas.rotas2()
        if resp == 'BHAS':
            matem.bhask()
        if resp == 'FIBO':
            matem.fibonacci()
        if resp == 'PESQ':
            funcweb.pesquisa()
        if resp == 'YTBE':
            funcweb.youtube()
        if resp == 'GGLE':
            funcweb.google()
        if resp == 'CGPT':
            funcweb.chatgpt()
        if resp == 'COTA':
            funcweb.contacao()
        if resp == 'SYST':
            rotas.rotas3()
        if resp == 'SAIR':
            rotas.rotas4()
        else:
            print(Fore.RED + 'COMANDO INVÁLIDO')
            cmd()
            
    except:
        print('Sistema Finalizado!!!')


def HCK():
    print(Back.BLACK + Fore.GREEN + '>> LINHA DE COMANDO HACKING <<' + Back.RESET + '\n')
    print(Back.BLACK + Fore.BLUE + '[VERIIP] - Mostra o IP da Máquina na Rede' + Back.RESET)
    print(Back.BLACK + Fore.BLUE + '[VERIFY] - Mostra Todos os Dispositivos Conectados a Rede' + Back.RESET)
    print(Back.BLACK + Fore.BLUE + '[VERIF1] - Mostra Portas Abertas do Dispositivo Conectado a Rede' + Back.RESET)
    print(Back.BLACK + Fore.BLUE + '[VERIOS] - Mostra o OS de Todos os Dispositivos Conectados a Rede' + Back.RESET)
   
    print(Back.BLACK + Fore.BLUE + '[WHOIS] - Abrir Função do whois' + Back.RESET )
    print(Back.BLACK + Fore.BLUE + '[WHATWEB] - Abrir Função do whatweb' + Back.RESET)

    print(Back.BLACK + Fore.BLUE + '[DIRB] - Procurar links de sites' + Back.RESET)

    print(Back.BLACK + Fore.BLUE + '[IPINFO] - Informações sobre IP' + Back.RESET + '\n\n')
    
    print(Back.BLACK + Fore.RED + '[SAIR] - SAIR HCK > (menu principal)' + Back.RESET+ Fore.GREEN)
    

    resp = input('Esperando Comando\n>>> ').upper()

    try:
        if resp == 'VERIIP':
            
            os.system('ifconfig')
            time.sleep(3)
            HCK()

        if resp == 'VERIFY':
            resp1 = input('Informe IP da Rede Somente até a 3° casa ( Ex: 192.168.0)\n>>> ')

            resp1 = resp1 + '/24'
            
            os.system(f'sudo nmap {resp1}')

            time.sleep(3)
            HCK()

        if resp == 'VERIF1':
            resp1 = input('Informe IP\n>>> ')
            
            os.system(f'sudo nmap {resp1}')

            time.sleep(3)
            HCK()
            
        if resp == 'VERIOS':
            resp1 = input('Informe IP de um Dispositivo na rede\n>>> ')
            
            os.system(f'sudo nmap {resp1} -O ')

            time.sleep(3)
            HCK()
        
        if resp == 'WHOIS':
            resp1 = input('Informe o IP ou Domínio do Site\n>>> ')
            
            os.system(f'whois {resp1}')

            time.sleep(3)
            HCK()
        
        if resp == 'WHATWEB':
            resp1 = input('Informe o IP ou Domínio do Site\n>>> ')
            
            os.system(f'whatweb {resp1}')

            time.sleep(3)
            HCK()
        
        if resp == 'DIRB':
            resp1 = input('Informe a URL do Site\n>>> ')
            
            os.system(f'dirb {resp1}')

            time.sleep(3)
            HCK()
        
        if resp == 'IPINFO':
            resp1 = input('Informe o IP Desejado ou "myip" se deseja saber sobre seu IP\n>>> ')
            
            os.system(f'ipinfo {resp1}')

            time.sleep(3)
            HCK()
        
        if resp == 'SAIR':
            rotas.rotas4()

        else:
            print(Fore.RED + 'COMANDO INVÁLIDO')
            HCK()
            
    except:
        print('Sistema Finalizado!!!')


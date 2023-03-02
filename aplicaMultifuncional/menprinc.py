from colorama import init, Fore, Back
import time, rotas, os, rotas2

def menu():
    
    print(Back.BLUE + Fore.WHITE + '*-*-*  MENU  *-*-*' + Back.RESET + '\n')
    print(Fore.YELLOW + '[1] - Menu Matemático\n')
    print(Fore.YELLOW + '[2] - Menu Web\n')
    print(Fore.YELLOW + '[3] - Monitor\n')
    #print(Fore.YELLOW + '[cmd] - LINHA DE COMANDO\n')
    print(Back.RESET + Fore.YELLOW + '[quit] - Sair\n')
    
    try:
        entrada = input(Fore.CYAN + 'Digite qual opção você deseja: ').upper()
        
        if entrada == 'QUIT':
            print(Fore.GREEN + 'Terminando...\n')
            time.sleep(1)
            os._exit(0)
        
        if entrada == 'HCK':
            rotas2.hac()
            

        elif entrada == 'CMD':
            print(Fore.GREEN + 'Abrindo Linha de Comando...\n')
            
            rotas2.rotaCMD()
        elif entrada == 'SAIR':
            exit()
        
        entrada = int(entrada)
        
        #print(type(entrada))
        if entrada == 1:
            print(Fore.GREEN + 'Abrindo Menu Matemático...\n')
            
            rotas.rotas()
        
        elif entrada == 2:
            print(Fore.GREEN + 'Entrando Web')
            
            rotas.rotas2()

        elif entrada == 3:
            print(Fore.GREEN + 'Verificando uso da CPU')
            
            rotas.rotas3()
        
        
        else:
            print(Fore.RED + '\n\n\nOPÇÃO INCORRETA\n')
            menu()
    except:
        print(Fore.RED + '\n\n\nENTRADA INCORRETA, REVEJA A ESCRITA\n')
        menu()

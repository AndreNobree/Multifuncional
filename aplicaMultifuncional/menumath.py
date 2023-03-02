from colorama import init, Fore, Back
import matem, time, menprinc, funcweb, rotas2

def menumath():
    
    print(Back.RED + Fore.WHITE + '*-*-*  MENU MATEMÁTICO  *-*-*'+ Back.RESET +'\n' )
    print(Fore.YELLOW + '[1] - Bhaskara')
    print(Fore.YELLOW + '[2] - Fibonacci')

    print(Fore.YELLOW + '[99] - RETORNAR AO MENU PRINCIPAL\n')
    
    entrada = input(Fore.CYAN + 'Digite qual opção você deseja: ').upper()
    
    try:
        if entrada == 'CMD':
            rotas2.rotaCMD()
        elif entrada == 'SAIR':
            exit()
        entrada = int(entrada)

        if entrada == 1:
            print(Fore.GREEN + '\nIniciando Programa de Bhaskara...\n')
            time.sleep(1)
            matem.bhask()
        
        elif entrada == 2:
            print(Fore.GREEN + '\nIniciando Programa de Fibonacci...\n')
            time.sleep(1)
            matem.fibonacci()
            
        elif entrada == 99:
            print(Fore.GREEN + '\nRetornando ao menu principal...\n')
            time.sleep(1)
            return menprinc.menu()


        else:
            print(Fore.RED + '\n\nOPÇÃO INCORRETA\n')
            menumath()
    except:
        print(Fore.RED + '\nENTRADA INCORRETA\n')
        print(Fore.RED + 'REVEJA A ESCRITA\n')


def weber():

    print(Back.GREEN + Fore.WHITE + '*-*-*  MENU WEB  *-*-*'+ Back.RESET + '\n')
    print(Fore.YELLOW + '[1] - Wikipédia')
    print(Fore.YELLOW + '[2] - Youtube')
    print(Fore.YELLOW + '[3] - Google')
    print(Fore.YELLOW + '[4] - ChatGPT')
    print(Fore.YELLOW + '[5] - Cotação Moeda')

    print(Fore.YELLOW + '[99] - RETORNAR AO MENU PRINCIPAL\n')
    
    entrada = input(Fore.CYAN + 'Digite qual opção você deseja: ')
    
    try:
        
        if entrada == 'cmd':
            rotas2.rotaCMD()
        
        if entrada == 'hck':
            rotas2.hac()

        elif entrada == 'sair':
            exit()
        entrada = int(entrada)
        if entrada == 1:
            funcweb.pesquisa()
        
        elif entrada == 2:
            funcweb.youtube()
            
        elif entrada == 3:
            funcweb.google()
        
        elif entrada == 4:
            funcweb.chatgpt()
        
        elif entrada == 5:
            funcweb.contacao()
        
        elif entrada == 99:
            menprinc.menu()

        else:
            print(Fore.RED + '\n\nOPÇÃO INCORRETA\n')
            weber()
    except:
        print(Fore.RED + '\nENTRADA INCORRETA\n')
        print(Fore.RED + 'REVEJA A ESCRITA\n')

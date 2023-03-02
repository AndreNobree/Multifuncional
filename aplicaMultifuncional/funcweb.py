from colorama import init, Fore, Back
import time, menprinc, rotas
import httpx, wikipedia, psutil, webbrowser, requests, pywhatkit, rotas2

def pesquisa():
    
    print(Fore.YELLOW + '\nWikipédia\nDIGITE [quit] PARA SAIR A QUALQUER MOMENTO DO PROGRAMA\n ')
    time.sleep(2)
    entr = str(input(Fore.CYAN + 'Digite a sua pesquisa: \n\n->'))
    wikipedia.set_lang('pt')
    
    try:
        if entr == 'quit':
            print(Fore.GREEN + 'Terminando...\n')
            time.sleep(2)
            rotas.rotas2()

        if entr == 'cmd':
            rotas2.rotaCMD()
            pesquisa()
        
        if entr == 'hck':
            rotas2.hac()
            pesquisa()
        
        elif entr == 'sair':
            exit()
            
        else:
            resultado = wikipedia.summary(entr, 2) 
            print(Fore.GREEN + 'Pesquisando...')
            time.sleep(1)
            print(Fore.YELLOW + f'{resultado}')   
            pesquisa()
    except Exception as erro:
        print(Fore.RED + f'ERRO, Especifique sua pesquisa \n-> {erro}')
        time.sleep(1)
        pesquisa()

def youtube():
    
    try:
        print(Fore.YELLOW + '\nYoutube\nDIGITE [quit] PARA SAIR A QUALQUER MOMENTO DO PROGRAMA\n ')
        time.sleep(2)
        entr = input(Fore.CYAN + 'Digite a sua Música: \n\n->')

        if entr == 'quit':
            rotas.rotas2()

        if entr == 'cmd':
            rotas2.rotaCMD()
            youtube()
        
        if entr == 'hck':
            rotas2.hac()
            youtube()
        
        elif entr == 'sair':
            exit()

        else:
            print(f'Tocando {entr}')  
            time.sleep(1)   
            resulta = pywhatkit.playonyt(entr)
            youtube()

        
    except Exception as erro:
        print(Fore.RED + f"Erro ao Tocar musica \n-> {erro}")

def google():
    
    try:
        entr = str(input(Fore.CYAN + 'Digite a sua pesquisa: \n\n->'))
        if entr == 'cmd':
            rotas2.rotaCMD()
            google()
        if entr == 'hck':
            rotas2.hac()
            google()

        elif entr == 'sair':
            exit()

        else:
            print('pesquisando')
            time.sleep(1)   
            webbrowser.open_new_tab(f'https://www.google.com.br/search?q={entr}') 
            rotas.rotas2()
    except Exception as erro:
        print(Fore.RED + f"Erro ao Pesquisar \n-> {erro}")

def chatgpt():
    
    try:
        print(Fore.YELLOW + '\nChatGPT\nDIGITE [quit] PARA SAIR A QUALQUER MOMENTO DO PROGRAMA\n ')
        time.sleep(2)
        prompt = input(Fore.CYAN + 'Digite: \n\n->')

        if prompt == 'quit':
            rotas.rotas2()

        if prompt == 'hck':
            rotas2.hac()
            chatgpt()

        elif prompt == 'sair':
            exit()

        if prompt == 'cmd':
            rotas2.rotaCMD()    
            chatgpt()
        else:

            api_key = "1234455"
            endpoint = "https://api.openai.com/v1/engines/davince/completions"
            
            model = "text-davince-002"

            data = {
                "prompt": prompt,
                "model": model,
                "max_tokens": 100
            }

            response = requests.post(endpoint, json=data, headers={
                "Content-Type": "aplication/json",
                "Authorization": f"Bearer {api_key}"
            })

            print(Fore.YELLOW + response.json())
            
            chatgpt()
    except Exception as erro:
        print(Fore.RED + f"Erro \n-> {erro}")
        rotas.rotas2()

def contacao():
    
    try:
        print(Fore.YELLOW + '\nCotação\nDIGITE [quit] PARA SAIR A QUALQUER MOMENTO DO PROGRAMA\n ')
        time.sleep(2)
        base_currency = str(input(Fore.CYAN + 'Digite a moeda de base (ex:BRL):\n >  ')).upper()
        if base_currency == 'QUIT':
            rotas.rotas2()

        if base_currency == 'CMD':
            rotas2.rotaCMD() 
            contacao()
        
        if base_currency == 'HCK':
            rotas2.hac()
            contacao()
        
        elif base_currency == 'sair':
            exit()

        else:
            currency = str(input(Fore.CYAN + 'Digite a moeda desejada (ex:USD):\n >  ')).upper()
            if currency == 'QUIT':
                rotas.rotas2()
            else:
                response = httpx.get(
                    url=f'https://api.exchangerate.host/latest?base={base_currency}'
                ).json()
                currency_data = response['rates']
                
                print(Fore.YELLOW + f'1 {base_currency} vale {currency_data.get(currency)} {currency}')
                
                contacao()

    except Exception as erro:
        print(Fore.RED + f"Erro ao fazer a cotação \n-> {erro}")
        rotas.rotas2()

def sistema():
    
    try:
        usocpuinfo = str(psutil.cpu_percent())
        usodacpu  = "{:.0f}".format(float(usocpuinfo))
        usomemoriainfo = str(psutil.virtual_memory().percent)
        usomemoria = "{:.0f}".format(float(usomemoriainfo))
        print(Fore.YELLOW + '\n\nO uso do processador está em ' + usodacpu +'%')
        print(Fore.YELLOW + '\nO uso da memória está em ' + usomemoria + '%\n\n\n')
        time.sleep(1)
        menprinc.menu()
    except Exception as erro:
        print(Fore.RED + f"Erro ao verificar sistema \n-> {erro}")
        menprinc.menu()
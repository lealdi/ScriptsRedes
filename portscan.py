import socket

host = input('Digite o host: ')
porta = int(input('Digite o número da porta: '))

def scannear():
    varredor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    verificador = varredor.connect_ex((host,porta))
    if verificador == 0:
        print(f'[+] Porta {porta} -> ABERTA ')
    else:
        print(f'[+] Porta {porta} -> FECHADA ')

scannear()


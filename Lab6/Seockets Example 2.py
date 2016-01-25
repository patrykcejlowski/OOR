#scanner portow, bardzo wolny mozna przyspieszyc stosujac threading

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'amw.gdynia.pl'

def pscan(port):
    try:
        s.connect((server,port))
        return True         #jak mozeszmy sie polaczyc z portem
    except:
        return False

for x in range(1,26):
    if pscan(x):
        print("Port",x,"jest otwarty!!!!! Mozna hackowac!!!!!")
    else:
        print("Port",x,"jest zamkniety :(")

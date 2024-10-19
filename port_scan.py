import socket
import sys
import re 
import logging


def main():
    logging.basicConfig (filename= 'Information_Ports.log', filemode='a',
                     format ="%(asctime)s - %(levelname)s - %(message)s",
                     datefmt = "%m/%d/%Y %I:%M:%S %p", level = logging.INFO)

    def validar_ip(ip):
        patron = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
        return re.match(patron, ip) is not None

    def validar_puertos(PortList):
        for port in PortList:
            if not (0 <= port <= 65535):
                return False
        return True

    def Arguments():
        PortList=[]
        while True:
            ip=input('Ingrese la IP en la que desea hacer el escaneo de puertos: ')
            if not validar_ip(ip):
                print('IP inválida. Por favor, inténtelo de nuevo.')
                logging.warning(f'IP inválida: {ip}')
                continue
            logging.info(f'IP: {ip}')
            PortList_input=input('Por favor, ingrese la lista de puertos a escanear \
    separados por comas (por ejemplo: 2,3,4,5): ')
            try: 
                PortList = [int(port.strip()) for port in PortList_input.split(',')]
            except ValueError:
                print('Asegúrate de ingresar números enteros.')
                logging.warning(f'Asegúrate de ingresar números enteros {PortList}')
                continue
            if not validar_puertos(PortList):
                print('Los puertos deben estar entre 0 y 65535.')
                logging.warning(f'Los puertos no estan entre 0 y 656536: {PortList}')
                continue
            logging.info(f'Lista de puertos: {PortList}')
            break
        return ip, PortList


    ip, PortList=Arguments()

    def CheckPorts(ip,PortList):
        try:
            for port in PortList:
                sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.settimeout(3)
                result=sock.connect_ex((ip,port))
                if result==0:
                    print(f'Puerto {port}: \t Abierto')
                    logging.info(f'Puerto {port}: \t Abierto')
                else:
                    print(f'Puerto {port}: \t Cerrado')
                    logging.info(f'Puerto {port}: \t Cerrado')
                sock.close()
        except socket.error as error:
            print(str(error))
            print("Error de conexión")
            logging.warning(f'Error de conexión: {error}')
            sys.exit()

    CheckPorts(ip,PortList)



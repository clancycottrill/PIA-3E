import requests 
import json 
import logging 



def main():
    logging.basicConfig(
    filename='internetdb_search_logs.log',
    filemode='a',
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO
)

    # Función principal encargada de hacer request a la API InternetDB y conseguir los datos para luego mostrar en pantalla.
    def internetdb_request(ip): 
        url = "https://internetdb.shodan.io/" + ip
        try: 
            response = requests.get(url)
            datos = response.json()

            # Impresión de IP
            print(f"IP: {datos['ip']}")
            logging.info(f"Revisión de la IP: {datos['ip']}")

            # Impresión de hostnames de la IP.
            hostname = datos.get('hostnames', [])
            if hostname:
                print(f"Hostname(s) asociados a la IP: {', '.join(hostname)}")
                logging.info(f"Hostname(s) asociados a la IP: {', '.join(hostname)}")
            else:
                print("La IP no tiene ningún hostname asociado.")
                logging.warning("La IP no tiene ningún hostname asociado.")

            # Impresión de puertos de la IP.
            ports = datos.get('ports', [])
            if ports:
                print(f"Puerto(s) abiertos en la IP: {', '.join(map(str, ports))}")
                logging.info(f"Puerto(s) abiertos en la IP: {', '.join(map(str, ports))}")
            else:
                print("La IP no tiene ningún puerto abierto.")
                logging.warning("La IP no tiene ningún puerto abierto.")

            # Impresión de etiquetas de la IP.
            tags = datos.get('tags', [])
            if tags:
                print(f"Etiqueta(s) asociadas a la IP: {', '.join(tags)}")
                logging.info(f"Etiqueta(s) asociadas a la IP: {', '.join(tags)}")
            else:
                print("La IP no tiene ninguna etiqueta asociada.")
                logging.warning("La IP no tiene ninguna etiqueta asociada.")

            # Impresión de vulnerabilidades de la IP
            vulns = datos.get('vulns', [])       
            if vulns:
                print(f"Vulnerabilidades de la IP: {', '.join(vulns)} ")
                logging.info(f"Vulnerabilidades de la IP: {', '.join(vulns)}")
            else:
                print("La IP no tiene ninguna vulnerabilidad registrada.")
                logging.warning("La IP no tiene ninguna vulnerabilidad registrada.")
                
        except requests.exceptions.RequestException as e:
            print(f"Error en la request a la API: {e}")
            logging.error(f"Error en la request a la API 'InternetDB': {e}")

        except Exception as e:
            print(f"Error en ejecución: {e}")
            logging.error(f"Error en ejecución: {e}")

    #Solicitar la IP
    ip = input("Ingrese la IP a revisar: ")

    # Llamada a la función
    internetdb_request(ip)



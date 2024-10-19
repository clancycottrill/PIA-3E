import requests 
import json 
import logging 
import shodan



def main():
    logging.basicConfig(
    filename='shodan_search_logs.log',
    filemode='a',
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO
)
    # Función principal encargada de hacer request a la API InternetDB (Shodan) y conseguir los datos para luego mostrar en pantalla.
    def shodan_request(apikey, ip): 
        shodanobj = shodan.Shodan(apikey)
        try:
            results = shodanobj.search(f"ip:{ip} country:MX has_vuln:True")

            if results['total'] > 0:
                for result in results['matches']:
                    # Impresión y loggeo de IP 
                    print(f"IP: {ip}")
                    logging.info(f"IP: {ip}")

                    # Impresión y loggeo de ciudad
                    city = result['location'].get('city', 'Ciudad no identificada')
                    print(f"Ciudad de la IP: {city}")
                    logging.info(f"Ciudad de la IP: {city}")

                    # Impresión y loggeo de vulnerabilidades
                    vulns = result.get('vulns', None)

                    if vulns:
                        print(f"Vulnerabilidades: {vulns}")
                        logging.info(f"Vulnerabilidades: {vulns}")
                        print("Vulnerabilidades totales: ", len(vulns))
                        logging.info("Vulnerabilidades totales: " + str(len(vulns)))
                    else:
                        print("No hay vulnerabilidades identificadas.")
                        logging.info("No hay vulnerabilidades identificadas")

            else:
                print(f"No se encontraron resultados para la IP {ip}.")
                logging.info(f"No se encontraron resultados para la IP {ip}.")

        except shodan.APIError as e:
            print(f"Error en la API de Shodan: {e}")
            logging.error(f"Error en la API de Shodan: {e}")

    #Solicitar API Key y la IP
    apikey = input("Ingrese su API Key de Shodan: ")
    ip = input("Ingrese la IP a revisar: ")

    #Llamada a la función
    shodan_request(apikey, ip)


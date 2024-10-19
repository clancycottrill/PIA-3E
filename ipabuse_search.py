import requests
import json
import sys
import simplejson

 
class API:
    def __init__(self, apikey):
        self.apikey = apikey
        self.url = "https://api.abuseipdb.com/api/v2/"
        self.h = {
            "Accept" : "application/json",
            "Key" : self.apikey
        }

    def checkip(self, ipaddress, maxdays=90):
        url= self.url + "check"
        parameters = {
            "ipAddress" : ipaddress,
            "maxAgeInDays" : maxdays
        }
        try:
            response = requests.get(url, headers=self.h, params=parameters)
            return response.json()
        
        except requests.exceptions.ConnectionError:
            return {"error": "Error de conexión. Verifica tu conexión a internet."}
        
        except requests.exceptions.Timeout:
            return {"error": "La solicitud ha excedido el tiempo de espera."}
        
        except requests.exceptions.RequestException as e:
            return {"error": f"Error inesperado: {str(e)}"}
        
        except simplejson.errors.JSONDecodeError:
            return {"error": "Error al procesar la respuesta en formato JSON."}

def menu():
    print("1. Ingresar API key")
    print("2. Verificar una IP")
    print("3. Salir")

def main():
    apikey = None  
    c = None  

    while True:
        menu()  
        opcion = input("\nSelecciona una opcion (1-3): ")
        
        if opcion == "1":
            apikey = input("Introduce tu API key: ")
            c = API(apikey)  
            
        elif opcion == "2":
            if c is None:
                print("Primero debes ingresar la API key (opción 1).")
            else:
                ipaddress = input("Introduce la IP que deseas verificar: ")
                resultado = c.checkip(ipaddress)  
                print("\nResultado de la verificación de IP:")
                print(resultado)
                
        elif opcion == "3":
            print("Saliendo del programa...")
            break  
        else:
            print("Opción no válida, por favor selecciona una opción entre 1 y 3.")


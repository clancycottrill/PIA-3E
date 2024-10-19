import logging 
import argparse 
import file_encrypt
import ipabuse_search
import port_scan 
import shodan_search
import internetdb_search

logging.basicConfig (filename = 'main_logs.log', filemode = 'a', format ="%(asctime)s - %(levelname)s - %(message)s", datefmt = "%m/%d/%Y %I:%M:%S %p", level = logging.INFO)


def menu():
    val = True
    while val:
        print("Este es el menú del tercer entregable del PIA de Programacion para Ciberseguridad.")
        print("-----------------------------------------")
        print("¿Qué desea realizar?")
        print("1. Módulo 'file_encrypt'")
        print("2. Módulo 'ipabuse_search'")
        print("3. Módulo 'port_scan'")
        print("4. Módulo 'shodan_search'")
        print("5. Módulo 'internetdb_search'")
        print("6. Salir")
        print("-----------------------------------------")
        option = input("Ingrese la opción: ")
        logging.info(f"Opción elegida: {option}")

        while not option.isdigit():
            print ("Ingrese un número válido.")
            logging.error("Número no válido ingresado.")
            option = input("Ingrese la opción: ")

        option = int(option)

        while option <=0 or option >=7:
            print('Elija una opción válida')
            logging.error("Número no válida ingresada.")
            option = input("Ingrese la opción: ")

        try:
            if option == 1:
                file_encrypt.main()
                logging.info("Módulo 'file_encrypt' ejecutado")
            elif option == 2:
                ipabuse_search.main()
                logging.info("Módulo 'ipabuse_search' ejecutado")
            elif option == 3:
                port_scan.main()
                logging.info("Módulo 'port_scan' ejecutado")
            elif option == 4:
                shodan_search.main()
                logging.info("Módulo 'shodan_search'")
            elif option == 5:
                internetdb_search.main()
                logging.info("Módulo 'internetdb_search'")
            else:
                print("Saliendo del programa...")
                logging.info("Salida de programa")
                val = False
                
        except Exception as e:
            print (f"Error al entrar al módulo seleccionado: {e}")
                
menu()

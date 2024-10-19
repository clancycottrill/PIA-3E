# PIA-3E

Tercer entregable del PIA de Programación para Ciberseguridad!

Este repositorio contiene los 5 módulos correspondientes al tercer entregable del PIA de Programación para Ciberseguridad, además de un script principal para manejar los 5 módulos.

Contiene los siguientes módulos:

1. file_encrypt
2. ipabuse_search
3. port_scan
4. shodan_search
5. internetdb_search

======================================================

En cuanto a las funciones individuales de los módulos:

file_encrypt: Nuestro módulo complejo. Este módulo se encarga de encriptar y desencriptar archivos seleccionados por el usuario, así como proporcionar la llave necesaria para desencriptarlo en caso de querer hacerlo manualmente.

ipabuse_search: Este módulo se encarga de revisar la API AbuseIPDB para revisar actividades maliciosas reportadas por usuarios de internet.

port_scan: Este módulo se encarga de escanear los puertos de una IP ingresada por el usuario y determinar si está cerrado o abierto.

shodan_search: Este módulo se encarga de revisar la API de Shodan para analizar una IP específicamente que sea de México y reportar las vulnerabilidades reportadas por usuarios de internet. 

internetdb_search: Este módulo se encarga de revisar la API de Internetdb para conseguir hostnames, puertos abiertos y vulnerabilidades reportadas por usuarios de internet de alguna dirección IP.

======================================================

Aclaraciones de los scripts:

Para el módulo 'shodan_search': El módulo está pensado para funcionar solamente con IPs localizadas en México. El módulo podría fallar usándolo con IPs fuera de México. 

Para el módulo 'shodan_search' y 'ipabuse_search': Para poder correr estos módulos, se necesitará una API Key de cada página. Para el módulo de 'shodan_search' específicamente, se necesita una cuenta arriba del nivel "gratis" para acceder a las vulnerabilidades, y que se ejecute correctamente.

======================================================

Realizado en conjunto por el equipo 5:

Santiago B.

Chris T.

Alexander T.

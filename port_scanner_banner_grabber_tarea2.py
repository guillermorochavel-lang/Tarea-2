# tarea 2 port scanner banner grabber

import socket    # usando libreria socket

ip_objetivo = '189.141.233.100'  #ip objetivo es la pública de mi laptop
puerto_inicio = 1  #escaneando puertos del 1 al 200
puerto_fin = 2000

print(f'Escaneando {ip_objetivo} de puerto {puerto_inicio} a {puerto_fin}...')
print('-' * 50)


for puerto in range(puerto_inicio, puerto_fin + 1):
    try:
        socket_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        resultado = socket_conexion.connect_ex((ip_objetivo, puerto))  # connect_ex()

        if resultado == 0:  #para detectar y arrojar los puertos que están abiertos

            print(f'Puerto {puerto}: ABIERTO')

            # Intentamos obtener el banner
            try:

                socket_conexion.settimeout(5) # timeout de  5 segundos

                banner = socket_conexion.recv(1024) #recv(1024) y  captura el banner del servicio que corre en cada puerto abierto

                banner_texto = banner.decode('utf-8', errors='ignore')

                print(f' Banner: {banner_texto.strip()}') #muestra los resultados correctamente.

            except:

                print(f' Banner: No disponible')

        socket_conexion.close()

    except:
        pass
    print('-' * 50)

    print('Escaneo completado')

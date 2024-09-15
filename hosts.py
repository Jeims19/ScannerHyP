import os
import platform

print("""
***********************************************
      INICIAMOS DESCUBRIMIENTO DE HOSTS
***********************************************
""")
segmento_escanear="192.168.1."


def escanear_segmento_red(segmento):
    hosts_activos = []
    for i in range(1,255):
        host = segmento+str(i)
        if ping_host(host):
            hosts_activos.append(host)
        else:
            print(f"Sin respuesta: {host}")
    return hosts_activos

def ping_host(host):
    # Determina el comando de ping según el sistema operativo
    comando = "ping -c 1 " + host if platform.system().lower() != "windows" else "ping -n 1 " + host
    respuesta = os.system(comando)
    return respuesta == 0

lista =escanear_segmento_red(segmento_escanear)
print("Hosts activos:", lista)


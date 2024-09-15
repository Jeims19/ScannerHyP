import socket
ip="192.168.1.57"
puertos_abiertos=[]
try:
    for port in range(1,65535):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conexion:
            resultado=conexion.connect_ex((ip,port))
            if resultado==0:
                print("Puerto",port,"está: abierto")
                puertos_abiertos=puertos_abiertos.append(port)
            else:
                print("Puerto",port,"está: cerrado o filtrado")
except Exception as c:
    print("Error: ",c)

print(puertos_abiertos)

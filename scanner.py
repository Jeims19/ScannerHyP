import socket
ip="192.168.1.67" 
try:
    for port in range(1,25):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conexion:
            resultado=conexion.connect_ex((ip,port))
            if resultado==0:
                print("Puerto",port,"está: abierto")
            else:
                print("Puerto",port,"está: cerrado o filtrado")
except Exception as c:
    print("Error: ",c)

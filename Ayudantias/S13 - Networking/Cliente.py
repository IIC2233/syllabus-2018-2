__author__ = "jnhasard & pnheinsohn"

import sys
import threading as th
import socket
import json
from FrontEnd import VentanaPrincipal
from PyQt5.QtWidgets import QApplication
from datetime import datetime


HOST = "localhost"
PORT = 8081

class Cliente:

    '''
    Esta es la clase encargada de conectarse con el servidor e intercambiar información
    '''

    def __init__(self):
        print("Inicializando cliente...")
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = HOST
        self.port = PORT

        self.frontend = VentanaPrincipal(self)
        self.frontend.show()

        try:
            self.socket_cliente.connect((self.host, self.port))
            print("Cliente conectado exitosamente al servidor")

            self.conectado = True

            escuchar_servidor = th.Thread(target=self.escuchar, daemon=True)
            escuchar_servidor.start()
            print("Escuchando al servidor...")

        except ConnectionRefusedError:
            self.terminar_conexion()

    def escuchar(self):
        '''
        Este método es usado en el thread y la idea es que reciba lo que
        envía el servidor. Implementa el protocolo de agregar los primeros
        4 bytes, que indican el largo del mensaje
        '''

        while self.conectado:
            try:
                # Recibimos los 4 bytes del largo
                tamano_mensaje_bytes = self.socket_cliente.recv(4)
                tamano_mensaje = int.from_bytes(tamano_mensaje_bytes, byteorder="big")
                
                contenido_mensaje_bytes = bytearray()

                # Recibimos el resto de los datos
                while len(contenido_mensaje_bytes) < tamano_mensaje:
                    contenido_mensaje_bytes += self.socket_cliente.recv(256)

                print("pase el while")
                # Decodificamos y pasamos a JSON el mensaje
                contenido_mensaje = contenido_mensaje_bytes.decode("utf-8")
                mensaje_decodificado = json.loads(contenido_mensaje)

                # Manejamos el mensaje
                self.manejar_comando(mensaje_decodificado)
            
            except ConnectionResetError:
                self.terminar_conexion()

    def manejar_comando(self, diccionario):
        '''
        Este método toma el mensaje decodificado de la forma:
        {"status": tipo del mensaje, "data": información}
        '''

        print(f"Mensaje recibido: {diccionario}")

        if diccionario["status"] == "mensaje":
            data = diccionario["data"]
            usuario = data["usuario"]
            contenido = data["contenido"]
            usuario = f"({datetime.now().hour}:{datetime.now().minute}) {usuario}"
            self.frontend.ventana_chat.actualizar_chat(f"{usuario}: {contenido}")

    def send(self, mensaje):
        '''
        Este método envía la información al servidor. Recibe un mensaje del tipo:
        {"status": tipo del mensaje, "data": información}
        '''

        # Codificamos y pasamos a bytes
        mensaje_codificado = json.dumps(mensaje)
        contenido_mensaje_bytes = mensaje_codificado.encode("utf-8")

        # Tomamos el largo del mensaje y creamos 4 bytes de esto
        tamano_mensaje_bytes = len(contenido_mensaje_bytes).to_bytes(4, byteorder="big")

        # Enviamos al servidor
        self.socket_cliente.send(tamano_mensaje_bytes + contenido_mensaje_bytes)

    def terminar_conexion(self):
        print("Conexión terminada")
        self.connected = False
        self.socket_cliente.close()
        exit()


if __name__ == "__main__":
    app = QApplication([])
    cliente = Cliente()
    sys.exit(app.exec_())

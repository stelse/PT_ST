#!/usr/bin/env python3

import paramiko
import json

class UnknownTransport(Exception):
    pass

class TransportError(Exception):
    pass

def get_transport(transport_name, **kwargs):
    if transport_name == 'ssh':
        with open('config.json', 'r') as file:
            file_config = json.load(file)
        file.close
        config = {'host' : file_config['host'],
                  'login' : file_config['transports']['SSH']['login'],
                  'password' : file_config['transports']['SSH']['password'],
                  'port' : file_config['transports']['SSH']['port']}
        config.update(kwargs)
        transport = paramiko.SSHClient()
        transport.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        transport = transport.connect(host = config['host'],
                                      port = config['port'],
                                      login = config['login'],
                                      password = config['password'])
        return transport
    else:
        raise UnknownTransport()

class transport_ssh:
    def __init__(self):
        self.client = get.transport('ssh')

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
        

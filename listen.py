#!/bin/env python
import socket
import paramiko
import ssl, OpenSSL
from os import chmod
from Crypto.PublicKey import RSA
from io import StringIO
from sys import stdout

client = paramiko.SSHClient()

class connect_listen:
 def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

 def socket_in(self):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((self.hostname, self.port))
   return s

 def socket_transport(self):
   transport = paramiko.Transport(self.socket_in())
   transport.connect()
   return transport

 def get_keyfile(self, xdir):
  f = open(str(xdir),'r')
  read = f.read()
  keyfile = StringIO.StringIO(read)
  mykey = paramiko.RSAKey.from_private_key(keyfile)
  return mykey


 def ssh_connect(self, pkey):
         client.connect(hostname = self.hostname,port = self.port, username = self.username , password = self.password, key_filename = self.get_keyfile(input("Enter ssh key directory)))
         client.load_system_host_keys()
         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

         while client.connect:
          try:
            print("connected run command")
            stdin, stdout, stderr = client.exec_command(input(str))
            print(stdin)
            return stdin
          except:
            print("error")


 def preference(self, _pubkeys, _key, _compression, _kex, _macs, _cipher):
        print("requesting preferred config")
        secure = paramiko.transport.SecurityOptions(self.socket_transport())
        secure.ciphers = ((self, _cipher))
        secure.kex = ((self, _kex))
        secure.compression = ((self, _compression))
        secure.key_types = ((self, _key))
        print(self.socket_transport().get_security_options()._transport)


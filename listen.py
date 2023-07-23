#!/bin/env python
from fileinput import filename
from ipaddress import ip_address
from sys import stdout
import sys
import socket
import paramiko
from jumpssh import SSHSession
import ssl, socket, OpenSSL
from os import chmod
from Crypto.PublicKey import RSA
from regex import purge
import subprocess
import jumpssh
import pyshark
import logging
from io import StringIO

client = paramiko.SSHClient()

class connect_listen:
 def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = 22
        self.username = username
        self.password = password

    
 def get_hostname(self, hostname): return self.hostname

 def get_port(self, port): return self.port
    
 def get_username(self, username): return self.username

 def get_password(self, password): return self.password

 def get_client(self) : return client

 def get_keyfile(self):
  f = open('/path/to/key.pem','r')
  read = f.read()
  keyfile = StringIO.StringIO(read)
  mykey = paramiko.RSAKey.from_private_key(keyfile)
  return mykey


 def socket_in(self):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((self.hostname, self.port))
   return s

 def socket_transport(self):
   transport = paramiko.Transport(self.socket_in())
   transport.connect()
   return transport


 def ssh_connect(self, pkey):
         client.connect(hostname = self.hostname,port = self.port, username = self.username , password = self.password, key_filename = pkey)
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


 def keygen(self, content_file = "key.txt", bits = None):
      key = RSA.generate(bits)    
      with open("key,txt", 'wb') as content_file:
        chmod("key.txt", 0)
        content_file.write(key.exportKey('PEM'))
      pubkey = key.publickey()
      with open("key.txt", 'wb') as content_file:
          content_file.write(pubkey.exportKey('OpenSSH'))

 def preference(self, _pubkeys, _key, _compression, _kex, _macs, _cipher):
        print("requesting preferred config")
        secure = paramiko.transport.SecurityOptions(self.socket_transport())
        secure.ciphers = ((self, _cipher))
        secure.kex = ((self, _kex))
        secure.compression = ((self, _compression))
        secure.key_types = ((self, _key))
        print(self.socket_transport().get_security_options()._transport)

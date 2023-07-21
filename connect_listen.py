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
#rewrite all code

client = paramiko.SSHClient()


ssh_crack = False
ssh_connect = False

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


 def logging(self):
  print(logging.basicConfig())
  print(logging.getLogger("paramiko").setLevel(logging.WARNING))


 def socket_in(self):
      _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      _socket.connect((self.hostname, self.port))
      return _socket

 def socket_transport(self):
   transport = paramiko.Transport(self.socket_in())
   transport.connect()
   return transport

 def channel(self, chanid):
        channel = paramiko.channel.Channel(chanid)
        return channel

 def _hexdump(self):
   return self.socket_transport().set_hexdump(True)

 def remotekey(self):
  return self.socket_transport().get_remote_serverkey()


 def ssh_connect(self, *passwords, pkey):
        #connect_listen(hostname = self.hostname , port = self.port, username = self.username, password = self.password).initate()
        for passin in passwords:
         client.connect(hostname = self.hostname,port = self.port, username = self.username , password = passin, key_filename = pkey)
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

            #make more modular

 def _serverkey(self):
     print(f'PUBLIC REMOTE SERVERKEY{self._remotekey()}')
     self._remotekey().get_bits()
     self._remotekey().get_fingerprint()
     self._remotekey().serverkey.get_name()

 def _hexdump(self):
  print(f'HEXDUMP{self.socket_transport()}')
  self.socket_transport().set_hexdump(True)
  print(self.socket_transport().get_hexdump())
  self.logging()


 def _log_channel(self):
  _log = set.client_log_channel(name = "log-channel-1")
  client.save_host_keys()
  return _log

 def remote_listen(self):
   capture = pyshark.RemoteCapture(self.hostname, 'wlp3s0')
   capture.sniff(timeout = 50)
   print(capture)



 def jump_hosts(self, _jumphost, _jumppass):
  gateway_session = SSHSession(self.hostname,

                               self.username, password=self.password).open()
  remote_session = gateway_session.get_remote_session(_jumphost,

                                                      password=_jumppass)

  def get_hash(self):
     sock = socket.socket()
     sslsock = ssl.wrap_socket(sock)
     cert_der = sslsock.getpeercert(True)
     cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, cert_der)
     print (cert.get_signature_algorithm() )



 def _agent(self):
        print(".... trying to see if forward agent is available")
        try:
         self.socket_transport().open_forward_agent_channel()
        except:
            print("Agent Foward Channel not available")
    
 def keep_alive(self):
        print("... sending packet to keep this session alive")
        self.socket_transport().set_keepalive(30)


 def key_ssh(self, privatekeys):
        print("... Loading Key Info....")
        pKey = paramiko.PKey(message = input(str), data = input(str))

        pKey.get_name()
        pKey.get_bits()
        pKey.get_base64()
    
 def invoke_subsytem(self, subsystem):
        self.channel(1).invoke_subsystem(subsystem)

 # capture handshake through raw socket
 def capture_handshake(self):
        cap = pyshark.LiveCapture(interface = "enp0s25", bpf_filter='port 22')
        socket = self.socket_in()
        local = self.socket_transport()

        localpack = self.socket_transport().packetizer
        print("... starting handshake")
        #self.socket_transport().lock
        try:
         print(localpack.start_handshake(timeout = 10))
        except:
          pass

 def auth(self):
        print("... catching bad exception")
        try:
            self.socket_transport().auth_none(self.username) #get sock except
        except paramiko.BadAuthenticationType:
            print (paramiko.BadAuthenticationType)

 def keygen(self, content_file = "key.txt", bits = None):
      key = RSA.generate(bits)    
      with open("key,txt", 'wb') as content_file:
        chmod("key.txt", 0)
        content_file.write(key.exportKey('PEM'))
      pubkey = key.publickey()
      with open("key.txt", 'wb') as content_file:
          content_file.write(pubkey.exportKey('OpenSSH'))

 # person can prefer weak ciphers then decrpyt them using the capture method
 def preference(self, _pubkeys, _key, _compression, _kex, _macs, _cipher):
        print("requesting preferred config")
        secure = paramiko.transport.SecurityOptions(self.socket_transport())
        secure.ciphers = ((self, _cipher))
        #secure.kex = ((self, _kex))
        #secure.compression = ((self, _compression))
        #secure.key_types = ((self, _key))
        print(self.socket_transport().get_security_options()._transport)

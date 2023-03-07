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
import connect_listen
import jumpssh

#rewrite all code

client = paramiko.SSHClient()


ssh_crack = False
ssh_connect = False

class connect_listen(object):
 def __init__(self, hostname, port, username, password):
        self = self
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    

 def get_port(self, port):
     return self.port
    
 def get_username(self, username):
        return self.username

 def set_connect(self):
     self.connect = True

 def get_hostname(self):
        return self.hostname

 def socket_in(self):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      return s.connect((self.hostname, self.port))

 def transport(self):
        #transport = paramiko.transport.Transport(connect_listen().socket_in())
        _transport = client.get_transport()
        return _transport

 def channel(self, chanid):
        channel = paramiko.channel.Channel(chanid)
        return channel

 def _hexdump(self):
   self.transport().set_hexdump(True)

 def _pack(self):
  pack = self.transport().packtizer
  return pack

 def _remotekey(self):
  return self.transport().get_remote_serverkey()

 def initate(self):
       transcport_in = connect_listen().transport().start_client(self.hostname, self.port)
       return transport_in


 def ssh_connect(self, pkey):
        #connect_listen(hostname = self.hostname , port = self.port, username = self.username, password = self.password).initate()
        client.connect(hostname = self.hostname,port = self.port, username = self.username , password = self.password, key_filename = pkey)
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.transport()
        while client.connect:
          try:
            print("connected run command")
            stdin, stdout, stderr = client.exec_command(input(str))
            print(stdin)
            return stdin
          except:
            print("error")

            #make more modular
 def inbound(self):

        client.connect(hostname = self.hostname,port = self.port, username = self.username , password = self.password, key_filename = pkey)
        try:
          connect_listen().initate()
          print("Openning Terminal and Transport Channel")


          
          channel = connect_listen().transport().open_session(window_size=None, max_packet_size=None, timeout=None)
          channel.invoke_shell()
          
          print("...host key policy")
         
          client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

          print("Saving Hostkey(If none then no hostkey will be saved)")
       
          client.save_host_keys()
          client.set_log_channel(name = "logchannel1")


          print(connect_listen().transport().open_channel("logchannel1", self.hostname, "127.0.0.1"))

          print(connect_listen().transport().set_hexdump(True))

          print(connect_listen().transport().get_hexdump())
          
          security = connect_listen().transport().get_security_options()
          
          print("getting info....")
          
          print(security.ciphers())
          print(security.digests())
          print(security.kex())
          

        except:
            print("could not accept")

 def _serverkey(self):
     print(f'PUBLIC REMOTE SERVERKEY{self._remotekey()}')
     self._remotekey().get_bits()
     self._remotekey().get_fingerprint()
     self._remotekey().serverkey.get_name()

 def _log_channel(self):
  _log = client.set_log_channel(name = "log-channel-1")
  client.save_host_keys()
  return _log



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
    
        
 
 def ssh_pack_data(self, size):
      packet =  client.get_transport().packetizer
      print(packet.read_all())
      read = packet.read_all(15, check_rekey= True)
      print(read)



 def _agent(self):
        connect_listen().transport().open_channel(window_size=None, max_packet_size=None, timeout=None)
        print(".... trying to see if forward agent is available")
        try:
         transport.open_forward_agent_channel() 
        except:
            print("Agent Foward Channel not available")
    
 def keep_alive(self):
        print("... sending packet to keep this session alive")
        self.transport().set_keepalive(30)


 def key_ssh(self, privatekeys):
        print("... Loading Key Info....")
        pKey = paramiko.PKey(message = input(str), data = input(str))

        pKey.get_name()
        pKey.get_bits()
        pKey.get_base64()
    
 def invoke_subsytem(self, subsystem):
        self.channel().invoke_subsystem(subsystem)

    
 def read_data(self, n):
        self.channel(2).recv_ready()
        self.channel(2).recv(n)
        return channel(2).recv(n)
    
 def get_message(self, content):
	    message = paramiko.message.Message(content)
	    message.get_text()
    
 def starting_handshake(self):
        start = client.get_transport().packetizer
        print("... starting handshake")
        try:
         start.start_handshake(input(str))
        except:
            print("an error occured")

 def auth(self):
        print("... catching bad exception")
        try:
            paramiko.transport.Transport(self.hostname, self.port).auth_none(self.username) #get sock except
        except paramiko.BadAuthenticationType:
            print("This user is not allowed authentication")
            print (paramiko.BadAuthenticationType)

 def keygen(self, content_file = "key.txt", bits = None):
      key = RSA.generate(bits)    
      with open("key,txt", 'wb') as content_file:
        chmod("key.txt", 0)
        content_file.write(key.exportKey('PEM'))
      pubkey = key.publickey()
      with open("key.txt", 'wb') as content_file:
          content_file.write(pubkey.exportKey('OpenSSH'))
    

 def logging_all_banner(self):
        print(connect_listen().transport().get_banner())
        print("... saving the banner to a file")
        file = open(input(str), "r+")
        with file:
         file.write(transport.get_banner())

        
 def preference(self, _key, _compression, _kex, _macs):
        print("requesting preferred config")
        self.transport().preferred_keys[_key]
        self.transport().preferred_compression[_compression]
        self.transport().preferred_kex[_kex]
        self.transport().preferred_macs[_macs]
        print(transport().get_security_options())

 def send(self, content):
      _message = self.get_message(content)
      channel(2).send(_message)

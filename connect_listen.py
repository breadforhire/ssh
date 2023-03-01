#!/bin/env python
from fileinput import filename
from ipaddress import ip_address
from sys import stdout
import sys
import socket
sys.path.insert(0, '$/home/ender/.local/lib/python3.11/site-packages/paramiko')
import paramiko
from jumpssh import SSHSession
import ssl, socket, OpenSSL
from os import chmod
from Crypto.PublicKey import RSA
from regex import purge
import subprocess

client = paramiko.SSHClient()



ssh_crack = False
ssh_connect = False

commands_to_run = ["save_bash_scripts"]
class connect_listen:
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

    def get_connect(self):
        return connect
    
    def get_hostname(self):
        return self.hostname


    def socket_in(self):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      return s.connect((self.hostname, self.port))

    def transport(self):
        transport = paramiko.transport.Transport(socket_in())
        return transport

    def channel(self, chanid):
        channel = paramiko.channel.Channel(chanid)
        return channel

    def initate(self):
       return transport().start_client(self.hostname, self.port)


    def ssh_connect(self, pkey):
        client.connect(hostname = self.hostname,port = self.port, username = self.username , password = self.password, key_filename = pkey)
       
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if client.connect:
          try:
            print("connected run command")
            stdin, stdout, stderr = client.exec_command(input(str))
            print(stdin)


            return stdin
          except:
            print("error")
            
    def inbound(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.hostname, self.port))

        print("do you want to gather data")

        s.getaddrinfo('localhost', None)
        if user_bool == "yes" and self.get_connect() == True:
         try:
          
          print("Openning Terminal and Transport Channel")


          
          channel = transport().open_session()
          channel.get_pty(term=input(str), width=50, height=50)
          channel.invoke_shell()          
          
          print("...host key policy")
         
          client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

          print("Saving Hostkey(If none then no hostkey will be saved)")
       
          client.save_host_keys()
          client.set_log_channel(name = input("Set log channel"))


          print(transport().get_log_channel())

          print("Print True or False if you want to hexdump the channel")

          transport().set_hexdump(True)

          transport().get_hexdump(input(str))
          
          security = transport.get_security_options()
          
          print("getting info....")
          
          security.ciphers()
          security.digests()
          security.kex()
          
          print("getting serverkey and getting name")
          
          serverkey = transport.get_remote_server_key()

          serverkey.get_bits()
          serverkey.get_fingerprint()
          serverkey.get_name()


         except:
            
            print("could not accept")

    
    def telnet_jump_hosts():

       gateway_session = SSHSession('gateway.example.com',
       'my_user', password='my_password').open()
       remote_session = gateway_session.get_remote_session('remote.example.com',
        password='my_password2')
       if remote_session.exists():
         print(remote_session.get_cmd_output('ls -lta'))  
         remote_session.get('/remote/path/to/the/file', '/local/path/')
         remote_session.put('/local/path/to/a/file', '/remote/path/to/the/file')

    def get_hash():
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



    def ssh_open_new_channel():
        transport().open_channel(window_size=None, max_packet_size=None, timeout=None)
        print(".... trying to see if forward agent is available")
        try:
         transport.open_forward_agent_channel() 
        except:
            print("Agent Foward Channel not available")
    
    def keep_alive():
        print("... sending packet to keep this session alive")
        transport.set_keepalive(30)

    
    def ssh_server_tcp():
     print("Do you want to listen to new tcp connections? ")
     transport = client.get_transport()
     print("Do you want no handler or a default handler")
     bool_handle = input(str)
     if bool_handle == "n":
      transport().request_port_forward("127.0.0.1", 23, handler=None)
      transport().open_forwarded_tcpip_channel()
      transport().accept()
    
    def sign_key():
        pKey = paramiko.PKey(message = input(str), data = input(str))
        print("The key sign bool: ")
        print(pKey.can_sign())
        return pKey.sign_ssh_data(data= input(str), algorithm= pKey.get_name())

    
    def key_ssh(privatekeys):
        print("... Loading Key Info....")
        pKey = paramiko.PKey(message = input(str), data = input(str))

        pKey.get_name()
        pKey.get_bits()
        pKey.get_base64()
        
        print("Seeing if Key can sign")
        if pKey.can_sign():
            print("This key can sign data, do you want to save ?")
            pKey.write_private_key(filename = input(str), password = input(str))
            return True
    
    def invoke_subsytem(self, subsystem):
        print("Do you want to open a subsytem")
        cha = paramiko.channel.Channel(1)
        cha.invoke_subsystem(subsystem)
    
    def read_data(self, n):
        channel(2).recv_ready()
        channel(2).recv(n)
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
        
    
    def start_new():
        print("... starting new client")
        transport.start_client()
        print("... do you want to start a new session as a server ? ")
        bool_new_server = input(str)
        if bool_new_server == "y":
            transport().start_server()
    
    def auth(self):
        print("... catching bad exception")
        try:
            paramiko.transport.Transport(self.hostname, self.port).auth_none(self.username) #get sock except
        except paramiko.BadAuthenticationType:
            print("This user is not allowed authentication")
    
    def keygen(self, content_file = "key.txt",bits=1024):
      key = RSA.generate(bits)    
      with open("key,txt", 'wb') as content_file:
        chmod("key.txt", 0)
        content_file.write(key.exportKey('PEM'))
      pubkey = key.publickey()
      with open("key.txt", 'wb') as content_file:
          content_file.write(pubkey.exportKey('OpenSSH'))
    
    def logging_all_banner(self):
        print(transport.get_banner())
        print("Do you want to output this to a file?")
        banner_bool = input(str)
        if banner_bool == "y":
            print("... saving the banner to a file")
            file = open(input(str), "r+")
            with file:
                file.write(transport.get_banner())

        
    def preference(self):
        print("requesting preferred config")
        transport().preferred_keys[input(str)]
        transport().preferred_compression[input(str)]
        transport().preferred_kex[(input(str))]
        transport().preferred_macs[input(str)]
        print(transport().get_security_options())
    
    def pre_ran_scripts(self):
	    print("Bash Script")
	    user_input_commands = input(str)
	  # bash scripts = the field for bash scripts
	    if user_input_commands == commands_to_run[0]:
	     os.listdir(input("please enter the path to your scripts"))
	     print("... running your bash scripts to this machine")
	     stdin.write('cat ' + bash_scripts)

    def send(self, content):
      channel(2).send(content)

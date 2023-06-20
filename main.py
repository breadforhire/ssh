#!/bin/env python
import sys
import os
from sqlite3 import connect 
import netifaces
import paramiko
import subprocess
import connect_listen
from sty import fg, bg, ef, rs
import threading
from sty import Style, RgbFg
import getopt
import logging
import json
import exploits
import main

netifaces.gateways()
interfaces = netifaces.interfaces()
addrs = netifaces.ifaddresses(str(interfaces[0]))
# add
#exploits.exploits().get_connect()
class main(connect_listen.connect_listen):
    def __init__(self, hostname, port, username, password, multithreading, logs, myfile, passfile):
        super().__init__(hostname, port, username , password)
        self.multithreading = multithreading
        self.logs = logs
        self.myfile = open("network.txt", "r+")
        self.passfile = open("pass.txt", "r+")



    def interface_get(self):
      print(str(addrs.keys()))
      print(str(netifaces.ifaddresses(str(interfaces[0]))))
      print(addrs[netifaces.AF_INET])
      print(addrs[netifaces.AF_LINK])


    def connect_normal(self):
     print(f'connecting to {self.hostname}')
     try:
      connect_listen.connect_listen.ssh_connect(self, pkey = None)
     except:
      print("error")

    def hexdump(self):
     connect_listen.connect_listen.socket_in()
     connect_listen.connect_listen.socket_transport()
     connect_listen.connect_listen._hexdump()

    def bruteforce(self):
     print("... bruteforcing into")

     #outer_c = main(multithreading = None , save_file = None, log_errs = None, log_suc = None, myfile = "pass.txt")

     #myline = outer_c.read_brute()
     my_line = self.myfile.readline()
     while my_line:
        connect_listen.connect_listen.ssh_connect(self, self.myfile.readline(), pkey = None)

    def testing_preferences(self):
      print("... requesting all preferences")
      my_line = self.myfile.readline()
      while my_line:
         connect_listen.connect_listen.preference(self, _pubkeys = self.myfile.readline(), _key = self.myfile.readline(), _compression = self.myfile.readline(), _kex = self.myfile.readline(), _macs = self.myfile.readline())


    def connect_auth_no_cred(self):
      print("Connecting Auth no username")
      connect_listen.connect_listen(hostname = input("hostname: "), username = input("username: "), password = None, port = 22).auth()

    def connect_pkey(self):
     connect_listen.connect_listen.ssh_connect(self, None, self.get_keyfile())

    def show_connections(self):
      print("[+] connections")
      print("[+]") #show hostname, netflow, current state



    def _read_network(self):
     clients = []
     print("reading network") # add a try and except statement
     #print(subprocess.check_output(['bash', 'discover.sh']))
     self.myfile.truncate(0)
     subprocess.check_output(['bash', 'discover.sh'], shell = True)
     print("[+]reading network done [+] connecting")

     my_line = self.myfile.readline()

     while my_line:
      try:
       print(f'Connecting{self.myfile.readline()}')
       connect_listen.connect_listen().ssh_connect(passwords = self.myfile.readline(), pkey = self.get_keyfile() )
      except:
        print(f'Connection Failed { self.myfile.readline() }')
        break

    def _jumphosts(self):
     print("[+] Jumping Host")
     connect_listen.connect_listen.jump_hosts(self,_jumphost = self.myfile.readline(), _jumppass = self.myfile.readline() )
     print(f'[+] Going Through {_jumphost} with {_jumppass}')

    def _cookie_bruteforce(self):
     #connect_listen.connect_listen()
     myline = self.myfile.readline()
     while myline:
      try:
       exploits.exploits().erlangcookie(self.myfile.readline())
      except:
          pass
    def handshake(self):
     connect_listen.connect_listen.socket_transport(self)
     connect_listen.connect_listen.capture_handshake(self)

    def info(self):
     exploits.exploits().info_dump()

    def read_config(self):
     print(f'[+] multithreading {self.multithreading}')
     print(f'[+] logging  {self.logs}')

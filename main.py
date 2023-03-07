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
class main:
    def __init__(self, multithreading, save_file, log_errs, log_suc, myfile):
        self.multithreading = multithreading
        self.save_file = save_file
        self.log_errs = log_errs
        self.log_suc = log_suc
        self.myfile = open("network.txt", "r+")



    #def get_main(self, multithreading = None , save_file = None, log_errs = None, log_suc = None):
     # outer_c = main.main(multithreading = None , save_file = None, log_errs = None, log_suc = None)
      #return outer_c
#MAKE CODE LESS SPAGHETTI!!!


    def interface_get(self):
      print(str(addrs.keys()))
      print(str(netifaces.ifaddresses(str(interfaces[0]))))
      print(addrs[netifaces.AF_INET])
      print(addrs[netifaces.AF_LINK])

    def open_two_terminals(self):
     proc1 = subprocess.Popen(['gnome-terminal', '-x', 'python', '__init__.py'])
     proc2 = subprocess.Popen(['gnome-terminal', '-x', 'python', '__init__.py'])
     proc1.wait()
     proc2.wait()



    def connect_normal(self):
     outer = connect_listen.connect_listen(hostname=input("hostname: "), username=input("username: "), password=input("password: "), port = 22)
     outer.ssh_connect(pkey = None)
     outer.set_connect()
     print(outer.get_connect)

    def hexdump(self):
     connect_listen.connect_listen(hostname = input("hostname: "), username = input("username: "), password = input("password: "), port = 22).inbound()

    def bruteforce(self):
     print("... bruteforcing into")

     #outer_c = main(multithreading = None , save_file = None, log_errs = None, log_suc = None, myfile = "pass.txt")

     #myline = outer_c.read_brute()
     hostname = input('hostname')
     username = input('username')
     my_line = self.myfile.readline()
     while myline:
        connect_listen.connect_listen(hostname = hostname, username = username, password = myfile.readline(), port = 22).ssh_connect(pkey= None)

    def testing_preferences(self):
      print("... reading all preferences")
      print("... requesting all preferences")
      my_line = myfile.readline()
      while my_line:
         connect_listen.connect_listen(hostname = hostname, username = username, password = password, port = 22).preference(_key = myfile.readline)


    def connect_auth_no_cred(self):
      print("Connecting Auth no username")
      connect_listen.connect_listen(hostname = input("hostname: "), username = input("username: "), password = None, port = 22).auth()

    def connect_pkey(self):
     dir_pkey = os.path.dirname("~/. ssh/id_rsa")
     print(dir_pkey)
     connect_listen.connect_listen(hostname = input("hostname: "), username = input("username: "), password = input("password: "), port = 22).ssh_connect(pkey = dir_pkey)

    def show_connections(self):
      print("[+] connections")
      print("[+]") #show hostname, netflow, current state



    def _read_network(self):
     clients = []
     print("reading network") # add a try and except statement
     #print(subprocess.check_output(['bash', 'discover.sh']))
     self.myfile.truncate(0)
     subprocess.check_output(['bash', 'discover.sh'], shell = True)
     print("")
     print("[+]reading network done [+] connecting")

     my_line = self.myfile.readline()

     while my_line:
      try:
       print(f'Connecting{self.myfile.readline()}')
       connect_listen.connect_listen(hostname = my_line, username = input("username: "), password = input("password: "), port = 22).ssh_connect(pkey = None)
      except:
        print(f'Connection Failed { self.myfile.readline() }')
        break

    def _jumphosts(self):
     print("JUMPING HOST")
     connect_listen.connect_listen(hostname = "127.0.0.1", username = "root", password = "pass", port = 22).jump_hosts("127.0.0.1", "jump")


    def read_config(self):
     print(f'[+] multithreading {self.multithreading}')
     print(f'[+] logging known hosts {self.log_suc}')
     print(f'[+] logging all errors {self.log_errs}')


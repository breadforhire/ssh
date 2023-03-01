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
#from netdiscover import *
netifaces.gateways()
interfaces = netifaces.interfaces()
addrs = netifaces.ifaddresses(str(interfaces[0]))

#add disclaimer


class main:
    def __init__(self, multithreading, save_file, log_errs, log_suc):
        self.multithreading = multithreading
        self.save_file = save_file
        self.log_errs = log_errs
        self.log_suc = log_suc
        
    def get_connect(self, *argv ):
      connect_listen.connect_listen()
    def graphics(self):
     fg.red = Style(RgbFg(255, 0, 0))
     print(fg.red + "       ____()()")
     print("      /      @@")
     print("`~~~~~\_;m__m._>o    jgs")
     print("SSH RAT")
     print("This tool is meant for information gathering and nothing more")
   



    def interface_get(self):
      print(str(addrs.keys()))
      print(str(netifaces.ifaddresses(str(interfaces[0]))))
      print(addrs[netifaces.AF_INET])
      print(addrs[netifaces.AF_LINK])

    def open_two_terminals():
     proc1 = subprocess.Popen(['gnome-terminal', '-x', 'python', 'Exploits.py'])
     proc2 = subprocess.Popen(['gnome-terminal', '-x', 'python', 'main.py'])
     proc1.wait()
     proc2.wait()
 
		   

    def connect_normal(self):
     outer = connect_listen.connect_listen(hostname=input(str), port= 22, username=input(str), password=input(str))

     outer.ssh_connect()
     outer.set_connect()
     print(outer.get_connect)

 
    def bruteforce(file):
      print("... bruteforcing into")
      file_name = open("user_config.txt", "r+")
      for lines in file_name(): connect_listen.connect_listen(hostname= file_name.readline(), username = file_name.readline(), password = file_name.readline(), port = 22)
       

    def testing_preferences(self):
      print("... reading all preferences")
      print(connect_listen.connect_listen.preference())
      print("... requesting all preferences")
    

    def jumping_hosts(self):
     print("... jumping from host to host") #if the connection is not recivered "jump" to next host 
     file_name = open("jump_host.txt", "r+")
     for lines in file_name(): connect_listen.connect_listen(hostname= file_name.readline(), username = file_name.readline(), password = file_name.readline(), port = 22)


    def connect_auth_no_cred(self):
      print("Connecting Auth no username")
      connect_listen.connect_listen(hostname = input("hostname"), username = input("username"), password = None, port = 22).auth()

    def connect_pkey(self):
     dir_pkey = os.path.dirname("~/. ssh/id_rsa")
     print(dir_pkey)
     connect_listen.connect_listen(hostname = input("hostname"), username = input("username"), password = input("password"), port = 22).ssh_connect(pkey = dir_pkey)

    def print_log_errs(self):
     dir_app = os.getcwd()
     logging.basicConfig(filename="/home/ender/Desktop/interpy/connect_listen.py", level=logging.DEBUG,
     format='%(asctime)s %(levelname)s %(name)s %(message)s')
     logger=logging.getLogger(__name__) # LOGGING DOES NOT WORK REMOVE METHOD

    def read_config(self):
     print(self.multithreading)
     print(self.log_suc)
     print(self.log_errs)

    def read_config_ssh(self):
     arr = json.loads("")
     d = {'dict1': {'foo': 1, 'bar': 2}, 'dict2': {'baz': 3, 'quux': 4}}
     #d_list = []
     #employee ='{"hostname":"09", "password": "Nitin", "port": 22 , "pkey": ""}
     ssh_dict = json.loads("arr.:json")

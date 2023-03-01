#!/bin/env python
import main
import os 
import exploits
import connect_listen
import paramiko
import logging


commands_user = ["normal-connect", "private-connect", "brute-pass-connect", "false-connect", "forward-agent-connect", "auth-no-pass", ]

commands_info_gathering = ["hexdump", "set_prefer_creds",]

def check_root_user():
     if os.geteuid() != 0:
      exit("You need to have root privileges to run this script.\nPlease try" )

def run():
  beg_mssg = main.main(multithreading = False, save_file = False, log_errs = True, log_suc = True)
  #beg_mssg.graphics()
  #beg_mssg.interface_get()
  #beg_mssg.read_config()
  beg_mssg._readnetwork()


  print(commands_user)
  print()
  while True:
   input_command = input(str)
   if commands_user[0] == input_command:
     try:
      outer = main.main(multithreading = False, save_file = None, log_suc = True, log_errs = True)
      outer.connect_normal()
     except: 
	     print("could not connect")
	     break
   if commands_user[1] == input_command:
    try:
     outer = main.main(multithreading = False, save_file = None, log_suc = True, log_errs = True)
     outer.connect_pkey()
    except Exception as e:
         logging.critical(e , exc_info = True)
check_root_user()
run()

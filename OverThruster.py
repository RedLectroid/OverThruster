#!/usr/bin/python
#uses HID-Project.h from https://github.com/NicoHood/HID, can be installed from Arduino Library Manager

import sys
import argparse
import os
import subprocess
import coreUtils
import winCore
import nixCore
import osxCore
import helperCore
import nfoCore
  
def mainMenu():

  menu = {}
  menu['0']="Info"
  menu['1']="Windows Payloads" 
  menu['2']="OSX Payloads"
  menu['3']="Linux Payloads"
  menu['4']="Helper/Listener Functions"
  menu['99']="Exit"

  while True:
    coreUtils.bannerMain()
    options=menu.keys()
    #options.sort(key=int)
    #for entry in options:
    for entry in sorted(options):
      print(entry, menu[entry])

    selection=input("\nPlease Select: ") 
    if selection =='1': 
      winCore.WinMenu() 
    elif selection == '2': 
      osxCore.osxMenu()
    elif selection == '3':
      nixCore.LinuxMenu()
    elif selection == '4':
      helperCore.helperMenu()
    elif selection == '0':
      nfoCore.generalInfo()
    elif selection == '99': 
      break
    else: 
      print("\n\n***That is not a valid option!***\n\n")


if __name__ == "__main__":
  mainMenu()

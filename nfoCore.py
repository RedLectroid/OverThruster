import coreUtils

def Win1info():
  print "\n\n"
  print "This payload will download a windows binary and execute it"
  print "You are required to specify the full URL of the binary to be downloaded, including the file name"
  print "As well as the other standard payload options (UACBypass, notification bubble, etc)"
  print "Example URL input: http://192.168.1.111/badBinary.exe"
  print "\n"
  print "Depending on which UAC Bypass technique you use, the binary will be dropped in:"
  print "1. The user's home folder"
  print "2. \\Windows\\System32 is you use the visiable UAC Bypass technique"
  print "3. \\Windows\\System32\\WindowsPowershell\\v1.0"
  print "\n"
  print "It is up to you to make sure it will get past AV, and to clean up after"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")
  
  
def Win2info():
  print "\n\n"
  print "This payload will download a powershell script and execute it"
  print "\n"
  print "You are required to specify the URL of the powershell to be downloaded, including the powershell script name"
  print "As well as the other standard payload options (UACBypass, notification bubble, etc)"
  print "Example URL input: http://192.168.1.111/maliciousPS.ps1"
  print "\n"
  print "The powershell script will run from memory"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")
  
def Win3info():
  print "\n\n"
  print "This payload will execute a powershell script that you provide"
  print "\n"
  print "You are required provide the powershell script contents, the payload will execute"
  print "As well as the other standard payload options (UACBypass, notification bubble, etc)"
  print "\n"
  print "the payload will automatically add \"powershell -nop -w hidden\""
  print "If you script is fully encoded (like Empire), please start it with -enc so it doesn't get wrapped with \" \" "
  print "\n"
  print "The powershell script will run from memory"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")
  
def Win4info():
  print "\n\n"
  print "This payload will type out a powershell script and execute it, creating a remote TCP Powershell prompt"
  print "\n"
  print "You are required to provide IP address and port the payload will connect back to"
  print "As well as the other standard payload options (UACBypass, notification bubble, etc)"
  print "\n"
  print "The powershell script will run from memory"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")
  
def Win5info():
  print "\n\n"
  print "This payload will add a User, add it to the Admin group, and add it to the RDP group"
  print "\n"
  print "You are required to provide the username and password, and optional IP and port"
  print "As well as the other standard payload options (UACBypass, notification bubble, etc)"
  print "This payload will optionally send the username and password to a listener (future feature*) "
  print "if you plan on attacking multiple machines"
  print "\n"
  print "***This payload does require Admin rights***"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")
  
def Win6info():
  print "\n\n"
  print "This payload will download Invote-Mimikatz.ps1 (by default from github) and execute it, then send the results to a listening server"
  print "\n"
  print "You are required to provide theIP address and port the output will be sent to"
  print "As well as the other standard payload options (UACBypass, notification bubble, etc)"
  print "\n"
  print "***This payload does require Admin rights***"
  print "Invoke-Mimikatz.ps1 will run from memory"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")
  
def Win7info():
  print "\n\n"
  print "This payload will add and entry to the host file in Windows"
  print "\n"
  print "You are required to provide the name and IP address to be entered into the host file"
  print "As well as the other standard payload options (UACBypass, notification bubble, etc)"
  print "\n"
  print "***This payload does require Admin rights***"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")
 
def Win8info():
  print "\n\n"
  print "This payload will download a file and place it on the current user's Desktop"
  print "\n"
  print "You are required to specify the full URL of the file to be downloaded, including the file name"
  print "As well as the other standard payload options (UACBypass, notification bubble, etc)"
  print "Example URL input: http://192.168.1.111/SecretHrData.doc"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")
  
def Win9info():
  print "\n\n"
  print "This payload will type out a powershell script and execute it, creating a remote TCP CMD prompt"
  print "\n"
  print "You are required to provide IP address and port the payload will connect back to"
  print "As well as the other standard payload options (UACBypass, notification bubble, etc)"
  print "\n"
  print "The powershell script will run from memory"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")
  
def UACBypassInfo():
  print "\n\n"
  print "Option 2. UAC Bypass technique will download FuzzySecurity's bypass technique from github, and run it"
  print "by default with the \"-Method ucmDismMethod\" argument, opening a Powershell prompt with Admin rights"
  print "There is no popup, but network lag affects how long the prompt takes to appear, and drops the file"
  print "\"dismcore.dll\" into the Windows\System32 folder"
  print "\n"
  print "Option 3. UAC Bypass technique will start a CMD Prompt from the Run Dialogue box with the RunAs argument"
  print "After a delay, it will press Alt-Y to select Yes from Yes/No dialogue box that appears"
  print "***This may get the user's attention***"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")
 
def bubbleInfo():
  print "\n\n"
  print "This option adds a notification bubble to popup from the system tray to distract the user"
  print "using the command wlrmdr.exe -s 60000 -f 1 -t \"Installing Drivers\" -m \"Please do not remove the device\""
  print "\n"
  raw_input("Please press Enter to return to the previous screen")
  print "\n"

def osx1info():
  print "\n\n"
  print "This payload will create a reverse TCP shell using netcat without the -e flag"
  print "\n"
  print "You are required to provide IP address and port the payload will connect back to"
  print "\n"
  print "This payload will run until the process is killed, so it will repeatedly attempt to connect to the IP you provide"
  print "\n"  
  raw_input("Please press Enter to return to the previous screen")
  
def osx2info():
  print "\n\n"
  print "This payload will create a reverse TCP shell using PHP"
  print "\n"
  print "You are required to provide IP address and port the payload will connect back to"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")

def osx3info():
  print "\n\n"
  print "This payload will create a reverse TCP meterpreter in PHP"
  print "\n"
  print "You are required to provide IP address and port the payload will connect back to"
  print "\n"
  print "\n"  
  raw_input("Please press Enter to return to the previous screen")
  
def nix1info():
  print "\n\n"
  print "This payload will create a reverse TCP shell using netcat without the -e flag"
  print "\n"
  print "You are required to provide IP address and port the payload will connect back to"
  print "\n"
  print "This payload will run until the process is killed, so it will repeatedly attempt to connect to the IP you provide"
  print "\n"  
  raw_input("Please press Enter to return to the previous screen")
  
def nix2info():
  print "\n\n"
  print "This payload will create a reverse TCP shell using PHP"
  print "\n"
  print "You are required to provide IP address and port the payload will connect back to"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")

def nix3info():
  print "\n\n"
  print "This payload will create a reverse TCP meterpreter in PHP"
  print "\n"
  print "You are required to provide IP address and port the payload will connect back to"
  print "\n"
  print "\n"  
  raw_input("Please press Enter to return to the previous screen")
  
  
  
def generalInfo():
  coreUtils.clearScreen()
  print "\n\n"
  print "GENERAL"
  print "OverThruster is designed to facilitate creating Arduino sketches for devices with the AtMega32U4 chipset"
  print "That can do keyboard emulation. Once plugged into a system, the malicious device will type out the contents"
  print "of the selected payload, which include download and execute binaries, custom powershell execution and more"
  print "Options include notification bubbles from system tray to distract users as well as UAC Bypass techniques"
  print "to get CMD prompts with elevated priveleges"
  print "\nREQUIREMENTS"
  print "This tool requires the HID-Project library for all Windows payloads"
  print "Which can be installed within the Arduino IDE: Sketch->.Include Library->manage Libraries and search for \"HID-Project\""
  print "\nABOUT ME"
  print "You can find me on twitter at @bhohenadel"
  print "and on github at https://github.com/RedLectroid"
  print "Thanks to: @loneferret and @mycurial for...alot"
  print "\n"
  raw_input("Please press Enter to return to the previous screen")

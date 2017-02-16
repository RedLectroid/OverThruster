# OverThruster
"I've been ionized, but I'm okay now." -Buckaroo Banzai.

###General Info
OverThruster is a tool to generate sketches for Arduinos when used as an HID Attack.  It was designed around devices with the ATMEGA32U4 chip, like the CJMCU-BEETLE, or the new LilyGo "BadUSB" devices popping up on ebay and aliexpress that look like USB sticks but contain an Arduino.  I wrote this because the few other tools out there that do similar don't have as many customization options like the UAC Bypass options or the notification bubble options.  I wanted to create something that could quickly generate a custom payload and that did not require anything extra to be install beyond the standard Python libraries and the Arduino IDE.  I also wrote this to get better at Python.  This is my first release of anything, so expect problems.

###Requirements
- An Arduino that supports keyboard emulation
- Python 2.7 (Python 3 version is coming)
- Arduino IDE: https://www.arduino.cc/en/Main/Software
- NicoHood's HID: https://github.com/NicoHood/HID/ (This can be installed straight from the Arduino IDE from the menu: Sketch->.Include Library->manage Libraries and search for "HID-Project")

###Use
1. start by launching OverThruster.py
2. Select the target's OS
3. Select the specific payload
4. Fill in the required settings
5. Generate the .ino file
6. Open the .ino file in the Arduino IDE
7. Flash the sketch to your Arduino device

###Notes

1. After flashing the payload, the Arduino IDE will disconnect the Arduino, then it will automatically reconnect, and deliver the payload. Be ready for characters to suddenly be typed to the screen; I recommend having notepad or similar open and focused when you flash the sketch
2. OverThruster currently drops the .ino file and the Metasploit .rc file in the working directory, so look for them there.
3. For the UAC Bypass techniques, timing is key.  Older devices will open the Terminal with Admin rights at a slower speed, and therefore you may need to adjust the delay() in the BypassUAC functions in the sketch
4. This is just the beginning.  Many more payloads, features, options and additions are coming.
5. Please contribute if you have something to add.

##Disclaimer
Don't do anything illegal with this.
Usage of OverThruster for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, provincial/state and federal laws. Developer assume NO liability and are NOT responsible for any misuse or damage caused by this program.

"Don't be mean; we don't have to be mean, cuz, remember, no matter where you go, there you are." - Buckaroo Banzai

##About me
You can find me on Twitter: [@bhohenadel](https://twitter.com/bhohenadel)

##Thanks
Thank you to my beautiful wife for putting up with my late nights while I worked on this, and her fantastic support she has always given me.

[@loneferret](https://twitter.com/loneferret) for the testing and the feedback and most importantly the encouragement when I first started playing with this idea

[@mycurial](https://twitter.com/myrcurial) for helping me get in the security industry and ...alot more

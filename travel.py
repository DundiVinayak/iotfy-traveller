 #!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import pycps

# Create a connection to a Clusterpoint database.
con = pycps.Connection('tcp://cloud-eu-0.clusterpoint.com:9007', 'dundivinayak', 'dundivinayak@gmail.com', 'vinu123@$', '2324')

    



continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the IOTfy Travel!!!"


# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    
    #UID.replace(" ","")
    #UID.replace(",","")
    
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
       
        # Print UID
        UID = "" + str(uid[0])+ "" + str(uid[1]) + "" + str(uid[2])+ "" + str(uid[3]) + ""
        print "THE USER " + UID
        
        try:
			print "Please Enter CHECK IN POINT: "
			Cin = sys.stdin.readline()
			print "Please Enter CHECK OUT POINT: "
			Cout = sys.stdin.readline()
			print "Please Enter FARE: "
			fare = sys.stdin.readline()
			con.replace({10: '<document> <Fare>'+fare+'</Fare> <Source>'+Cin+'</Source> <Destination>'+Cout+'</Destination> </document>'})
		except pycps.APIError as e:
			print(e)
        
        # disconnect from server
        
        print "EXIT" + UID
        
      

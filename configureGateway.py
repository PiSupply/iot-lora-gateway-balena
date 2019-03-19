import os
import sys
import urllib2
import json
import time

print("Gateway Configuring")

#Lets configure this how we do in our PHP version while also including balena variables



#Set the Gateway ID to part of the mac address
macAddress =
gatewayId = "504953" +

#Get Server ID
os.environ.get("TTN_ID")
#Get TTN Key
os.environ.get("TTN_KEY")

#That's all we need from balena

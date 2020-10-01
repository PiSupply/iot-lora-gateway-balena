import os
import sys
import urllib2
import json
import time
import shutil
import pprint
import codecs

print("Gateway Configuring")

#Get Server ID
gatewayTtnId = os.environ.get("TTN_ID")
#Get TTN Key
keyDetails = os.environ.get("TTN_KEY")
if(gatewayTtnId == None or keyDetails == None):
    print("Please set variables from balena console")
    sys.exit()
emailAddr = os.environ.get("CONTACT_EMAIL")

# Parse GW_GPS env var. It is a string, we need a boolean.
if(os.getenv("GW_GPS", "false")=="true"):
  gw_gps = True
else:
  gw_gps = False
#That's all we need from balena

#Now request from TTN API
ttnResponse = urllib2.urlopen("https://account.thethingsnetwork.org/api/v2/gateways/"+gatewayTtnId)
ttnJson = ttnResponse.read()
ttnData = json.loads(ttnJson)

#Set the Gateway ID to part of the mac address
gatewayGenId = str.encode("IOT"+gatewayTtnId[-5:])
gatewayGenId = codecs.encode(gatewayGenId, "hex")

routerUrl = "router." + ttnData['router']['address'][0:-5]

#Check for latitude and longitude data
try:
    latitude = ttnData['location']['lat']
    longitude = ttnData['location']['lng']
except (TypeError, AttributeError):
    latitude = 0
    longitude = 0

#Open Up the config file
configLocation = '/opt/iotloragateway/local_conf.json'
with open(configLocation, 'r') as f:
    data = json.load(f)

    # Lets set the easy stuff first
    data["gateway_conf"]["servers"][0]["serv_gw_id"] = gatewayTtnId
    try:
        data["gateway_conf"]["description"] = ttnData['attributes']['description']
    except (TypeError, AttributeError):
        data["gateway_conf"]["description"] = "Pi Supply Gateway"
    data["gateway_conf"]["servers"][0]["serv_gw_key"] = keyDetails
    data["gateway_conf"]["gateway_ID"] = gatewayGenId.decode()
    data["gateway_conf"]["servers"][0]["server_address"] = routerUrl
    data["gateway_conf"]["contact_email"] = emailAddr

    # Use hardware GPS
    if(gw_gps):
      data["gateway_conf"]["gps"] = "true"
      data["gateway_conf"]["fake_gps"] = "false"
      data["gateway_conf"]["gps_tty_path"] = os.getenv('GW_GPS_PORT', "/dev/serial0")
    # Use fake GPS with coordinates from TTN
    elif(gw_gps==False and latitude!=0 and longitude!=0):
      data["gateway_conf"]["gps"] = "true"
      data["gateway_conf"]["fake_gps"] = "true"
      data["gateway_conf"]["ref_latitude"] = latitude
      data["gateway_conf"]["ref_longitude"] = longitude
      data["gateway_conf"]["ref_altitude"] = ttnData['altitude']
    # No GPS coordinates
    else:
      data["gateway_conf"]["gps"] = "false"
      data["gateway_conf"]["fake_gps"] = "false"

os.remove(configLocation)
with open(configLocation, 'w') as f:
    json.dump(data, f, indent=4)

freqResponse = urllib2.urlopen(ttnData['frequency_plan_url'])
freqJson = freqResponse.read()
freqData = json.loads(freqJson)
# Copy the frequency plan over
boot_conf_file = "/opt/iotloragateway/global_conf.json"
with open(boot_conf_file, 'w') as f:
    json.dump(freqData, f, indent=4)

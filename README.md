# iot-lora-gateway-balena

This Github Repo is a setup for using the Pi Supply IoT LoRa Gateway with Balena Cloud and is based on the guide at https://github.com/jpmeijers/ttn-resin-gateway-rpi with some optimisations and tweaks made for the Pi Supply Gateway.

# Notice
This is still in testing, if you have one of our beta boards and can test then please report any issues.

# How To guide

You can find the full guide on how to setup your gateway using this method on our makerzone at

One-click deploy to balenaCloud:

[![balena deploy button](https://balena.io/deploy.png)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/PiSupply/iot-lora-gateway-balena&defaultDeviceType=raspberry-pi)


# Variables
The software only requires 3 variables to be set.

The email variable ```CONTACT_EMAIL``` can be set in the application's envrionment variables.

For each gateway you must then go into it and set two device variables:

`TTN_ID` - This is the ID as in the TTN Console.

`TTN_KEY` - This is the Gateway's Key as from the TTN Console.

`GW_GPS` - This determines whether you are using a hardware GPS module or not (add true if you have one)


## GPS module
You will also require to enable UART on the Raspberry Pi for GPS to fully function. To do this on the Balena console click your device, and then at the side Device Configuration, then enable where it says Enable Uart.

## Pi 3, 4 & Zero W
You'll also need to swap the serial port used by the bluetooth module around, you can do this by in the same device configuration tab adding ```,"miniuart-bt"``` to the end of the ```Define DT overlays``` list, for example it should look like ```"vc4-fkms-v3d", "miniuart-bt"```

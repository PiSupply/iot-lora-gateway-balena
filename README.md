# iot-lora-gateway-balena

This Github Repo is a setup for using the Pi Supply IoT LoRa Gateway with Balena Cloud and is based on the guide at https://github.com/jpmeijers/ttn-resin-gateway-rpi with some optimisations and tweaks mad efor the Pi Supply Gateway.

# Notice
This is still in testing, if you have one of our beta boards and can test then please report any issues.

# How To guide

You can find the full guide on how to setup your gateway using this method on our makerzone at

# Variables
The software only requires 3 variables to be set.

The email variable ```CONTACT_EMAIL``` can be set in the application's envrionment variables.

For each gateway you must then go into it and set two device variables:
```TTN_ID``` - This is the ID as in the TTN Console.
```TTN_KEY``` - This is the Gateway's Key as from the TTN Console.

Another variable will be used soon.

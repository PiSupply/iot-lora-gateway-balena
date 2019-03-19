#!/bin/bash
python /opt/iotloragateway/configureGateway.py
if [ ! -d "/sys/class/gpio/gpio22" ]; then
    echo "22" > /sys/class/gpio/export
fi
echo "out" > /sys/class/gpio/gpio22/direction
echo "1" > /sys/class/gpio/gpio22/value
sleep 1
echo "0" > /sys/class/gpio/gpio22/value

/opt/iotloragateway/iot-lora-gateway

#/bin/bash

while [ -z $IP_ADDRESS ]
do
	IP_ADDRESS=`ifconfig wlan0|grep "inet addr"|cut -f 2 -d ":"|cut -f 1 -d " "`
	if [ ! -z "$IP_ADDRESS" ]; then
		echo "IP Address is: $IP_ADDRESS"
	else
		echo "Waiting for IP Address..."
		sleep 5
	fi
done

python nextmetro.py

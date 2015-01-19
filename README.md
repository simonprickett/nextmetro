# nextmetro
Next DC Metro from Wiehle-Reston East Station

TODO Write up notes on configuring Raspberry Pi, required hardware etc.   

TODO:

* Auto login as root
* Configure wifi
* Set WMATA_API_KEY
* Install Python dependencies
* Install Python code
* Set to run on boot
* Test

AUTO LOGIN:

```
sudo vi /etc/inittab
```

Find:

```
1:2345:respawn:/sbin/getty —noclear 38400 tty1
```

comment it out #

Add below:

```
1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1
```

Save, exit, reboot to check

CONFIGURE WIFI:

(assuming root login, pi booted with wifi adapter plugged in)

```
vi /etc/network/interfaces
```

Should look like:

```
auto lo

iface lo inet loopback
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp
```

Save and exit.

(assuming root login)

```
vi /etc/wpa_supplicant/wpa_supplicant.conf
```

assuming WPA2 setup...

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
ssid=“NETWORK SSID"
psk=“NETWORK PASSWORD"
proto=RSN
key_mgmt=WPA-PSK
pairwise=CCMP
auth_alg=OPEN
}
```

Save, exit reboot

Once rebooted, test:

```
ping google.com
```

Should return pings.

SET WMATA API KEY

As root:

```
vi ~/.profile
```

Add line at the bottom:

```
export WMATA_API_KEY=your_api_key
```

Save and exit.

Reboot.  When logged in as root test, by:

```
echo $WMATA_API_KEY
```

Should return your key.

INSTALL PYTHON DEPENDENCIES:

(as root)

```
apt-get update
apt-get install python-pip
apt-get install python-dev
pip install requests
pip install schedule
pip install unicornhat
```

INSTALL UNICORN HAT STUFF

get their github
run install script

INSTALL PYTHON CODE:

(as root)

```
cd
git clone https://github.com/simonprickett/nextmetro.git
```

TEST:

(attach unicorn hat)

(as root)

```
cd ~/nextmetro
python nextmetro.py
```

AUTO RUN ON BOOT:

As root

Add to ~/.profile:

```
/usr/bin/python /root/nextmetro/nextmetro.py
```
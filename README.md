# GPIONATOR
A simple web UI for interfacing with pi face on the raspberry pi
## Setup
### Prerequisites
install apache
```bash
sudo apt-get update
sudo apt-get install apache2
```
Test whether it works by visiting http://localhost/ on pi or entering the ip address of the pi on another device
### Adding files
Replace the files in the directory ```/var/www/``` with files in from the repository
Place the files in cgi-bin folder to ```/usr/lib/cgi-bin```
## Known Issues
No code implemented to query current pin states

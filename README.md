# Traps Event Notifier (TEN)

This app was written for Palo Alto Networks to gather Malware Events from the Traps Cloud Service and send Email Notifications.  
## Install:
  
  pip install selenium
  
  pip install smtplib
  
  pip install argparse
  
  pip install getpass
  
  pip install warnings
 
## Usage:
```
usage: traps.py [-h] [--traps TRAPS] [--events EVENTS]
                [--emailuserid EMAILUSERID] [--emailreceiver EMAILRECEIVER]
                [--trapsuser TRAPSUSER] [--mailserver MAILSERVER]
                [--mailserverport MAILSERVERPORT] [--phantompath PHANTOMPATH]

Usage Example: 

python traps.py --traps mytrapsservicename --events 20 --emailuserid anyone@anywhere.com --emailreceiver anyone@anywhere.com --trapsuser myusername@paloaltonetworks.com --mailserver my.mailsever.com --mailserverport 465 --phantompath /yourpath/bin/phantomjs

optional arguments:

  -h, --help            show this help message and exit
  
  --traps TRAPS         Traps Service Name
  
  --events EVENTS       Number of Events
  
  --emailuserid EMAILUSERID
  
                        Username for Email Account
                        
  --emailreceiver EMAILRECEIVER
  
                        Email Address to receive email
                        
  --trapsuser TRAPSUSER
  
                        Traps Username
                        
  --mailserver MAILSERVER
  
                        Mail Server
                        
  --mailserverport MAILSERVERPORT
  
                        Mail Server Port
                        
  --phantompath PHANTOMPATH
  
                        Path to PhantomJS Web Client (Required)
                        
  ```

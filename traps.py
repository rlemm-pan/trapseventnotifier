from selenium import webdriver
import json
import smtplib
import argparse
from argparse import RawTextHelpFormatter
import getpass
import warnings
warnings.filterwarnings("ignore")

number_of_events = ''
traps_cloud_name = ''
mail_user = ''
mail_password = ''
traps_username = ''
traps_password = ''
to = []
mail_server = ''
mail_port = 0
phantomJS_path = ''

parser = argparse.ArgumentParser(add_help=True,
                    formatter_class=RawTextHelpFormatter,
                    description='Usage Example: \n\npython mech.py --traps mytrapsservicename --events 20 --emailuserid anyone@anywhere.com --emailreceiver anyone@anywhere.com --trapsuser myusername@paloaltonetworks.com --mailserver my.mailsever.com --mailserverport 465')

parser.add_argument("--traps", action="store",
                    help="Traps Service Name")

parser.add_argument("--events", action="store",
                    help="Number of Events")

parser.add_argument("--emailuserid", action="store",
                    help="Username for Email Account")

parser.add_argument("--emailreceiver", action="store",
                    help="Email Address to receive email")

parser.add_argument("--trapsuser", action="store",
                    help="Traps Username")

parser.add_argument("--mailserver", action="store",
                    help="Mail Server")

parser.add_argument("--mailserverport", action="store",
                    help="Mail Server Port")

parser.add_argument("--phantompath", action="store",
                    help="Path to PhantomJS Web Client (Required)")

args = parser.parse_args()

if args.traps:
    traps_cloud_name = args.traps
if args.events:
    number_of_events = args.events
if args.emailuserid:
    mail_user = args.emailuserid
if args.emailreceiver:
    to = [args.emailreceiver]
if args.trapsuser:
    traps_username = args.trapsuser
if args.mailserver:
    mail_server = args.mailserver
if args.mailserverport:
    mail_server_port = args.mailserverport
if args.phantompath:
    phantomJS_path = args.phantompath

if mail_user == '':
    mail_user = raw_input("\nValid login credentials required.\nPlease enter your Email username: ")
if traps_username == '':
    traps_username = raw_input("\nValid login credentials required.\nPlease enter your Traps username: ")
if traps_cloud_name == '':
    traps_cloud_name = raw_input("Please enter your Traps Service Name: ")
if number_of_events == '':
    number_of_events = raw_input("\nDevices will require valid login credentials.\nPlease enter your Traps username: ")
if mail_server == '':
    mail_server = raw_input("Please enter your Mail Server name/IP: ")
if mail_server_port == '':
    mail_server_op = float(raw_input("Please enter your Mail Server Port: "))
if phantomJS_path == '':
    phantomJS_path = float(raw_input("Please enter the path to PhantomJS Web Client: "))
if mail_password == '':
    mail_password = getpass.getpass(prompt='Please enter your mail password: ')
if traps_password == '':
    traps_password = getpass.getpass(prompt='Please enter your Traps password: ')
else:
    pass

formatter = "{0:<15}{1:<17}{2:<70}{3:<20}{4:<20}"
result = formatter.format('Machine Name', 'Machine IP', 'FileName', 'Prevention Mode', 'Time') + '\n'
url = "https://" + traps_cloud_name + ".traps.paloaltonetworks.com"
events = url + "/api/v1/events?limit=" + number_of_events
sent_from = mail_user
subject = 'Malware Detected'
browser = webdriver.PhantomJS(phantomJS_path)
browser.get(url)
username = browser.find_element_by_id("Email")
password = browser.find_element_by_id("Password")
submitButton = browser.find_element_by_class_name("loginbtn")
username.send_keys(traps_username)
password.send_keys(traps_password)
submitButton.click()
browser.get(events)
json_load = json.loads(browser.find_element_by_tag_name("pre").text)

for item in json_load['data']:
    name = item['agent']['name']
    ip = item['agent']['ip']
    filename = item['sourceFileName']
    prevent = item['preventionMode']
    time = item['time']
    result += formatter.format(name, ip, filename, prevent, time) + '\n'

def send_email():
    global body, result, email_text
    try:
        server = smtplib.SMTP_SSL(mail_server, mail_server_port)
        server.ehlo()
        server.login(mail_user, mail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
    except:
        pass

body = 'Traps has found Malware on the following Machines reported from the Traps Cloud Service: ' + url + '\n' + '\n' + result
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

send_email()

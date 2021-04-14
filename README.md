# meraki_snort_blocklist_check

> This will check your Meraki Client destination sites against the Snort Blocklist and generate a report. The report will have all sites visited and indicate if any of them are active on the Snort blocklist. 

> Basically a nice open source way of keeping track of some of your network activity :).

## Prereqs

1. Python and pip package manager installed on your host computer / dev machine.

2. Active Meraki Account
3. Meraki API key
4. Git installed on computer

## Running it

Using git on command line...

`git clone https://github.com/JockDaRock/meraki_snort_blocklist_check`

and then

`cd meraki_snort_blocklist_check`

and

`cp env.template .env`

> You will want to edit the .env file to add in the API key and network ID you are looking to check.

Then run the following commands

`pip3 install -r requirements.txt`

and then

`python3 meraki_site_check.py`

In the same directory as this file you will have an excel file that has matched your Meraki sites visited from your network and checked to see if it is part of the updated blocklist.

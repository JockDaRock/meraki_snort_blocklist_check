import requests
import time
from openpyxl import Workbook, load_workbook
import re
import datetime
from dotenv import load_dotenv
import os
import ip_controller
import meraki_controller
import xl_controller

load_dotenv()

if __name__ == "__main__":
    # Enter your Meraki Org ID and assoicated Meraki API key to use this application

    netID = os.environ.get('NETID')
    apiKey = os.environ.get('APIKEY')
    timespan = "7200"
    #insert logging here

    timestamp = datetime.datetime.isoformat(datetime.datetime.now())
    #insert logging here

    header_row = {"A1": "Destination", "B1": "Active Blacklist",  "C1": "Protocol to Dest", "D1": "Dest Port", "E1": "KB Recv", "F1": "KB Sent", "G1": "Packet Flows", "H1": "Meraki Clients", "I1": "Time Active Milliseconds"}
    #insert logging here
    
    workbook = Workbook()
    sheet = workbook.active
    #insert logging here

    sheet["A1"] = header_row["A1"]
    sheet["B1"] = header_row["B1"]
    sheet["C1"] = header_row["C1"]
    sheet["D1"] = header_row["D1"]
    sheet["E1"] = header_row["E1"]
    sheet["F1"] = header_row["F1"]
    sheet["G1"] = header_row["G1"]
    sheet["H1"] = header_row["H1"]
    sheet["I1"] = header_row["I1"]

    workbook.save(filename="dest_talos_blacklist_check_{0}.xlsx".format(timestamp))
    #insert logging here

    meraki_resp = meraki_controller.meraki_network_traffic(netID, apiKey, timespan)
    print(xl_controller.xl_populate(meraki_resp, timestamp, workbook))
    #insert logging here


    workbook.save(filename="dest_talos_blacklist_check_{0}.xlsx".format(timestamp))

    #insert logging here


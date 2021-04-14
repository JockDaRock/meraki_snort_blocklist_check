import requests
import time
from openpyxl import Workbook, load_workbook
import ipaddress
import re
import datetime
import socket
from dotenv import load_dotenv
import os

load_dotenv()

def is_ip_or_hostname(host_ip):
    re_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    ip = re.findall(re_ip, host_ip)
    if len(ip) == 0:
        return "hostname"
    else:
        return "ip"


def is_private_ip(ip_addy):
    priv_ip = ipaddress.ip_address(ip_addy).is_private
    return priv_ip

def get_block_list():
    block_list_req = requests.get("https://www.snort.org/downloads/ip-block-list")
    block_list_text = block_list_req.text
    
    block_list_array = block_list_text.splitlines()

    return block_list_array

def convert_host_to_ip(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except:
        ip = "unknown"
        return ip

def meraki_network_traffic(net_ID, api_key, time_span, timestamp, workbook):

    url = "https://api.meraki.com/api/v1/networks/{0}/traffic".format(net_ID)

    querystring = {"timespan": time_span}

    headers = {
        'Accept': "*/*",
        'X-Cisco-Meraki-API-Key': api_key,
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    #insert logging here

    block_list = get_block_list()
    
    site_json = response.json()
    count = 2

    xl_sheet = workbook.active

    for i in site_json:
        meraki_dest = i["destination"]
        app = i["application"]
        protocol = i["protocol"]
        dest_port = i["port"]
        kilo_bytes_recv = i["recv"]
        kilo_bytes_sent = i["sent"]
        num_flows = i["flows"]
        active_time = i["activeTime"]
        num_client = i["numClients"]

        if meraki_dest == None:
            print("Destination is null, application type {0}.".format(app))
        else:
            if is_ip_or_hostname(meraki_dest) == "hostname":
                ip = convert_host_to_ip(meraki_dest)
                if ip in block_list:
                    active_blocklist = True

                    #insert logging here
                
                    xl_sheet["A{0}".format(str(count))] = meraki_dest
                    xl_sheet["B{0}".format(str(count))] = str(active_blocklist)
                    xl_sheet["C{0}".format(str(count))] = protocol
                    xl_sheet["D{0}".format(str(count))] = dest_port
                    xl_sheet["E{0}".format(str(count))] = kilo_bytes_recv
                    xl_sheet["F{0}".format(str(count))] = kilo_bytes_sent
                    xl_sheet["G{0}".format(str(count))] = num_flows
                    xl_sheet["H{0}".format(str(count))] = num_client
                    xl_sheet["H{0}".format(str(count))] = active_time

                    workbook.save(filename="dest_talos_blacklist_check_{0}.xlsx".format(timestamp))

                    count = count + 1
                else:
                    active_blocklist = ip in block_list

                    #insert logging here
                
                    xl_sheet["A{0}".format(str(count))] = meraki_dest
                    xl_sheet["B{0}".format(str(count))] = str(active_blocklist)
                    xl_sheet["C{0}".format(str(count))] = protocol
                    xl_sheet["D{0}".format(str(count))] = dest_port
                    xl_sheet["E{0}".format(str(count))] = kilo_bytes_recv
                    xl_sheet["F{0}".format(str(count))] = kilo_bytes_sent
                    xl_sheet["G{0}".format(str(count))] = num_flows
                    xl_sheet["H{0}".format(str(count))] = num_client
                    xl_sheet["H{0}".format(str(count))] = active_time

                    workbook.save(filename="dest_talos_blacklist_check_{0}.xlsx".format(timestamp))

                    count = count + 1

            elif is_private_ip(meraki_dest):
                print("Meraki destination {0} is a private address and will not be checked.".format(meraki_dest))
            else:
                if meraki_dest in block_list:
                    active_blocklist = True

                    #insert logging here
                
                    xl_sheet["A{0}".format(str(count))] = meraki_dest
                    xl_sheet["B{0}".format(str(count))] = str(active_blocklist)
                    xl_sheet["C{0}".format(str(count))] = protocol
                    xl_sheet["D{0}".format(str(count))] = dest_port
                    xl_sheet["E{0}".format(str(count))] = kilo_bytes_recv
                    xl_sheet["F{0}".format(str(count))] = kilo_bytes_sent
                    xl_sheet["G{0}".format(str(count))] = num_flows
                    xl_sheet["H{0}".format(str(count))] = num_client
                    xl_sheet["H{0}".format(str(count))] = active_time

                    workbook.save(filename="dest_talos_blacklist_check_{0}.xlsx".format(timestamp))

                    count = count + 1
                else:
                    active_blocklist = False

                    #insert logging here
                
                    xl_sheet["A{0}".format(str(count))] = meraki_dest
                    xl_sheet["B{0}".format(str(count))] = str(active_blocklist)
                    xl_sheet["C{0}".format(str(count))] = protocol
                    xl_sheet["D{0}".format(str(count))] = dest_port
                    xl_sheet["E{0}".format(str(count))] = kilo_bytes_recv
                    xl_sheet["F{0}".format(str(count))] = kilo_bytes_sent
                    xl_sheet["G{0}".format(str(count))] = num_flows
                    xl_sheet["H{0}".format(str(count))] = num_client
                    xl_sheet["H{0}".format(str(count))] = active_time

                    workbook.save(filename="dest_talos_blacklist_check_{0}.xlsx".format(timestamp))
                    #insert logging here

                    count = count + 1
            
    #insert logging here
    return "All Done!!!"


if __name__ == "__main__":
    # Enter your Meraki Org ID and assoicated Meraki API key to use this application

    netID = "L_566327653141850389"
    apiKey = "35ef10ca8b5e9de04013c5c54b1ba5304c87b95a"
    #timespan = "2592000"
    #timespan = "86400"
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

    
    print(meraki_network_traffic(netID, apiKey, timespan, timestamp, workbook))
    #insert logging here


    workbook.save(filename="dest_talos_blacklist_check_{0}.xlsx".format(timestamp))

    #insert logging here

